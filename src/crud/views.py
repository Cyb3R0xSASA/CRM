from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateUserForm, LoginFrom, RecordsForm
from django.contrib.auth import authenticate, login as auth_login, logout as logout_auth
from django.contrib.auth.decorators import login_required
from .models import Records
from django.db.models import Q
import logging
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def register(request):
    # This condition work when user send the form 
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save() # Add form values to the User model
            return redirect('login')
    # This work when user open register page to send empty form in this page
    else:
        form = CreateUserForm() # if the request not post send the form to fill it
    context = {'form': form}

    return render(request, 'pages/register.html', context=context)

def login(request):
    if request.method == 'POST':
        form = LoginFrom(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')  # Get the value of the username input
            password = request.POST.get('password')  # Get the value of the password input
            user = authenticate(request, username=username, password=password)  # Check the values with the database

            if user is not None:  # If the check is valid
                auth_login(request, user)  # Correctly login the user using Django's built-in login
                return redirect('dashboard')
    else:
        form = LoginFrom()
    return render(request, 'pages/login.html', context={'form': form})

@login_required(login_url='login')
def dashboard(request):
    context = {'records': Records.objects.all()}
    return render(request, 'pages/dashboard.html', context)

@login_required(login_url='login')
def record(request):
    if request.method == 'POST':
        form = RecordsForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, 'Record Created Successfully')
            return redirect('dashboard')
    else:
        form = RecordsForm()
    context = {'form': form}
    return render(request, 'pages/records.html', context)

@login_required(login_url='login')
def view_record(request, record_id):
    context = {
        'record': get_object_or_404(Records, id=record_id),
    }
    return render(request, 'pages/record.html', context)

@login_required(login_url='login')
def edit_record(request, record_id):
    record = get_object_or_404(Records, id=record_id)
    if request.method == 'POST':
        form = form = RecordsForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, 'Success Update')
            return redirect('record', record_id=record_id)
    else: 
        form = RecordsForm(instance=record)
    return render(request, 'pages/edit_record.html', {'form': form})

@login_required(login_url='login')
def delete_record(request, record_id):
    record = get_object_or_404(Records, id=record_id)
    record.delete()
    return redirect('dashboard')

@login_required(login_url='login')
def search(request):
    query = request.GET.get('search')
    result = []
    try:
        if query:
            result = Records.objects.filter(
                Q(first_name__icontains=query) | Q(id__icontains=query)
                )
    except Exception as e:
        logging.getLogger(__name__).error(f'Error during search: {e}')
    return render(request, 'pages/dashboard.html', context={'records': result, 'query': query})


def logout(request):
    logout_auth(request)
    return redirect('login')

def custom_page_404(request, exception):
    return render(request, 'pages/404.html', status=404)