from django.shortcuts import render
from django.shortcuts import redirect
from .models import Customer,Manager,User
from django.views.generic import CreateView
from .forms import CustomerSignUpForm,ManagerSignUpForm
# Create your views here.
def index(request):
    return render(request,'index.html')
class CustomerSignUpView(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = 'signup.html'
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'customer'
        return super().get_context_data(**kwargs)
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')
class ManagerSignUpView(CreateView):
    model = User
    form_class = ManagerSignUpForm
    template_name = 'signup.html'
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'manager'
        return super().get_context_data(**kwargs)
    def form_valid(self, form):
        user = form.save()
        #login(self.request, user)
        return redirect('index')

                
                
