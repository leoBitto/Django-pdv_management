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

    return render(request, 'pdv_management/dashboard/pdv_dashboard.html', context)

@login_required
def pdv_delete(request, pdv_id):
    pdv = get_object_or_404(PDV, id=pdv_id)
    if request.method == 'POST':
        pdv.delete()
        messages.success(request, 'PDV eliminato con successo.')
    else:
        messages.error(request, 'Si è verificato un errore. Si prega di riprovare.')
    return redirect('pdv_management:pdv_dashboard')

@login_required
def pdv_update(request, pdv_id):
   
    pdv = get_object_or_404(PDV, id=pdv_id)

    if request.method == 'POST':
        pdv_form = PDVForm(request.POST, instance=pdv)
        if pdv_form.is_valid():
            pdv_form.save()
            messages.success(request, 'PDV aggiornato con successo.')
            return redirect('pdv_management:pdv_dashboard')
        else:
            for field, errors in pdv_form.errors.items():
                for error in errors:
                    messages.error(request, f"Errore nel campo {field}: {error}")
            return redirect('pdv_management:pdv_dashboard')
    else:
        return redirect('pdv_management:pdv_dashboard')

@login_required
def pdv_add(request):
    if request.method == 'POST':
        pdv_form = PDVForm(request.POST)

        if pdv_form.is_valid():
            pdv_form.save()
            messages.success(request, 'PDV aggiunto con successo.')
            return redirect('pdv_management:pdv_dashboard')
        else:
            for field, errors in pdv_form.errors.items():
                for error in errors:
                    messages.error(request, f"Errore nel campo {field}: {error}")
            return redirect('pdv_management:pdv_dashboard')
    else:
        return redirect('pdv_management:pdv_dashboard')
    
@login_required
def opening_hours_dashboard(request):

    opening_hours_list = OpeningHours.objects.all()

    # Raggruppa per pdv
    grouped_opening_hours = {}
    for opening_hours in opening_hours_list:
        pdv = opening_hours.pdv
        if pdv not in grouped_opening_hours:
            grouped_opening_hours[pdv] = []
        grouped_opening_hours[pdv].append({
            'opening_hours': opening_hours,
            'opening_hours_form': OpeningHoursForm(instance=opening_hours)
        })

    context = {
        'opening_hours_data': grouped_opening_hours,
        'opening_hours_form': OpeningHoursForm(),
    }
    return render(request, 'pdv_management/dashboard/opening_hours_dashboard.html', context)

@login_required
def opening_hours_add(request):
    if request.method == 'POST':
        form = OpeningHoursForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Orario di apertura aggiunto con successo.')
            return redirect('pdv_management:opening_hours_dashboard')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Errore nel campo {field}: {error}")
            return redirect('pdv_management:opening_hours_dashboard')
    else:
        return redirect('pdv_management:opening_hours_dashboard')

@login_required
def opening_hours_delete(request, opening_hours_id):
    opening_hour = get_object_or_404(OpeningHours, id=opening_hours_id)
    if request.method == 'POST':
        opening_hour.delete()
        messages.success(request, 'Orario di apertura eliminato con successo.')
    else:
        messages.error(request, 'Si è verificato un errore. Si prega di correggere il modulo.')
    return redirect('pdv_management:opening_hours_dashboard')

@login_required
def opening_hours_update(request, opening_hours_id):
    opening_hours = get_object_or_404(OpeningHours, id=opening_hours_id)
    if request.method == 'POST':
        oh_form = OpeningHoursForm(request.POST, instance=opening_hours)
        if oh_form.is_valid():
            oh_form.save()
            messages.success(request, 'Orario di apertura aggiornato con successo.')
            return redirect('pdv_management:opening_hours_dashboard')
        else:
            for field, errors in oh_form.errors.items():
                for error in errors:
                    messages.error(request, f"Errore nel campo {field}: {error}")
            return redirect('pdv_management:opening_hours_dashboard')
    else:
        return redirect('pdv_management:opening_hours_dashboard')   

