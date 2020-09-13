from rest_framework import routers
from django.urls import path,include
from . import views
router=routers.DefaultRouter()
router.register(r'information/',views.informationviewset)
urlpatterns =[
    path("",views.index,name="home"),
    path('data/',include(router.urls)),
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework')),
    path("login",views.login,name="login"),
]