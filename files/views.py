from django.shortcuts import render
from .models import * 
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from .models import Filepdf

def homepage(request):
    return render(request,'./dbms.html')

def download_file(request, id):
    files = get_object_or_404(Filepdf, pk=id)
    file_path = files.file.path
    response = FileResponse(open(file_path,'rb'))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = f'attachment; filename="{files.title}.pdf"'
    return response

def PPT(request):
    files = Filepdf.objects.all()
    context = {
        'files' : files[14::]
    }
    return render(request, './ppt.html',context)

def Study(request):
    files = Filepdf.objects.all()
    context = {
        'files' : files[9:13]
    }
    return render(request, './Studymaterial.html',context)

def Practicals(request):
    files = Filepdf.objects.all()
    context = {
        'files' : files[:9]
    }
    return render(request, './Practicals.html',context)

def Module(request):
    files = Filepdf.objects.all()
    context = {
        'files' : files[13::13]
    }
    return render(request, './Modules.html',context)

def trail(request):
    return render(request,'./trial.html')
