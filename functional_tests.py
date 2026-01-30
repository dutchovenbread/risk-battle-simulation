import unittest

from selenium import webdriver

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

    # Wilhelm is invited to simulate a Risk battle right away.
    self.fail("Finish the test!")

    # Wilhelm types in the number of attacking armies

    # Wilhelm types in the number of defending armies

    # Wilhelm clicks the "Simulate" button

    # Wilhelm see the result of the battle simulation

    # Wilhelm is clicks to see the odds of a similar battle

    # Wilhelm sees the odds displayed on the page

    # Wilhelm is satisfied and closes the browser
    browser.quit()

if __name__ == '__main__':
  unittest.main()