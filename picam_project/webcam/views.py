from django.shortcuts import render

# Create your views here.
import io
from django.utils import timezone
try:
    from picamera import PiCamera
except ImportError:
    PiCamera = None
    import requests

from PIL import Image
from .models import CameraImage

# TODO: Not sure if this is the best way to do this... 
# 
# Used this to guide me: 
#   - https://picamera.readthedocs.io/en/release-1.13/recipes2.html
#   - https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/
#
# I'm not sure if this is the best way to do this...
# or if it works at all as I couldn't install picamera on the mac
# Need to get back to linux soon... 🙈

def capture_image():
    if PiCamera:
        # Existing PiCamera code
        stream = io.BytesIO()
        with PiCamera() as camera:
            camera.start_preview()
            camera.capture(stream, format='jpeg')
        stream.seek(0)
        image = Image.open(stream)
    else:
        # Fetch a dummy image of birds from the internet
        response = requests.get('https://picsum.photos/400/300?category=birds')
        image = Image.open(io.BytesIO(response.content))
    
    return image


def index(request):
    image = capture_image()
    img_io = io.BytesIO()
    image.save(img_io, format='JPEG')
    img_file = CameraImage()
    img_file.image.save(f'image_{timezone.now().strftime("%Y%m%d_%H%M%S")}.jpg', img_io)
    img_file.save()

    latest_image = CameraImage.objects.latest('timestamp')
    return render(request, 'webcam/index.html', {'image': latest_image})
