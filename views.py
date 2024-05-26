from django.shortcuts import render, redirect, get_object_or_404
from .models import PDV, OpeningHours
from .forms import PDVForm, OpeningHoursForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def pdv_dashboard(request):
    pdv_form = PDVForm()
    pdv_list = PDV.objects.all()
    pdv_data = {}

    for pdv in pdv_list:
        pdv_data[pdv] = {
            'pdv_instance': pdv,
            'pdv_form': PDVForm(instance=pdv),
        }

    context = {
        'pdv_data': pdv_data,
        'pdv_form': pdv_form,
    }

    return render(request, 'pdv_management/pdv_dashboard.html', context)

@login_required
def pdv_delete(request, pdv_id):
    pass
    #pdv = get_object_or_404(PDV, id=pdv_id)
    #if request.method == 'POST':
    #    pdv.delete()
    #    messages.success(request, 'PDV eliminato con successo.')
    #else:
    #    messages.error(request, 'Si è verificato un errore. Si prega di correggere il modulo.')
    #return redirect('pdv_management:pdv_dashboard')

@login_required
def pdv_update(request, pdv_id):
    pass
    #pdv = get_object_or_404(PDV, id=pdv_id)
#
    #if request.method == 'POST':
    #    pdv_form = PDVForm(request.POST, instance=pdv)
    #    if pdv_form.is_valid():
    #        pdv_form.save()
    #        messages.success(request, 'PDV aggiornato con successo.')
    #        return redirect('pdv_management:pdv_dashboard')
    #    else:
    #        messages.error(request, 'Si è verificato un errore. Si prega di correggere il modulo.')
    #else:
    #    pdv_form = PDVForm(instance=pdv)
#
    #context = {
    #    'pdv': pdv,
    #    'pdv_form': pdv_form,
    #}
#
    #return render(request, 'pdv_management/pdv_dashboard.html', context)

@login_required
def pdv_add(request):
    pass
    #if request.method == 'POST':
    #    pdv_form = PDVForm(request.POST)
    #    if pdv_form.is_valid():
    #        pdv_form.save()
    #        messages.success(request, 'PDV aggiunto con successo.')
    #        return redirect('pdv_management:pdv_dashboard')
    #    else:
    #        messages.error(request, 'Si è verificato un errore. Si prega di correggere il modulo.')
    #else:
    #    form = PDVForm()
#
    #context = {
    #    'form': form,
    #}
    #return render(request, 'pdv_management/pdv_dashboard.html', context)
    
@login_required
def opening_hours_dashboard(request):
    opening_hours_list = OpeningHours.objects.all()
    opening_hours_data = []

    for opening_hour in opening_hours_list:
        form = OpeningHoursForm(instance=opening_hour)
        opening_hours_data.append({'opening_hour': opening_hour, 'form': form})

    context = {
        'opening_hours_data': opening_hours_data,
    }
    return render(request, 'pdv_management/opening_hours_dashboard.html', context)

@login_required
def opening_hours_add(request):
    if request.method == 'POST':
        form = OpeningHoursForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Orario di apertura aggiunto con successo.')
            return redirect('pdv_management:opening_hours_dashboard')
        else:
            messages.error(request, 'Si è verificato un errore. Si prega di correggere il modulo.')
    else:
        form = OpeningHoursForm()

    context = {
        'opening_hours_form': form,
    }
    return render(request, 'pdv_management/opening_hours_dashboard.html', context)

@login_required
def opening_hours_delete(request, opening_hours_id):
    opening_hours = get_object_or_404(OpeningHours, id=opening_hours_id)

    if request.method == 'POST':
        opening_hours.delete()
        messages.success(request, 'Orario di apertura eliminato con successo.')
    else:
        messages.error(request, 'Si è verificato un errore. Si prega di correggere il modulo.')
    return render(request, 'pdv_management/opening_hours_dashboard.html')

@login_required
def opening_hours_update(request, opening_hours_id):
    opening_hours = get_object_or_404(OpeningHours, id=opening_hours_id)

    if request.method == 'POST':
        form = OpeningHoursForm(request.POST, instance=opening_hours)
        if form.is_valid():
            form.save()
            messages.success(request, 'Orario di apertura aggiornato con successo.')
            return redirect('pdv_management:opening_hours_dashboard')
        else:
            messages.error(request, 'Si è verificato un errore. Si prega di correggere il modulo.')
    else:
        form = OpeningHoursForm(instance=opening_hours)

    context = {
        'opening_hours': opening_hours,
        'form': form,
    }

    return render(request, 'pdv_management/opening_hours_dashboard.html', context)

