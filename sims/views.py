from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from sims.roll import risk_rolls_battle_to_completion as battle_simulation
from sims.models import Simulation

def home_page(request):
  if request.method == 'POST':
    starting_attacking_armies = int(request.POST.get('attacking_armies', 1))
    starting_defending_armies = int(request.POST.get('defending_armies', 1))
    ending_attacking_armies, ending_defending_armies = battle_simulation(starting_attacking_armies, starting_defending_armies)
    if ending_attacking_armies > ending_defending_armies:
      result_statement = "Attackers win"
    else:
      result_statement = "Defenders win"
    # save simulation to database
    sim = Simulation(
      attacking_armies_starting=starting_attacking_armies,
      defending_armies_starting=starting_defending_armies,
      attacking_armies_remaining=ending_attacking_armies,
      defending_armies_remaining=ending_defending_armies,
      result_statement=result_statement,
      timestamp=timezone.now(),
    )
    sim.save()

    # get history (most recent first)
    history = Simulation.objects.order_by('-timestamp')

    return render(request, 'home.html', {
      'result_statement': result_statement,
      'starting_attacking_armies': starting_attacking_armies,
      'starting_defending_armies': starting_defending_armies,
      'ending_attacking_armies': ending_attacking_armies,
      'ending_defending_armies': ending_defending_armies,
      'history': history,
    })
  return render(request, 'home.html')
