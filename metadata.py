import PIL.Image

img = PIL.Image.open("test.jpg")

import PIL.ExifTags
exif = {
    PIL.ExifTags.TAGS[k]: v
    for k, v in img._getexif().items()
    if k in PIL.ExifTags.TAGS
   
}

north = exif['GPSInfo'][2]
west = exif['GPSInfo'][4]

latitude = float(((((north[0] * 60) + north[1])* 60 ) + north[2]) / 60 / 60)
longitude = float(((((west[0] * 60) + west[1])* 60 ) + west[2]) / 60 / 60)

print(latitude)
print(longitude)