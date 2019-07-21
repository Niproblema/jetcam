from .camera import Camera
import atexit
import cv2
import numpy as np
import threading
import traitlets


class RTSPCamera(Camera):
    
    capture_fps = traitlets.Integer(default_value=30)
    capture_width = traitlets.Integer(default_value=640)
    capture_height = traitlets.Integer(default_value=480)   
    capture_source = traitlets.Any(default_value='rtsp://localhost:8080')
    
    def __init__(self, *args, **kwargs):
        super(RTSPCamera, self).__init__(*args, **kwargs)
        try:
            print(self._gst_str())
            self.cap = cv2.VideoCapture(self._gst_str(), cv2.CAP_GSTREAMER)

            re , image = self.cap.read()
            
            if not re:
                raise RuntimeError('Could not read image from camera.')
            
        except:
            raise RuntimeError(
                'Could not initialize camera.  Please see error trace.')

        atexit.register(self.cap.release)
                
    def _gst_str(self):
        #return 'rtspsrc location={} latency=0 ! decodebin ! videorate ! videoscale ! video/x-raw,width={},height={},framerate={}/1 ! appsink sync=false'.format(self.capture_source, self.capture_width, self.capture_height, self.capture_fps)
        return 'rtspsrc location={} latency=0 ! rtph264depay ! h264parse ! avdec_h264 ! videoconvert ! appsink'.format(self.capture_source)
    def _read(self):
        re, image = self.cap.read()
        if re:
            image_resized = cv2.resize(image,(int(self.width),int(self.height)))
            return image_resized
        else:
            raise RuntimeError('Could not read image from camera')
