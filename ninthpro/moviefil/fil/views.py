from django.urls import reverse_lazy
from django.views.generic import ListView
from django.contrib.auth import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

from .forms import movieform
from .models import movie


# Create your views here.
def demo(request):
    a = movie.objects.all()
    return render(request, 'mov.html', {'aa': a})


def detail(request, id):
    w = movie.objects.get(id=id)

    return render(request, "icon.html", {"ee": w})


def pict(request):
    if request.method == "POST":
        name = request.POST.get('name', )
        year = request.POST.get('year', )
        designation = request.POST.get('designation', )
        image = request.FILES['image']
        q = movie(name=name, year=year, description=designation, image=image)
        q.save()
        return redirect('/')
    return render(request, 'pict.html')


def update(request, id):
    r = movie.objects.get(id=id)
    form = movieform(request.POST or None, request.FILES, instance=r)
    if form.is_valid():
        form.save()
        return redirect('/')
    else:
        form = movieform(instance=r)
    return render(request, 'form1.html', {'bb': r, 'form': form})


def delete(request, id):
    if request.method == 'POST':
        l = movie.objects.get(id=id)
        l.delete()
        return redirect('/')
    return render(request, 'delete.html')


class movielistview(ListView):
    model = movie
    template_name = "mov.html"
    context_object_name = 'aa'


class moviedeatilview(DetailView):
    model = movie
    template_name = "icon.html"
    context_object_name = 'ee'


class movieupdateview(UpdateView):
    model = movie
    template_name = "update.html"
    context_object_name = ''
    fields = ('name', 'year', 'image')

    def get_success_url(self):
        return reverse_lazy('movie:u', kwargs={'pk': self.object.id})
class moviedeleteview(DetailView):
    model = movie
    template_name = 'delete.html'
    success_url=reverse_lazy('u')