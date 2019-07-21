from jetcam.rtsp_camera import RTSPCamera
camera = RTSPCamera(width=224, height=224, capture_width=640, capture_height=480,capture_source='rtsp://10.42.0.161:5540/ch0')
#from jetcam.usb_camera import USBCamera
#camera = USBCamera(width=224, height=224, capture_width=640, capture_height=480,capture_device=0)