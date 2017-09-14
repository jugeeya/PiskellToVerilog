import sys

def main():
    if (len(sys.argv) != 2):
        print("Needs one argument: piskell file name")
        exit()
    filename = sys.argv[1]
    spriteName = filename[:-2]
    
    with open(filename) as f:
        lines = f.readlines()
    lines = [x.strip('\n') for x in lines]
    
    #number of frames
    numFrames = int(lines[2][-1])
    #frame width and height
    width=int(lines[3][-3:]) if (lines[3][-3:].isdigit()) else int(lines[3][-2:])
    height=int(lines[4][-3:]) if (lines[4][-3:].isdigit()) else int(lines[4][-2:])

    print("parameter %sWidth = %d;" % (spriteName, width), end='\n')
    print("parameter %sHeight = %d;" % (spriteName, height), end='\n')
    
    #FOR SINGLE FRAMES
    if (numFrames == 1):
        print("reg [8:0] %s [%d:0] = {" % (spriteName, width*height-1), end="")
        j = 0
        for i in lines:
            if (j >= 10 and j < (10 + height)):
                pixels = [x.strip() for x in i.split(',')]
                pixNum = 0
                for p in pixels:
                    if (p != ""):
                        isPixel = 1 if (int(p[3:4], 16) != 0) else 0
                        red = int(p[8:10], 16)
                        green = int(p[6:8], 16)
                        blue = int(p[4:6], 16)
                        red = red * 7 // 255
                        green = green * 7 // 255
                        blue = blue * 3 // 255
                        redBinary = '{0:03b}'.format(red)
                        greenBinary = '{0:03b}'.format(green)
                        blueBinary = '{0:02b}'.format(blue)
                        fullBinary = "9'b%d%s%s%s" % (isPixel, redBinary, greenBinary, blueBinary)
                        print(fullBinary, end="")
                        if (pixNum == (width - 1) and j == (10 + height - 1)):
                            print('};', end="\n")
                        else:
                            print(',', end="")
                            pixNum = pixNum + 1
            j = j + 1
        exit()

    #FOR MULTIPLE FRAMES
    for k in range(0, numFrames):
        print("reg [8:0] %sFrame%d [%d:0] = {" % (spriteName, k+1,width*height-1), end="")
        j = 0
        for i in lines:
            #starts at 10
            if (j >= (k * (height + 2)) + 10 and j < (k * (height + 2)) + 10 + height):
                pixels = [x.strip() for x in i.split(',')]
                pixNum = 0
                for p in pixels:
                    if (p != ""):
                        isPixel = 1 if (int(p[3:4], 16) != 0) else 0
                        red = int(p[8:10], 16)
                        green = int(p[6:8], 16)
                        blue = int(p[4:6], 16)
                        red = red * 7 // 255
                        green = green * 7 // 255
                        blue = blue * 3 // 255
                        redBinary = '{0:03b}'.format(red)
                        greenBinary = '{0:03b}'.format(green)
                        blueBinary = '{0:02b}'.format(blue)
                        fullBinary = "9'b%d%s%s%s" % (isPixel, redBinary, greenBinary, blueBinary)
                        print(fullBinary, end="")
                        if (pixNum == (width - 1) and j == ((k * (height + 2)) + 10 + height - 1)):
                            print('};', end="\n")
                        else:
                            print(',', end="")
                    pixNum = pixNum + 1
            j = j + 1
        
main()
