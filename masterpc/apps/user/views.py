from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from django.views.generic import View, FormView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from .forms import UserRegisterForm, PcForm
from .models import Pc

class Index(View):

    def get(self, request):
        if request.user.is_authenticated:
            pcs = Pc.objects.filter(user = request.user)

            return render(request, 'user/index.html', locals())
        else:
            return render(request, 'user/index.html')
    
    def post(self, request):
        form = PcForm(request.POST)
        if form.is_valid():
            pc = form.save(commit=False)
            pc.user = request.user
            pc.save()
            return HttpResponseRedirect('/')
        else:
            print ("with error")
            return render(request, 'user/index.html', locals())

class PcView(FormView, LoginRequiredMixin):
    model = Pc
    form_class = PcForm
    template_name = 'user/pc_form.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class CreatePc(CreateView, PcView):
    pass

class UpdatePc(UpdateView, PcView):
    pass

class DeletePc(DeleteView):
    model = Pc
    success_url = reverse_lazy('index')
    
# class CreatePc(LoginRequiredMixin, CreateView):
#     model = Pc
#     form_class = PcForm
#     template_name = 'user/pc_form.html'
#     success_url = reverse_lazy('index')

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)


class UserRegister(View):

    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'registration/signup.html', locals())

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user_data = form.save(commit=False)
            user_data.save()
            return render(request, 'registration/register_success.html', locals())
        else:
            return render(request, 'registration/signup.html', locals())

def register_success(request):
    return render(request, 'registration/register_success.html')