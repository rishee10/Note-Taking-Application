from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from NOTE import settings
from .forms import ContactForm, ItemForm, LoginForm
from .models import Contact 



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})





def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('index')  
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
# Create your views here.

def register(request):
    return redirect('signup')






def object_edit(request, item_id):
    item = Contact.objects.get(pk=item_id)
    form = ItemForm(request.POST, instance=item)
    if form.is_valid():
        form.save()
        return redirect('index')
    
    

    return render(request, 'index.html', {'item': item})

def index1(request,item_id):
    return redirect('index')




@login_required
def index(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('index')
    else:
        form = ItemForm()
    return render(request, 'index.html', {'form': form})
    
    


def about(request, item_id):
    item = Contact.objects.get(pk=item_id)
    return render(request, 'about.html', {'item': item})






@login_required
def about1(request):
    items = Contact.objects.filter(user=request.user)
    return render(request, 'about1.html', {'items': items})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']

            recipients = [settings.CONTACT_EMAIL]  # Add your recipient email(s) here

            send_mail(subject, message, sender, recipients)

            # Optionally, you can redirect to a "Thank You" page after successful submission
            return HttpResponseRedirect('/thank-you/')
    else:
        form = ContactForm()

    return render(request, 'contact/contact_form.html', {'form': form})
    



def delete_object(request, item_id):
    item = get_object_or_404(Contact, pk=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('about1')
    return redirect('about1')

def stosaved(request, item_id):
    return redirect('about1')





def edit(request, item_id):
    item=Contact.objects.get(pk=item_id)
    return render(request, "edit.html", {'item':item})


def seetoabout1(request):
    return redirect('about1')

def seetoindex(request):
    return redirect('index')


