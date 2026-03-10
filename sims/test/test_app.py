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