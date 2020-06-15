import time
import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (1280, 720)
    camera.start_preview()
    camera.exposure_compensation = 2
    camera.exposure_mode = 'auto'
    camera.image_effect = 'sketch'
    time.sleep(30)
    camera.exif_tags['IFD0.Artist'] = 'Kim'
    camera.exif_tags['IFD0.Copyright'] = 'CopyleftKim'
    camera.capture('foo.jpg')
    camera.stop_preview()
