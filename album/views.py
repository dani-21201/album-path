from django.shortcuts import render
from django.http import HttpResponse
from album.models import Category, Photo
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, CreateView, DeleteView


# Create your views here.

def first_view(request):
    return render(request,'base.html')

def category(request):
	category_list = Category.objects.all()
	context = {'object_list': category_list,'otra':'esta es la información'}
	return render(request, 'album/category.html', context)

def category_detail(request, category_id):
	category = Category.objects.get(id=category_id)
	context = {'object': category}
	return render(request, 'album/category_detail.html', context)

class PhotoListView(ListView):
	model = Photo

class PhotoDetailView(DetailView):
	model = Photo



class PhotoUpdate(UpdateView):
	model = Photo
	fields = '__all__'    
class PhotoCreate(CreateView):
	model = Photo
	fields = '__all__'
class PhotoDelete(DeleteView):
    model = Photo
    success_url = reverse_lazy('photo-list')	

class CategoryUpdate(UpdateView):
	model = Category
	fields = '__all__'    
class CategoryCreate(CreateView):
	model = Category
	fields = '__all__'
class CategoryDelete(DeleteView):
    model = Category
    success_url = reverse_lazy('category-list')	