from django.urls import path
from SURYA.views import *

app_name='SURYA'
urlpatterns=[
    path('SINGAM/',SINGAM,name='SINGAM')
]