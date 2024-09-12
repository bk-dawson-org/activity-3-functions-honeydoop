import math

def getCylinderVolume(radius, height) :
    volume = math.pi * (radius ** 2) * height
    return volume

x = getCylinderVolume(10, 12)
y = getCylinderVolume(2, 6)
print(int(x))
print(int(y))

#wheeeee skipping this line cus yeeehaaaa

def getNumberOfSlices(radius, height, volumeOfSlice) :
    volume = getCylinderVolume(radius, height)
    numberOfSlices = volume / volumeOfSlice
    return int(numberOfSlices)

numberOfSlices1 = getNumberOfSlices(10, 10, 100)
print(numberOfSlices1)