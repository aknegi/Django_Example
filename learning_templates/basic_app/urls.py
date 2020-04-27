from django.contrib import admin
from django.urls import path
from basic_app import views
#template tagging

app_name='basic_app' # ye basic app wha html ki file me same hona chahiye
# wha html ki file me dictionary me same name hona chahiye

urlpatterns=[

    path('other/',views.other,name='other'),
    path('relative/',views.relative,name='relative'),
]
