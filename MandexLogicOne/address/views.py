from django.shortcuts import render
from .models import Address

def address_detail(request, address_id):
    address = Address.objects.get(id=address_id)
    return render(request, 'address/address_detail.html', {'address': address})
