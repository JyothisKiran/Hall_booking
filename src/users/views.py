from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login
from .forms import CustomUserCreationForm

class UserLoginView(LoginView):
    redirect_authenticated_user = True
    fields = '__all__'
    template_name = 'login.html'

    def get_success_url(self) :
        return reverse_lazy('hallbooking')
    

class UserRegisterView(FormView):
    template_name = 'register.html'
    form_class = CustomUserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('hallbooking')

    def form_valid(self, form):
        user = form.save()
        if self.request.method == "POST":
            if user is not None:
                login(self.request, user)
        return super(UserRegisterView,self).form_valid(form)
    
    def get(self,*args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect('hallbooking')
        return super(UserRegisterView,self).get(*args,**kwargs)


   