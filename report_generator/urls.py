from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('instructions', views.instructions, name='instructions'),
    path('upload', views.upload_file, name='upload_file'),
    path('preview', views.preview, name='preview'),
    path('send_email', views.send_email, name='send_email'),
    path('handler404', views.handler404, name='handler404'),
    path('handler500', views.handler500, name='handler500')
]