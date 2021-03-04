from django.shortcuts import render
from service.models import Service


def service_page(request):
    services = Service.objects.all()
    return render(request, 'service/service_page.html', {'services': services})
