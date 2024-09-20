from django.contrib import admin
from django.urls import path
from . import views
 
urlpatterns = [
    path("",views.homepage,name="homepage"),
    path("ppt/",views.PPT,name="ppt"),
    path("StudyMaterial/",views.Study,name="StudyMaterial"),
    path("Modules/",views.Module,name="Modules"),
    path("Practicals/",views.Practicals,name="Modules"),
    path("Anushka/",views.Anushka,name="Anushka"),
    path('download/<int:id>/',views.download_file, name='download_file'),
]