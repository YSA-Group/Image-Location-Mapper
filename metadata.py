import PIL.Image

img = PIL.Image.open("test.jpg")

import PIL.ExifTags
exif = {
    PIL.ExifTags.TAGS[k]: v
    for k, v in img._getexif().items()
    if k in PIL.ExifTags.TAGS 
}

latPre = exif['GPSInfo'][2]
lonPre = exif['GPSInfo'][4]

print(exif['GPSInfo'])
print(latPre)
print(lonPre)


latitude = float(((((latPre[0] * 60) + latPre[1])* 60 ) + latPre[2]) / 60 / 60)
longitude = float(((((lonPre[0] * 60) + lonPre[1])* 60 ) + lonPre[2]) / 60 / 60)

if exif['GPSInfo'][1] == 'S':
    latitude *= -1
if exif['GPSInfo'][3] == 'W':
    longitude *= -1

print(latitude)
print(longitude)