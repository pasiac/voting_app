from django.contrib import admin
from django.urls import path, include

from voting.views import OptionViewSet, PollViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'options', OptionViewSet)
router.register(r'poll', PollViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
