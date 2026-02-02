from roll import roll_die, roll_multiple_dice, risk_rolls, repeated_risk_battles

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

if __name__ == "__main__":
  main()