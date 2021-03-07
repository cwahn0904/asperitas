from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import *

from django_file_md5 import calculate_md5

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

def get_latest_firmware(request):
    latest_firmware = ContFirmware.objects.latest('datetime')
    md5 = calculate_md5(latest_firmware.firmware)
    base_url =  "{0}://{1}".format(request.scheme, request.get_host())
    url = base_url + latest_firmware.firmware.url
    return JsonResponse({
        'name': latest_firmware.name,
        'md5': md5,
        'url': url,
    })

        