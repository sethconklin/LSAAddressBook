from django.shortcuts import render, redirect
from .models import Member

# Create your views here.

def index(request):
    members = Member.objects.all()
    context = {'members': members}
    return render(request, 'contacts/index.html', context)

def create(request):
    member = Member(first_name=request.POST['first_name'], last_name=request.POST['last_name'],
                    phone_number=request.POST['phone_number'], email_address=request.POST['email_address'],
                    street_address=request.POST['street_address'])
    member.save()
    return redirect('/')

def edit(request, id):
    members = Member.objects.get(id=id)
    context = {'members': members}
    return render(request, 'contacts/edit.html', context)

def update(request, id):
    member = Member.objects.get(id=id)
    member.first_name = request.POST['first_name']
    member.last_name = request.POST['last_name']
    member.phone_number = request.POST['phone_number']
    member.email_address = request.POST['email_address']
    member.street_address = request.POST['street_address']
    member.save()
    return redirect('/contacts/')

def delete(request, id):
    member = Member.objects.get(id=id)
    member.delete()
    return redirect('/contacts/')