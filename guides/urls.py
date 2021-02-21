
from django.urls import path,include
from . import views
from rest_framework import routers
from .api import GuidesViewAPI

router = routers.DefaultRouter()                     
router.register(r'guide', GuidesViewAPI, 'guide')
# router.register('api/guide',GuidesViewAPI, 'guide')


urlpatterns = [
    path('api/', include(router.urls)),
    # path('', GuidesView),
]
    
