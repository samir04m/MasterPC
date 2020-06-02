from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from django.views.generic import View, FormView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from .forms import *
from .models import Pc
from apps.pc.models import *

class Index(View):
    def get(self, request):
        if request.user.is_authenticated:
            pcs = Pc.objects.filter(user = request.user)
        
        return render(request, 'user/index.html', locals())

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

class DetailPc(DetailView, LoginRequiredMixin):
    model = Pc
    template_name = 'user/pc_details.html'


def select_component(request, pc_id, name_component, comp_id):
    Model = None
    if name_component == 'CPU': Model = Cpu
    elif name_component == 'GPU': Model = Gpu
    elif name_component == 'Board': Model = Board
    elif name_component == 'RAM': Model = Ram
    elif name_component == 'Storage': Model = Storage
    elif name_component == 'PSU': Model = Psu
    elif name_component == 'Case': Model = Case

    if Model:
        objects = Model.objects.all()

        if comp_id != 0:
            if name_component == 'CPU':
                stores = Store_cpu.objects.filter(cpu__id = comp_id, is_available = 1).order_by('price')
            elif name_component == 'GPU':
                stores = Store_gpu.objects.filter(gpu__id = comp_id, is_available = 1).order_by('price')
            elif name_component == 'Board':
                stores = Store_board.objects.filter(board__id = comp_id, is_available = 1).order_by('price')
            elif name_component == 'RAM':
                stores = Store_ram.objects.filter(ram__id = comp_id, is_available = 1).order_by('price')
            elif name_component == 'Storage':
                stores = Store_storage.objects.filter(storage__id = comp_id, is_available = 1).order_by('price')
            elif name_component == 'PSU':
                stores = Store_psu.objects.filter(psu__id = comp_id, is_available = 1).order_by('price')
            elif name_component == 'Case':
                stores = Store_case.objects.filter(case__id = comp_id, is_available = 1).order_by('price')        
        
        return render(request, 'user/pc_add_component.html', locals())
    else:
        return redirect('detail_pc', pc_id)


def add_component(request, pc_id, name_component, store_id):
    Model = None
    if name_component == 'CPU': Model = Pc_cpu
    elif name_component == 'GPU': Model = Pc_gpu
    elif name_component == 'Board': Model = Pc_board
    elif name_component == 'RAM': Model = Pc_ram
    elif name_component == 'Storage': Model = Pc_storage
    elif name_component == 'PSU': Model = Pc_psu
    elif name_component == 'Case': Model = Pc_case

    if Model:
        if name_component == 'Storage':
            comp = Model(pc_id=pc_id, store_id=store_id)
        else:
            comp = Model.objects.filter(pc_id=pc_id).first()
            if comp:
                comp.store_id = store_id
            else:
                comp = Model(pc_id=pc_id, store_id=store_id)
        comp.save()

    return redirect('detail_pc', pc_id)

def remove_component(request, pc_id, name_component, store_id):
    Model = None
    if name_component == 'Storage': Model = Pc_storage

    if Model:
        comp = Model.objects.filter(pc_id=pc_id, store_id=store_id).first().delete()

    return redirect('detail_pc', pc_id)
    
def change_view(request, pc_id, view):
    pc = Pc.objects.get(id=pc_id)
    if pc:
        pc.view = view
        pc.save()
    return redirect('detail_pc', pc_id)