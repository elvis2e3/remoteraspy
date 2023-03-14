from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
import os
os.environ['DISPLAY'] = ":0.0"
import pyautogui as remote
import time
from PIL import Image
from remoteraspy.settings import BASE_DIR

class RemoteViewSet(APIView):
    permission_classes = ([])

   # @staticmethod
    def get(self, request):
        width, height = remote.size()
        return Response(
            {
                'width': width,
                'height': height
            }
        )

    def move(self, width, height):
        remote.moveTo(width, height)

    def sleep(self, second):
        time.sleep(second)

    def click(self):
        remote.click()

    def doubleClick(self):
        remote.doubleClick()

@api_view(['GET',])
def screenshot(request):
    name = 'screenshot_%d.png' % time.time_ns()
    try:
        for file in os.scandir('static/'):
            os.remove(file.path)
    except:
        pass
    remote.screenshot('static/' + name)
    im = Image.open(str(BASE_DIR) + '/static/' + name)
    im=im.rotate(90, expand=True)
    im.save(str(BASE_DIR) + '/static/' + name)
    return Response({'file_name': name})

@api_view(['GET',])
def set_point(request, width, height):
    remote.moveTo(width, height)
    return Response({'width': width, 'height': height})

@api_view(['GET'])
def click(request):
    remote.click()
    return Response({'status': True})

@api_view(['GET'])
def double_click(request):
    remote.doubleClick()
    return Response({'status': True})

@api_view(['GET'])
def scroll_up(request, move_size):
    remote.scroll(move_size)
    return Response({'status': True})

@api_view(['GET'])
def scroll_down(request, move_size):
    remote.scroll(move_size * -1)
    return Response({'status': True})

