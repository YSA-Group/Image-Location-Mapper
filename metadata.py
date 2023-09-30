import PIL.Image
import PIL.ExifTags
import os

class image:
    def __init__(self, imgDir):
        self.imgDir = imgDir
        self.img = PIL.Image.open(imgDir)
        self.exif = {
            PIL.ExifTags.TAGS[k]: v
            for k, v in self.img._getexif().items()
            if k in PIL.ExifTags.TAGS 
        }

        self.latPre = self.exif['GPSInfo'][2]
        self.lonPre = self.exif['GPSInfo'][4]

        self.latitude = float(((((self.latPre[0] * 60) + self.latPre[1])* 60 ) + self.latPre[2]) / 60 / 60)
        if self.exif['GPSInfo'][1] == 'S':
            self.latitude *= -1

        self.longitude = float(((((self.lonPre[0] * 60) + self.lonPre[1])* 60 ) + self.lonPre[2]) / 60 / 60)
        if self.exif['GPSInfo'][3] == 'W':
            self.longitude *= -1
        
        self.dateCreated = self.exif["DateTimeOriginal"]
    
    def returnData(self):
        return {"name": os.path.basename(self.imgDir), "lon": self.longitude, "lat": self.latitude, "dateCreated": self.dateCreated}

