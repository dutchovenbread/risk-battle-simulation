from sims.roll import roll_die, roll_multiple_dice, risk_rolls, risk_attack_successive_countries

def test_roll_one_die():
  for i in range(100):  
    result = roll_die()
    assert 1 <= result[0] <= 6

def test_roll_multiple_dice():
  for j in range(100):  
    for i in range(1,4):
      results = roll_multiple_dice(i)
      assert len(results) == i
      for result in results:
        assert 1 <= result <= 6

def test_risk_rolls():
  for j in range(100):  
    for attacking_armies in range(1,4):
      for defending_armies in range(1,3):
        risk_roll_result = risk_rolls(attacking_armies, defending_armies)
        assert len(risk_roll_result) == 2
        attacker_losses, defender_losses = risk_roll_result
        assert 0 <= attacker_losses <= 2
        assert 0 <= defender_losses <= 2
        assert attacker_losses + defender_losses == min(2, attacking_armies - 1, defending_armies)

def test_risk_rolls_battle_to_completion_2_1():
  for j in range(100):  
    attacking_armies = 2
    defending_armies = 1
    while attacking_armies > 1 and defending_armies > 0:
      attacker_losses, defender_losses = risk_rolls(attacking_armies, defending_armies)
      attacking_armies -= attacker_losses
      defending_armies -= defender_losses
    assert attacking_armies == 1 or defending_armies == 0
    assert attacking_armies + defending_armies >= 1
    assert attacking_armies <= 2
    assert defending_armies <= 1

def test_risk_rolls_battle_to_completion_3_1():
  for j in range(100):  
    attacking_armies = 3
    defending_armies = 1
    while attacking_armies > 1 and defending_armies > 0:
      attacker_losses, defender_losses = risk_rolls(attacking_armies, defending_armies)
      attacking_armies -= attacker_losses
      defending_armies -= defender_losses
    assert attacking_armies == 1 or defending_armies == 0
    assert attacking_armies + defending_armies >= 1
    assert attacking_armies <= 3
    assert defending_armies <= 1
def test_risk_rolls_battle_to_completion_3_2():
  for j in range(100):  
    attacking_armies = 3
    defending_armies = 2
    while attacking_armies > 1 and defending_armies > 0:
      attacker_losses, defender_losses = risk_rolls(attacking_armies, defending_armies)
      attacking_armies -= attacker_losses
      defending_armies -= defender_losses
    assert attacking_armies == 1 or defending_armies == 0
    assert attacking_armies + defending_armies >= 1
    assert attacking_armies <= 3
    assert defending_armies <= 2

def test_risk_rolls_battle_to_completion_4_2():
  for j in range(100):  
    attacking_armies = 4
    defending_armies = 2
    while attacking_armies > 1 and defending_armies > 0:
      attacker_losses, defender_losses = risk_rolls(attacking_armies, defending_armies)
      attacking_armies -= attacker_losses
      defending_armies -= defender_losses
    assert attacking_armies == 1 or defending_armies == 0
    assert attacking_armies + defending_armies >= 1
    assert attacking_armies <= 4
    assert defending_armies <= 2

def test_risk_rolls_battle_to_completion_5_3():
  for j in range(100):  
    attacking_armies = 5
    defending_armies = 3
    while attacking_armies > 1 and defending_armies > 0:
      attacker_losses, defender_losses = risk_rolls(attacking_armies, defending_armies)
      attacking_armies -= attacker_losses
      defending_armies -= defender_losses
    assert attacking_armies == 1 or defending_armies == 0
    assert attacking_armies + defending_armies >= 1
    assert attacking_armies <= 5
    assert defending_armies <= 3
  
def test_succession_of_defended_countries():
  for j in range(100):  
    attacking_armies = 10
    defending_armies_list = [0, 3, 2, 1]
    attacking_armies_by_country, defending_armies_by_country = risk_attack_successive_countries(attacking_armies, defending_armies_list)
    assert len(defending_armies_by_country) == len(defending_armies_list)
    assert len(attacking_armies_by_country) == len(defending_armies_list)
    for i in range(len(defending_armies_list)):
      assert defending_armies_by_country[i] == 0 or attacking_armies_by_country[i] == 0
      assert defending_armies_by_country[i] <= defending_armies_list[i]
    assert sum(attacking_armies_by_country) <= attacking_armies
    print("successful test of succession of defended countries")

def test_succession_of_defended_countries_2_1_1():
  attacking_armies = 2
  defending_armies_list = [0, 1, 1]
  attacking_armies_by_country, defending_armies_by_country = risk_attack_successive_countries(attacking_armies, defending_armies_list)
  assert defending_armies_by_country == [0, 0, 1] or defending_armies_by_country == [0, 1, 1]
  assert attacking_armies_by_country == [1, 1, 0] or attacking_armies_by_country == [1, 0, 0]
  assert sum(attacking_armies_by_country) + sum(defending_armies_by_country) == 3

def test_succession_of_defended_countries_1_1_1():
  attacking_armies = 1
  defending_armies_list = [0, 1, 1]
  attacking_armies_by_country, defending_armies_by_country = risk_attack_successive_countries(attacking_armies, defending_armies_list)
  assert defending_armies_by_country == [0, 1, 1]
  assert attacking_armies_by_country == [1, 0, 0]
  assert sum(attacking_armies_by_country) + sum(defending_armies_by_country) == 3   

