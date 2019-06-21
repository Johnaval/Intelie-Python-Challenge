from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Schema, Entry

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class SchemaForm(forms.ModelForm):
    attribute = forms.CharField(max_length=200)
    cardinality = forms.CharField(max_length=4)
    class Meta:
        model = Schema
        exclude = ()

class EntryForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(EntryForm, self).__init__(*args, **kwargs)
        for attribute in Schema.objects.order_by().values_list('attribute').distinct():
            self.fields[attribute[0]] = forms.CharField(max_length=200, label=attribute[0], required=False)