from django.urls import path
from BALAYYA.views import *

app_name='BALAYYA'
urlpatterns=[
    path('BALA/',BALA,name='BALA')
]