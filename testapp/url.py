from django.urls import path,include
from . import views
urlpatterns=[
    path('',views.home),
    path('about/',views.about),
    path('get-in-touch/',views.get_in_touch)
]