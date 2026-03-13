from django.test import TestCase
from django.http import HttpRequest
from sims.views import home_page

class HomePageTest(TestCase):
  def test_uses_home_template(self):
    response = self.client.get('/')
    self.assertTemplateUsed(response, 'home.html')

  def test_renders_homepage_content(self):
    response = self.client.get('/')
    self.assertContains(response, 'Risk Simulation')

  def test_renders_homepage_form(self):
    response = self.client.get('/')
    self.assertContains(response, '<form method="POST">')
    self.assertContains(response, 'name="attacking_armies"')
    self.assertContains(response, 'name="defending_armies"')
    

  def test_home_page_can_submit_post_request(self):
    response = self.client.post('/', data={
      'attacking_armies': '5',
      'defending_armies': '3',
    })
    self.assertEqual(response.status_code, 200)
    contains_win = response.content.decode().find('Attackers win') != -1
    contains_lose = response.content.decode().find('Defenders win') != -1
    self.assertTrue(contains_win or contains_lose)
    self.assertFalse(contains_win and contains_lose)
    self.assertTemplateUsed(response, 'home.html')

  def test_home_page_does_not_show_result_before_post_request(self):
    response = self.client.get('/')
    self.assertNotContains(response, 'Attackers win')
    self.assertNotContains(response, 'Defenders win')

  def test_home_page_shows_result_after_post_request_attacker_win(self):
    response = self.client.post('/', data={
      'attacking_armies': '100',
      'defending_armies': '1',
    })
    self.assertContains(response, 'Attackers win')
    self.assertNotContains(response, 'Defenders win')
    self.assertTemplateUsed(response, 'home.html')

  def test_home_page_shows_result_after_post_request_defender_win(self):
    response = self.client.post('/', data={
      'attacking_armies': '1',
      'defending_armies': '100',
    })
    self.assertContains(response, 'Defenders win')
    self.assertNotContains(response, 'Attackers win')
    self.assertTemplateUsed(response, 'home.html')

  def test_home_page_shows_remaining_armies_after_post_request(self):
    response = self.client.post('/', data={
      'attacking_armies': '5',
      'defending_armies': '3',
    })
    self.assertContains(response, 'Attacking armies remaining:')
    self.assertContains(response, 'Defending armies remaining:')
    self.assertTemplateUsed(response, 'home.html')

  def test_home_page_shows_starting_armies_after_post_request(self):
    attacking_armies = '5'
    defending_armies = '3'
    response = self.client.post('/', data={
      'attacking_armies': attacking_armies,
      'defending_armies': defending_armies,
    })
    self.assertContains(response, f'Attacking armies starting: {attacking_armies}')
    self.assertContains(response, f'Defending armies starting: {defending_armies}')
    self.assertTemplateUsed(response, 'home.html')

  def test_home_page_shows_history_after_multiple_post_requests(self):
    response1 = self.client.post('/', data={
      'attacking_armies': '5',
      'defending_armies': '3',
    })
    response2 = self.client.post('/', data={
      'attacking_armies': '10',
      'defending_armies': '9',
    })
    # history renders as an HTML table with the expected columns
    self.assertContains(response2, '<table')
    self.assertContains(response2, 'Date/Time')
    self.assertContains(response2, 'Attacking Armies')
    self.assertContains(response2, 'Defending Armies')
    self.assertContains(response2, 'Resulting Attacking Armies')
    self.assertContains(response2, 'Resulting Defending Armies')
    self.assertContains(response2, 'Result')
    # rows should include the submitted start values
    self.assertContains(response2, '5')
    self.assertContains(response2, '3')
    self.assertContains(response2, '10')
    self.assertContains(response2, '9')
    self.assertTemplateUsed(response2, 'home.html')