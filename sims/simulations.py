from roll import risk_rolls, repeated_risk_battles

def simulate_2v1_battle():
  attacker_wins = 0
  defender_wins = 0
  for i in range(100000):
    attacking_armes = 2
    defending_armies = 1
    attacker_losses, defender_losses = risk_rolls(attacking_armes, defending_armies)
    attacker_wins += defender_losses
    defender_wins += attacker_losses
  print(f"Attackers win {attacker_wins} times.")
  print(f"Defenders win {defender_wins} times.")

def simulate_up_to_30_armies():
  simulations = 100000
  for attacker_armies in range(30,1,-1):
    for defender_armies in range(30,2,-1):
      attacker_wins, defender_wins = repeated_risk_battles(attacker_armies, defender_armies, simulations)
      print(f"{attacker_armies} attacking armies vs {defender_armies} defending armies: Attackers won {attacker_wins} times ({(attacker_wins/simulations)*100:.2f}%), Defenders won {defender_wins} times ({(defender_wins/simulations)*100:.2f}%)")

def main():
  simulations = 100000
  for attacker_armies, defender_armies in ((70,35), (62,30), (56,23)):
    attacker_wins, defender_wins = repeated_risk_battles(attacker_armies, defender_armies, simulations)
    print(f"{attacker_armies} attacking armies vs {defender_armies} defending armies: Attackers won {attacker_wins} times ({(attacker_wins/simulations)*100:.2f}%), Defenders won {defender_wins} times ({(defender_wins/simulations)*100:.2f}%)")
if __name__ == "__main__":
  main()