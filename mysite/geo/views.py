from django.shortcuts import render
from .models import State, City
from django.http import Http404


def state(request, state_id):
    try:
        state_obj = State.objects.get(pk=state_id)
    except State.DoesNotExist:
        raise Http404(f'The state id {state_id} does not exist')
    return render(request, 'geo/states.html', {'state': state_obj})
