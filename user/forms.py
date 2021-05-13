from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import Customer, Manager,User
class CustomerSignUpForm(UserCreationForm):
    name=forms.CharField(required=True)
    age=forms.CharField(required=True)
    class Meta(UserCreationForm.Meta):
        model = User
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        
        user.is_customer = True
        user.save()
        student = Customer.objects.create(user=user)
        return user
class ManagerSignUpForm(UserCreationForm):
    name=forms.CharField(required=True)
    age=forms.CharField(required=True)
  
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        
        user.is_manager = True
        user.save()
        manager = Manager.objects.create(user=user)
        
        manager.save()

        return manager