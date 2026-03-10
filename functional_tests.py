from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

  def setUp(self):
    self.browser = webdriver.Firefox()

  def tearDown(self):
    self.browser.quit()

  def test_wilhelm_can_simulate_risk_battle(self):
    # Wilhelm goes to a new app, starting on the home page.
    self.browser.get("http://localhost:8000")
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
    time.sleep(1)  # wait for the results to load
    result_statement = self.browser.find_element(By.ID, 'id_result_statement').text
    self.assertIn(result_statement, ["Attackers win", "Defenders win"])

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

    # Wilhelm is clicks to see the odds of a similar battle

    # Wilhelm sees the odds displayed on the page

    # Wilhelm is satisfied and closes the browser

if __name__ == '__main__':
  unittest.main()