from roll import roll_die, roll_multiple_dice, risk_rolls, repeated_risk_battles, risk_attack_successive_countries

def main():
  # simulate some dice rolls and print the results
  for i in range(12):
    # rolle one die and print the result
    die_result = roll_die()
    print(f"Rolled a die: {die_result[0]}")

  for i in range(12):
    # simulate rolling two dice
    result = roll_multiple_dice(2)
    print(f"Rolling two dice: {result[0]}, {result[1]}")

  for i in range(12):
    # simulate rolling 3 dice
    result = roll_multiple_dice(3)
    print(f"Rolling three dice: {result[0]}, {result[1]}, {result[2]}")

  for i in range(12):
    # simulate a risk roll with 4 attacking armies and 2 defending armies
    attacker_losses, defender_losses = risk_rolls(4, 2)
    print(f"Risk roll with 4 attacking armies and 2 defending armies: Attacker losses: {attacker_losses}, Defender losses: {defender_losses}")

  for i in range(12):
    # simulate repeated risk battles with 36 attacking armies and 
    # attacking 38 countries with 1 defending army each, 
    # except the second country has 3 armies
    defender_armies_list = [0] + [1]*37
    defender_armies_list[2] = 3
    attacker_armies = 36
    attacker_wins, defender_wins = risk_attack_successive_countries(attacker_armies, defender_armies_list)

    print(f"Risk attack successive countries with {attacker_armies} attacking armies.")
    print(f"Final number of attcker countries taken: {sum(1 for armies in defender_armies_list if armies == 0) - 1}")
    print(f'Final number of defender countries defended: {sum(1 for armies in defender_armies_list if armies > 0)}')
    print('\n')


  # simulate repeated risk battles with 36 attacking armies and 
  # attacking 38 countries with 1 defending army each, 
  # except the second country has 3 armies
  # do the above 100,000 times and collect statistics
  total_attacker_countries_taken = 0
  number_of_simulations = 100000

  for i in range(number_of_simulations):
    # simulate repeated risk battles with 36 attacking armies and 
    # attacking 38 countries with 1 defending army each, 
    # except the second country has 3 armies
    defender_armies_list = [0] + [1]*37
    defender_armies_list[2] = 3
    attacker_armies = 36
    attacker_wins, defender_wins = risk_attack_successive_countries(attacker_armies, defender_armies_list)

    # print(f"Risk attack successive countries with {attacker_armies} attacking armies.")
    # print(f"Final number of attcker countries taken: {sum(1 for armies in defender_armies_list if armies == 0) - 1}")
    # print(f'Final number of defender countries defended: {sum(1 for armies in defender_armies_list if armies > 0)}')
    # print('\n')
    total_attacker_countries_taken += sum(1 for armies in defender_armies_list if armies == 0) - 1
  print(f"After {number_of_simulations} simulations, average number of attacker countries taken: {total_attacker_countries_taken / number_of_simulations:.2f}")

if __name__ == "__main__":
  main()