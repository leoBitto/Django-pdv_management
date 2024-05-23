from django.shortcuts import render, redirect, get_object_or_404
from .models import PDV
from .forms import PDVForm

def pdv_manage(request):
    #pdv_list = PDV.objects.all()
    #if request.method == 'POST':
    #    form = PDVForm(request.POST)
    #    if form.is_valid():
    #        form.save()
    #        return redirect('pdv_management:pdv_manage')
    #else:
    #    form = PDVForm()
    #return render(request, 'pdv_management/pdv_manage.html', {'pdv_list': pdv_list, 'form': form})
    pass

def pdv_delete(request, pk):
    #pdv = get_object_or_404(PDV, pk=pk)
    #if request.method == 'POST':
    #    pdv.delete()
    #    return redirect('pdv_management:pdv_manage')
    #return render(request, 'pdv_management/pdv_delete.html', {'pdv': pdv})
    pass

def pdv_create(request):
    #if request.method == 'POST':
    #    form = PDVForm(request.POST)
    #    if form.is_valid():
    #        form.save()
    #        return redirect('pdv_management:pdv_manage')
    #else:
    #    form = PDVForm()
    #return render(request, 'pdv_management/pdv_create.html', {'form': form})
    pass

def pdv_update(request, pk):
    #pdv = get_object_or_404(PDV, pk=pk)
    #if request.method == 'POST':
    #    form = PDVForm(request.POST, instance=pdv)
    #    if form.is_valid():
    #        form.save()
    #        return redirect('pdv_management:pdv_manage')
    #else:
    #    form = PDVForm(instance=pdv)
    #return render(request, 'pdv_management/pdv_update.html', {'form': form, 'pdv': pdv})
    pass
