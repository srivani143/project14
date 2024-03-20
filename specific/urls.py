from .views import *
from django.urls import path

app_name='hello'

urlpatterns=[
    path=('specific1/',specific1),
    path=('specific2/',specific2),
]