import random

def roll_die():
  return(random.randint(1, 6),)

def roll_multiple_dice(num_dice):
  return [roll_die()[0] for _ in range(num_dice)]

def risk_rolls(attacker_armies, defender_armies):
  attacker_dice = min(3, attacker_armies - 1)
  defender_dice = min(2, defender_armies)
  attacker_rolls = roll_multiple_dice(attacker_dice)
  defender_rolls = roll_multiple_dice(defender_dice)
  attacker_rolls.sort(reverse=True)
  defender_rolls.sort(reverse=True)
  comparisons = min(len(attacker_rolls), len(defender_rolls))
  attacker_losses = 0
  defender_losses = 0
  for i in range(comparisons):
    if attacker_rolls[i] > defender_rolls[i]:
      defender_losses += 1
    else:
      attacker_losses += 1
  return attacker_losses, defender_losses

def risk_rolls_battle_to_completion(attacker_armies, defender_armies):
  while attacker_armies > 1 and defender_armies > 0:
    attacker_losses, defender_losses = risk_rolls(attacker_armies, defender_armies)
    attacker_armies -= attacker_losses
    defender_armies -= defender_losses
  return attacker_armies, defender_armies

def risk_attack_successive_countries(attacker_armies, defender_armies_list):
  pass
  # assert defender_armies_list[0] == 0
  # result_attacker_armies_by_country = []
  # result_defender_armies_by_country = []
  # for index, defender_armies in enumerate(defender_armies_list):
  #   print(f'Index: {index}, Attacker armies: {attacker_armies}, Defender armies: {defender_armies}')
  #   if index == 0:
  #     print(f'  First country, no battle')
  #     # there will never be a defender army in the first country
  #     result_defender_armies_by_country.append(0)
  #   else:
  #     print(f'  Country index {index -1} with attacking armies {attacker_armies} attacking country index {index} with defending armies {defender_armies}')
  #     # if there is one attacker army left, stop attacking
  #     if attacker_armies == 1:
  #       print(f'  Only one attacker army left, stopping attack')
  #       # put the last attacker army in the current country
  #       result_attacker_armies_by_country.append(1)
  #       assert len(result_attacker_armies_by_country) == index 
  #       # pad the rest of the attacker armies with 0s
  #       result_attacker_armies_by_country.extend([0] * (len(defender_armies_list) - index))
  #       assert len(result_attacker_armies_by_country) == len(defender_armies_list)
  #       # put the remaining defender armies in the current country
  #       result_defender_armies_by_country.append(defender_armies)
  #       assert len(result_defender_armies_by_country) == index + 1
  #       # pad the rest of the defender armies as is
  #       result_defender_armies_by_country.extend(defender_armies_list[index+1:])
  #       assert len(result_defender_armies_by_country) == len(defender_armies_list)
  #       print(f'  Result attacker armies by country: {result_attacker_armies_by_country}')
  #       print(f'  Result defender armies by country: {result_defender_armies_by_country}')
  #       break
  #     # else, continue attacking
  #     print(f'  Continuing attack')
  #     attacker_armies, remaining_defender_armies = risk_rolls_battle_to_completion(attacker_armies, defender_armies)
  #     # if the attacker conquered the country
  #     if remaining_defender_armies == 0:
  #       print(f'  Attacker conquered country {index}. Attacker armies left: {attacker_armies}. Defender armies left: {remaining_defender_armies}')
  #       # set defender armies to 0
  #       result_defender_armies_by_country.append(0)
  #       # leave one army behind in the attacking country
  #       result_attacker_armies_by_country.append(1)
  #       attacker_armies -= 1
  #       #if the conquered country is the last one, put the remaining attacking armies there
  #       if index == len(defender_armies_list) - 1:
  #         result_attacker_armies_by_country[-1] += attacker_armies
  #         print(f'  Last country conquered, moving remaining {attacker_armies} armies to it')
  #       print(f'  Armies left in the attacking country {result_attacker_armies_by_country[-1]}')
  #     else:
  #       print(f'  Attacker failed to conquer country {index}. Attacker armies left: {attacker_armies}. Defender armies left: {remaining_defender_armies}')
  #       # put the remaining defender armies in the current country
  #       result_defender_armies_by_country.append(remaining_defender_armies)
  #       # put the remaining attacker armies in the current country
  #       result_attacker_armies_by_country.append(attacker_armies)
  #       print(f'  Armies left in the attacking country {result_attacker_armies_by_country[-1]}')
  #       # pad the rest of the attacker armies with 0s
  #       result_attacker_armies_by_country.extend([0] * (len(defender_armies_list) - index - 1))
  #       assert len(result_attacker_armies_by_country) == len(defender_armies_list)
  #       # pad the rest of the defender armies as is
  #       result_defender_armies_by_country.extend(defender_armies_list[index+1:])
  #       assert len(result_defender_armies_by_country) == len(defender_armies_list)
  #       print(f'  Result attacker armies by country: {result_attacker_armies_by_country}')
  #       print(f'  Result defender armies by country: {result_defender_armies_by_country}')
  #       break 

  # print(f'Final result attacker armies by country: {result_attacker_armies_by_country}')
  # print(f'Final result defender armies by country: {result_defender_armies_by_country}')
  # return result_attacker_armies_by_country, result_defender_armies_by_country

def repeated_risk_battles(attacker_armies, defender_armies, num_simulations):
  attacker_wins = 0
  defender_wins = 0
  for _ in range(num_simulations):
    final_attacker_armies, final_defender_armies = risk_rolls_battle_to_completion(attacker_armies, defender_armies)
    if final_defender_armies == 0:
      attacker_wins += 1
    else:
      defender_wins += 1
  return attacker_wins, defender_wins
