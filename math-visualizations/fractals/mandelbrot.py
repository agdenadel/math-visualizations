from __future__ import division
import cmath
from PIL import Image
from math import sqrt, log

# https://www.youtube.com/watch?v=NGMRB4O922I

def mandelbrot(c, endpoint):
    def iterate(x_n, c):
        return x_n * x_n + c
    x = [0] * endpoint
    x[0] = 0 + 0j

    
    for i in range(1, endpoint):
        x[i] = iterate(x[i-1], c)

        if (x[i] * x[i].conjugate()).real >= 4:
            return i
        
    return endpoint


# moves origin to the center of the image and gives us typical axes (x increases from
# left to right and y increases from bottom to top)
def indexToXYCoordinate(index, height, width):
    x = index % width # based on 0,0 being top right corner and increasing going right
    y = index // width # based on 0,0 being top right corner and increasing going down

    x = x - width//2
    y = -y + height//2

    return (x,y)

def getComplexNumberFromCoordinate(coordinate, xOffset, yOffset, height, width, zoomFactor):
    a = (coordinate[0] + xOffset) / (width/zoomFactor) 
    b = (coordinate[1] + yOffset) / (height/zoomFactor)
    return complex(a,b)
    
def main():
    width = 10000
    height = 10000

    xOffset = 0
    yOffset = 0

    zoomFactor = 4

    maxEndpoint = 100

    pixelIndices = range(height*width)

    colors = [(255,255,255)] * (height * width)


    for pixelIndex in pixelIndices:
        coordinate = indexToXYCoordinate(pixelIndex, height, width)

        complexNumber = getComplexNumberFromCoordinate(coordinate, xOffset, yOffset, height, width, zoomFactor)
        endpoint = mandelbrot(complexNumber, maxEndpoint)

        if endpoint == maxEndpoint:
            colors[pixelIndex] = (0,0,0)
        else:
            colorChange = int(endpoint / maxEndpoint * 255)
            colors[pixelIndex] = (colorChange, 0, 0)

    img = Image.new('RGB', (width, height))
    img.putdata(colors)
    img.save('image.png')
    
    
if __name__ == "__main__":
    main()
    
    
