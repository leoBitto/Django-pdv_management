from django.views import View
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import PDV, OpeningHours
from .forms import PDVForm, OpeningHoursForm

class PDVDashboardView(LoginRequiredMixin, View):
    template_name = 'pdv_management/dashboard/pdv_dashboard.html'

    def get(self, request, *args, **kwargs):
        """
        Gestisce le richieste GET per visualizzare la dashboard dei PDV.

        Se un ID di PDV è passato come parametro nella query string, mostra i dettagli del PDV
        selezionato insieme ai form per la modifica e la gestione degli orari di apertura.
        Altrimenti, mostra solo l'elenco dei PDV e il form per aggiungere un nuovo PDV.

        Args:
            request: L'oggetto HttpRequest.

        Returns:
            HttpResponse: La risposta renderizzata con il template della dashboard.
        """
        pdv_id = request.GET.get('pdv_id')
        selected_pdv = None
        opening_hours_forms = []

        pdv_form = PDVForm()
        opening_hours_form = OpeningHoursForm()
        
        # Ottieni tutti i PDV
        pdv_list = PDV.objects.all()
        pdv_data = {}

        if pdv_id:
            selected_pdv = get_object_or_404(PDV, id=pdv_id)
            # Ottieni le ore di apertura per il PDV selezionato
            opening_hours_list = selected_pdv.opening_hours.all()
            opening_hours_forms = [OpeningHoursForm(instance=oh) for oh in opening_hours_list]
            # Passa i moduli degli orari di apertura e il PDV selezionato
            context = {
                'pdv_form': PDVForm(instance=selected_pdv),
                'selected_pdv': selected_pdv,
                'opening_hours_forms': opening_hours_forms,
                'opening_hours_form': opening_hours_form,
                'pdv_data': pdv_list
            }
        else:
            # Passa solo i PDV senza dettagli specifici
            context = {
                'pdv_form': pdv_form,
                'pdv_data': pdv_list,
                'opening_hours_form': opening_hours_form
            }
        
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        """
        Gestisce le richieste POST per aggiungere, aggiornare o eliminare PDV e orari di apertura.

        Gestisce i moduli per:
        - Aggiungere un nuovo PDV.
        - Aggiornare un PDV esistente.
        - Eliminare un PDV.
        - Aggiungere orari di apertura a un PDV selezionato.
        - Aggiornare gli orari di apertura di un PDV.
        - Eliminare gli orari di apertura di un PDV.

        Args:
            request: L'oggetto HttpRequest.

        Returns:
            HttpResponseRedirect: Reindirizza alla pagina della dashboard dei PDV.
        """
        if 'add_pdv' in request.POST:
            pdv_form = PDVForm(request.POST)
            if pdv_form.is_valid():
                pdv = pdv_form.save()
                messages.success(request, 'PDV aggiunto con successo.')
                return redirect('pdv_management:pdv_dashboard')
            else:
                for field, errors in pdv_form.errors.items():
                    for error in errors:
                        messages.error(request, f"Errore nel campo '{field}': {error}")

        elif 'update_pdv' in request.POST:
            pdv_id = request.POST.get('pdv_id')
            selected_pdv = get_object_or_404(PDV, id=pdv_id)
            pdv_form = PDVForm(request.POST, instance=selected_pdv)
            if pdv_form.is_valid():
                pdv_form.save()
                messages.success(request, 'PDV aggiornato con successo!')
            else:
                for field, errors in pdv_form.errors.items():
                    for error in errors:
                        messages.error(request, f"Errore nel campo '{field}': {error}")

        elif 'delete_pdv' in request.POST:
            pdv_id = request.POST.get('pdv_id')
            selected_pdv = get_object_or_404(PDV, id=pdv_id)
            selected_pdv.delete()
            messages.success(request, 'PDV eliminato con successo.')

        elif 'add_opening_hours' in request.POST:
            pdv_id = request.POST.get('pdv_id')
            selected_pdv = get_object_or_404(PDV, id=pdv_id)
            opening_hours_form = OpeningHoursForm(request.POST)
            if opening_hours_form.is_valid():
                new_opening_hours = opening_hours_form.save(commit=False)
                new_opening_hours.pdv = selected_pdv
                new_opening_hours.save()
                messages.success(request, 'Orario di apertura aggiunto con successo.')
            else:
                for field, errors in opening_hours_form.errors.items():
                    for error in errors:
                        messages.error(request, f"Errore nel campo '{field}': {error}")

        elif 'update_opening_hours' in request.POST:
            opening_hours_id = request.POST.get('opening_hours_id')
            opening_hours = get_object_or_404(OpeningHours, id=opening_hours_id)
            opening_hours_form = OpeningHoursForm(request.POST, instance=opening_hours)
            if opening_hours_form.is_valid():
                opening_hours_form.save()
                messages.success(request, 'Orario di apertura aggiornato con successo!')
            else:
                for field, errors in opening_hours_form.errors.items():
                    for error in errors:
                        messages.error(request, f"Errore nel campo '{field}': {error}")

        elif 'delete_opening_hours' in request.POST:
            opening_hours_id = request.POST.get('opening_hours_id')
            opening_hours = get_object_or_404(OpeningHours, id=opening_hours_id)
            opening_hours.delete()
            messages.success(request, 'Orario di apertura eliminato con successo.')

        return redirect('pdv_management:pdv_dashboard')
