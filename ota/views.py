from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index(request):
    return render(request, 'ota/demo.html', {})

def firmware_upload(request):
    if(request.method == 'POST'):
        firmware = ContFirmware()
        firmware.name = request.POST['name']
        firmware.firmware = request.FILES['firmware']
        firmware.comment = request.POST['comment']
        firmware.save()

        return redirect('firmware')

    elif (request.method == 'GET'):
        return render(request, 'ota/firmware.html', {})

        