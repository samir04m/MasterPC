from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, View
from django.contrib.auth.models import User
from .forms import UserRegisterForm

def index(request):
    return render(request, 'user/index.html')


# class UserRegister(CreateView):
#     model = User
#     template_name = 'registration/signup.html'
#     form_class = UserRegisterForm
#     success_url = reverse_lazy('register_success')

class UserRegister(View):

    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'registration/signup.html', locals())

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            print ("Form is validated")
            user_data = form.save(commit=False)
            user_data.save()
            return render(request, 'registration/register_success.html', locals())
        else:
            print ("with error")
            return render(request, 'registration/signup.html', locals())

def register_success(request):
    return render(request, 'registration/register_success.html')