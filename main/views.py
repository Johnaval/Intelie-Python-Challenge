from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Schema, Entry
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import SchemaForm, EntryForm, NewUserForm

# Create your views here.
def homepage(request):
    if request.user.is_authenticated:
        entity_list = [value[0] for value in Entry.objects.order_by().values_list('entity').distinct()]
        return render(request, template_name = "main/home_authenticated.html",
                    context={'entities': entity_list, "entries": Entry.objects.all()})
    else:
        return render(request, template_name='main/home_not_authenticated.html')

def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'New account created: {username}')
            login(request, user)
            return redirect('main:homepage')
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")
    form = NewUserForm
    return render(request, "main/register.html", context={"form":form})

def logout_request(request):
    logout(request)
    messages.info(request, 'Logged out successfully')
    return redirect('main:homepage')

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'You are logged in as {username}')
                return redirect('main:homepage')
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password')
    form = AuthenticationForm()
    return render(request, 'main/login.html', {'form':form})

def modify_schema(request):
    if request.method == 'POST':
        attribute = request.POST.get('attribute')
        cardinality = request.POST.get('cardinality')
        attribute_list = [att['attribute'] for att in Schema.objects.all().values('attribute')]
        if attribute != "":
            if attribute not in attribute_list:
                schema = Schema(attribute=attribute, cardinality=cardinality)
                schema.save()
                messages.info(request, 'Schema modified successfully')
                return redirect('main:homepage')
            else:
                messages.error(request, 'This attribute already exists')
        else:
            messages.error(request, 'Invalid value')
    return render(request, 'main/modify_schema.html')

def create_entity(request):
    if request.method == 'POST':
        entity_list = [value[0] for value in Entry.objects.order_by().values_list('entity').distinct()]
        entity = entity_list[-1] + 1 if len(entity_list) > 0 else 1
        form = EntryForm(request.POST)
        for field in form:
            value = request.POST.get(field.label)
            if value != '':
                entry = Entry(entity=entity, attribute=field.label, value=value, validation=True)
                entry.save()
        messages.info(request, 'Entity created successfully')  
        return redirect('main:homepage')
    form = EntryForm()
    return render(request, 'main/create_entity.html', {'form':form})

def modify_entity(request):
    if request.method == 'POST':
        entity_id = request.POST.get('entity_id')
        form = EntryForm(request.POST)
        for field in form:
            value = request.POST.get(field.label)
            if value != '':
                for schema in Schema.objects.all():
                    if schema.attribute == field.label and schema.cardinality == 'one':
                        for entity in Entry.objects.filter(entity=entity_id, attribute=field.label):
                            entity.validation = False
                            entity.save()
                entry = Entry(entity=entity_id, attribute=field.label, value=value, validation=True)
                entry.save()
        messages.info(request, 'Entity modified successfully') 
        return redirect('main:homepage')
    entity_id = request.GET.get('entity_id')
    form = EntryForm()   
    return render(request, 'main/modify_entity.html', {'entity_id':entity_id, 'form':form})

def exclude_entity(request):
    if request.user.is_superuser:
        Entry.objects.filter(entity=request.GET.get('entity_id')).delete()
    else:
        messages.error(request, "You can't do that")
        messages.error(request, "Ask a superuser to give you permission")
    return redirect('main:homepage')

def entity_history(request):
    entity_id = request.GET.get('entity_id')
    return render(request, 'main/entity_history.html', {'entity_id':entity_id, 'entries':Entry.objects.filter(entity=entity_id)})
