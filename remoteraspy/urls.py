from django.contrib import admin
from django.urls import path, include
from remoteraspy.viewsets import RemoteViewSet, screenshot, set_point, click, double_click, scroll_up, scroll_down
from django.conf.urls.static import static
from remoteraspy.settings import MEDIA_URL, MEDIA_ROOT

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('api-auth/', include('rest_framework.urls')),
    path('', RemoteViewSet.as_view()),
    path('screenshot/', screenshot),
    path('set_point/<int:width>/<int:height>/', set_point),
    path('click', click),
    path('double_click', double_click),
    path('scroll/up/<int:move_size>/', scroll_up),
    path('scroll/down/<int:move_size>/', scroll_down)
] + static(MEDIA_URL, document_root=MEDIA_ROOT)

