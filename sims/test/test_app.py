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

  def test_home_page_can_submit_post_request(self):
    response = self.client.post('/', data={
      'attacking_armies': '5',
      'defending_armies': '3',
    })
    self.assertEqual(response.status_code, 200)
    contains_win = response.content.decode().find('Attackers win') != -1
    contains_lose = response.content.decode().find('Defenders win') != -1
    self.assertTrue(contains_win or contains_lose)

