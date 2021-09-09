from django.urls.base import reverse_lazy
from .models import Core
from django.shortcuts import render
from django.views.generic import ListView, DetailView , UpdateView, DeleteView,CreateView



class IndexView(ListView):
    model = Core
    template_name = 'core/index.html'
    context_object_name = 'index'

class SingleView(DetailView):
    model = Core
    template_name = 'core/single.html'
    context_object_name = 'post'

class PostView(ListView):
    model = Core
    template_name = 'core/posts.html'
    context_object_name = 'post_list'

class AddView(CreateView):
    model = Core
    # fields = ['name']
    template_name = 'core/add.html'
    fields = '__all__'
    success_url = reverse_lazy('app:post')

class EditView(UpdateView):
    model = Core
    # fields = ['name']
    template_name = 'core/edit.html'
    fields = '__all__'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('app:post')

class Delete(DeleteView):
    model = Core
    # fields = ['name']
    template_name = 'core/confirm_delete.html'

    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('app:post')