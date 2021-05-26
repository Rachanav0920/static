from django.urls import path
from app1 import views
app_name="app1"

urlpatterns = [
    path('index/',views.index,name="index"),
    path('demo1/',views.demo1,name="demo1"),
    path('<a>/<b>',views.demo2,name="demo2"),
    path('demo3',views.demo3,name="demo3"),
    path('',views.demo5,name="demo5"),
    path('sample3/',views.sample3,name='sample3'),
]
