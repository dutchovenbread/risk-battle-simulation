from django.http import HttpResponse
from django.shortcuts import render
from sims.roll import risk_rolls_battle_to_completion as battle_simulation

def home_page(request):
  if request.method == 'POST':
    starting_attacking_armies = int(request.POST.get('attacking_armies', 1))
    starting_defending_armies = int(request.POST.get('defending_armies', 1))
    ending_attacking_armies, ending_defending_armies = battle_simulation(starting_attacking_armies, starting_defending_armies)
    if ending_attacking_armies > ending_defending_armies:
      result_statement = "Attackers win"
    else:
      result_statement = "Defenders win"
    return render(request, 'home.html', {
      'result_statement': result_statement,
      'starting_attacking_armies': starting_attacking_armies,
      'starting_defending_armies': starting_defending_armies,
      'ending_attacking_armies': ending_attacking_armies,
      'ending_defending_armies': ending_defending_armies,
    })
  return render(request, 'home.html')
