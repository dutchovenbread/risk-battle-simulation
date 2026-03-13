from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest

MAX_WAIT = 5

class NewVisitorTest(StaticLiveServerTestCase):

  def setUp(self):
    self.browser = webdriver.Firefox()

  def tearDown(self):
    self.browser.quit()

  def wait_for_result_statement(self, expected_text_1, expected_text_2=None):
    start_time = time.time()
    while True:
      try:
        result_statement = self.browser.find_element(By.ID, 'id_result_statement').text
        expected_text = [expected_text_1]
        if expected_text_2:
          expected_text.append(expected_text_2)
        self.assertIn(result_statement, expected_text)
        return result_statement
      except (AssertionError, Exception) as e:
        if time.time() - start_time > MAX_WAIT:
          raise e
        time.sleep(0.5)

  def wait_for_row_in_results_table(self, starting_attacking, starting_defending):
    """Wait until a row appears in the history table with the given starting values.

    Supports tables with or without a leading timestamp column.
    """
    start_time = time.time()
    while True:
      try:
        results_table = self.browser.find_element(By.ID, 'id_history')
        rows = results_table.find_elements(By.TAG_NAME, 'tr')
        for row in rows:
          cells = row.find_elements(By.TAG_NAME, 'td')
          if len(cells) >= 5:
            # If there's a timestamp column, starting values are at 1 and 2
            if len(cells) >= 6:
              a = cells[1].text
              d = cells[2].text
            else:
              a = cells[0].text
              d = cells[1].text
            if a == str(starting_attacking) and d == str(starting_defending):
              return
        # not found yet -> retry
      except Exception as e:
        last_exc = e
      if time.time() - start_time > MAX_WAIT:
        # raise the last exception or an assertion
        try:
          raise last_exc
        except Exception:
          raise AssertionError(f"Row with starting values {starting_attacking}, {starting_defending} not found in table")
      time.sleep(0.5)

  def test_wilhelm_can_simulate_risk_battle(self):
    # Wilhelm goes to a new app, starting on the home page.
    self.browser.get(self.live_server_url)
    # Wilhelm notices the title of the page.
    self.assertIn("Risk Simulation", self.browser.title)
    header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
    self.assertIn("Risk Simulation", header_text)

    # Wilhelm is invited to simulate a Risk battle right away.
    attacking_inputbox = self.browser.find_element(By.ID, 'id_attacking_armies')
    self.assertEqual(attacking_inputbox.get_attribute('placeholder'), 'Number of attacking armies')
    defending_inputbox = self.browser.find_element(By.ID, 'id_defending_armies')
    self.assertEqual(defending_inputbox.get_attribute('placeholder'), 'Number of defending armies')

    # Wilhelm types in the number of attacking armies
    attacking_inputbox.send_keys('5')

    # Wilhelm types in the number of defending armies
    defending_inputbox.send_keys('3')

    # Wilhelm clicks the "Simulate" button
    simulate_button = self.browser.find_element(By.ID, 'id_simulate_button')
    self.assertEqual(simulate_button.text, 'Simulate')
    simulate_button.click()

    # Wilhelm see the result of the battle simulation
    result_statement = self.wait_for_result_statement("Attackers win", "Defenders win")

    # Wilhelm sees the number of armies each side had at the beginning of the battle
    attacking_starting_text = self.browser.find_element(By.ID, 'id_attacking_armies_starting').text
    defending_starting_text = self.browser.find_element(By.ID, 'id_defending_armies_starting').text
    self.assertIn("Attacking armies starting:", attacking_starting_text)
    self.assertIn("Defending armies starting:", defending_starting_text)

    # Wilhelm sees the remaining armies for each side
    attacking_remaining_text = self.browser.find_element(By.ID, 'id_attacking_armies_remaining').text
    defending_remaining_text = self.browser.find_element(By.ID, 'id_defending_armies_remaining').text
    self.assertIn("Attacking armies remaining:", attacking_remaining_text)
    self.assertIn("Defending armies remaining:", defending_remaining_text)
    attacking_remaining = int(attacking_remaining_text.split(':', 1)[1].strip())
    defending_remaining = int(defending_remaining_text.split(':', 1)[1].strip())
    self.assertGreaterEqual(attacking_remaining, 1)
    self.assertGreaterEqual(defending_remaining, 0)
    if result_statement == "Attackers win":
      self.assertEqual(defending_remaining, 0)
    else:
      self.assertEqual(attacking_remaining, 1)

    # Wilhelm runs another simulation with different starting armies
    attacking_inputbox = self.browser.find_element(By.ID, 'id_attacking_armies')
    defending_inputbox = self.browser.find_element(By.ID, 'id_defending_armies')
    attacking_inputbox.clear()
    defending_inputbox.clear()
    attacking_inputbox.send_keys('10')
    defending_inputbox.send_keys('10')
    simulate_button = self.browser.find_element(By.ID, 'id_simulate_button')
    simulate_button.click()

    # Wilhelm sees the result of the second battle simulation
    result_statement = self.wait_for_result_statement("Attackers win", "Defenders win")

    # In a previous results table, Wilhelm sees the results of his previous simulations, including the one with 5 attacking and 3 defending armies, and the one with 10 attacking and 10 defending armies. He sees the starting and remaining armies for each simulation, and the result statement for each simulation.
    self.wait_for_row_in_results_table('5', '3')
    self.wait_for_row_in_results_table('10', '10')
    results_table = self.browser.find_element(By.ID, 'id_history')
    rows = results_table.find_elements(By.TAG_NAME, 'tr')
    self.assertGreaterEqual(len(rows), 2)  # at least 2 rows for the two simulations
    found_first_simulation = False
    found_second_simulation = False
    for row in rows:
      cells = row.find_elements(By.TAG_NAME, 'td')
      # support table with Date/Time + 5 data columns (6 tds)
      if len(cells) >= 5:
        # if there's a timestamp column, starting values shift by one
        if len(cells) >= 6:
          starting_attacking = cells[1].text
          starting_defending = cells[2].text
          remaining_attacking = cells[3].text
          remaining_defending = cells[4].text
          result = cells[5].text
        else:
          starting_attacking = cells[0].text
          starting_defending = cells[1].text
          remaining_attacking = cells[2].text
          remaining_defending = cells[3].text
          result = cells[4].text
        if (starting_attacking == '5' and starting_defending == '3'):
          found_first_simulation = True
          self.assertIn(result, ["Attackers win", "Defenders win"])
          self.assertGreaterEqual(int(remaining_attacking), 1)
          self.assertGreaterEqual(int(remaining_defending), 0)
          if result == "Attackers win":
            self.assertEqual(int(remaining_defending), 0)
          else:
            self.assertEqual(int(remaining_attacking), 1)
        elif (starting_attacking == '10' and starting_defending == '10'):
          found_second_simulation = True
          self.assertIn(result, ["Attackers win", "Defenders win"])
          self.assertGreaterEqual(int(remaining_attacking), 1)
          self.assertGreaterEqual(int(remaining_defending), 0)
          if result == "Attackers win":
            self.assertEqual(int(remaining_defending), 0)
          else:
            self.assertEqual(int(remaining_attacking), 1)
    self.assertTrue(found_first_simulation)
    self.assertTrue(found_second_simulation) 



    # Wilhelm is satisfied and closes the browser
    self.browser.quit()

