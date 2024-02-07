from django.shortcuts import render
from .models import Deliver

def deliver_list(request):
    delivers = Deliver.objects.all()
    return render(request, 'delivers/deliver_list.html', {'delivers': delivers})


def deliver_detail(request, deliver_id):
    deliver = Deliver.objects.get(id=deliver_id)
    return render(request, 'delivers/deliver_detail.html', {'deliver': deliver})
