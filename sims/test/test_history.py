from django.test import TestCase
from django.utils import timezone
from sims.models import Simulation

class SimulationModelTest(TestCase):
  def test_saving_and_retrieving_simulations(self):
    first_simulation = Simulation()
    first_simulation.attacking_armies_starting = 5
    first_simulation.defending_armies_starting = 3
    first_simulation.attacking_armies_remaining = 2
    first_simulation.defending_armies_remaining = 0
    first_simulation.result_statement = "Attackers win"
    first_ts = timezone.now()
    first_simulation.timestamp = first_ts
    first_simulation.save()

    second_simulation = Simulation()
    second_simulation.attacking_armies_starting = 10
    second_simulation.defending_armies_starting = 10
    second_simulation.attacking_armies_remaining = 1
    second_simulation.defending_armies_remaining = 0
    second_simulation.result_statement = "Attackers win"
    second_ts = timezone.now()
    second_simulation.timestamp = second_ts
    second_simulation.save()

    saved_simulations = Simulation.objects.all()
    self.assertEqual(saved_simulations.count(), 2)

    first_saved_simulation = saved_simulations[0]
    second_saved_simulation = saved_simulations[1]
    self.assertEqual(first_saved_simulation.attacking_armies_starting, 5)
    self.assertEqual(first_saved_simulation.defending_armies_starting, 3)
    self.assertEqual(first_saved_simulation.attacking_armies_remaining, 2)
    self.assertEqual(first_saved_simulation.defending_armies_remaining, 0)
    self.assertEqual(first_saved_simulation.result_statement, "Attackers win")
    self.assertEqual(first_saved_simulation.timestamp, first_ts)
    self.assertEqual(second_saved_simulation.attacking_armies_starting, 10)
    self.assertEqual(second_saved_simulation.defending_armies_starting, 10)
    self.assertEqual(second_saved_simulation.attacking_armies_remaining, 1)
    self.assertEqual(second_saved_simulation.defending_armies_remaining, 0)
    self.assertEqual(second_saved_simulation.result_statement, "Attackers win")
    self.assertEqual(second_saved_simulation.timestamp, second_ts)