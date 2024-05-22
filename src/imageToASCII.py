from PIL import Image

#TODO: Improve 'pixelStride' functionality, use argparser to create command-line interface

#ascii characters from most to least bright
ASCII_MAP = ['.', ',', ':', ';', '/', '#']

#returns brightness in 0 to 255 (inclusive) range
def getBrightness(pixel):
    return (pixel[0]+pixel[1]+pixel[2])/3

#returns the single ASCII value associated with a (group of) pixel(s) based on (average) pixel brightness
def getASCII(pixelRGBs):
    brightness = [getBrightness(pixelRGB) for pixelRGB in pixelRGBs]
    brightness = sum(brightness)/len(brightness)
    index = int((brightness*len(ASCII_MAP))//256)
    return ASCII_MAP[index]

#writes a row buffer to a text file using writelines
def writeASCIIRowBuffer(rowBuffer, name):
    try:
        with open(f'images/{name}.txt', 'w') as f:
            f.writelines(rowBuffer)
    except: 
        print('Couldn\'t write the provided row buffer to the file at:', f'images/{name}.txt')
        exit(-1)

#creates a list of strings where each string represents the ASCII values found for each pixel in a row of the input image
def getASCIIRowBuffer(RGBImage, pixelStride=1):
    width, height = RGBImage.size
    asciiRowBuffer = []
    for x in range(0, width, pixelStride):
        curRow = ''
        for y in range(0, height, pixelStride):
            maxX = min(width-1, x + pixelStride)
            maxY = min(height-1, y + pixelStride)
            pixels = []
            for x in range(x, maxX):
                for y in range(y, maxY):
                    pixels.append(image.getpixel((x, y)))
            curRow += getASCII(pixels)
        asciiRowBuffer.append(curRow)
    #transpose the result
    return [''.join(list(x)) for x in zip(*asciiRowBuffer)]
    

image = Image.open("images/mules-on-mountain-1.jpg").convert('RGB')
asciiRowBuffer = getASCIIRowBuffer(image, 10)

#test code for now just prints out each row
for row in asciiRowBuffer:
    print(row)
#writeASCII(asciiRowBuffer, 'test')

#will be used to create command-line interface
if __name__ == 'main':
    pass