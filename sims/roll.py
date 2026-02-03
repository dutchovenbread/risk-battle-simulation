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
  assert defender_armies_list[0] == 0
  result_attacker_armies_by_country = [attacker_armies]
  result_attacker_armies_by_country.extend([0] * (len(defender_armies_list) -1))
  result_defender_armies_by_country = defender_armies_list

  # print(f'Initial attacker armies by country: {result_attacker_armies_by_country}')
  # print(f'Initial defender armies by country: {result_defender_armies_by_country}')

  for index in range(1, len(defender_armies_list)):
    attacker_armies = result_attacker_armies_by_country[index - 1]
    defender_armies = result_defender_armies_by_country[index]
    # print(f'Index: {index}, Attacker armies: {attacker_armies}, Defender armies: {defender_armies}')
    if attacker_armies <= 1:
      # print(f'  Only one attacker army left, stopping attack')
      break
    else:
      # print(f'  Continuing attack')
      attacker_armies_after_battle, remaining_defender_armies = risk_rolls_battle_to_completion(attacker_armies, defender_armies)
      if remaining_defender_armies == 0:
        # print(f'  Attacker conquered country {index}. Attacker armies left: {attacker_armies_after_battle}. Defender armies left: {remaining_defender_armies}')
        # set defender armies to 0
        result_defender_armies_by_country[index] = 0
        # leave one army behind in the attacking country
        result_attacker_armies_by_country[index - 1] = 1
        # move remaining attacking armies to conquered country
        result_attacker_armies_by_country[index] = attacker_armies_after_battle - 1
        # print(f'  Armies left in the attacking country {result_attacker_armies_by_country[index-1]}')
        # print(f'  Armies moved to conquered country {result_attacker_armies_by_country[index]}')
      else:
        # print(f'  Attacker failed to conquer country {index}. Attacker armies left: {attacker_armies_after_battle}. Defender armies left: {remaining_defender_armies}')
        # put the remaining defender armies in the current country
        result_defender_armies_by_country[index] = remaining_defender_armies
        # put the remaining attacker armies in the current country
        result_attacker_armies_by_country[index - 1] = attacker_armies_after_battle
        # print(f'  Armies left in the attacking country {result_attacker_armies_by_country[index - 1]}')
        break
  # print(f'Final result attacker armies by country: {result_attacker_armies_by_country}')
  # print(f'Final result defender armies by country: {result_defender_armies_by_country}')
  return result_attacker_armies_by_country, result_defender_armies_by_country

def successive_country_summary(attacker_armies_list, defender_armies_list):
  total_armies_able_to_attack = (attacker_armies_list[-1] -1 ) if attacker_armies_list[-1] > 1 else 0
  total_defender_armies_remaining = sum(defender_armies_list)
  summary = total_armies_able_to_attack - total_defender_armies_remaining
  return summary

def individual_battle_summary(attacker_armies, defender_armies):
  if attacker_armies == 1:
    return -1 * defender_armies
  else:
    return attacker_armies - 1


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
