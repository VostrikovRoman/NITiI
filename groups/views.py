from django.shortcuts import render, redirect
from .models import Groups, Specialities
from django.views.generic import DetailView, UpdateView, DeleteView
from .forms import GroupsForm



def groups (request):
    s=request.GET.get('search','')
    groups = Groups.objects.filter(name__icontains = s).order_by('name')
    specialities = Specialities.objects.all()
    return render(request, 'groups/groups.html', {'groups':groups, 'specialities':specialities})

def add (request):
    error = ''
    if request.method == 'POST':
        form = GroupsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('groups')
        else:
            error = 'Данные заполнены неверно'
    form = GroupsForm()
    return render(request, 'groups/add.html', {'form': form, 'error':error})

class Group_Page(DetailView):
    model = Groups
    template_name = 'groups/group_page.html'
    context_object_name = 'group'

class Delete(DeleteView):
    model = Groups
    success_url = '/groups/'
    template_name = 'groups/delete.html'

class Update(UpdateView):
    model = Groups
    template_name = 'groups/update.html'
    form_class = GroupsForm
    success_url = '/groups/'

def Search (request):
    s=request.GET['text']
