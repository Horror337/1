from django.test import TestCase , SimpleTestCase
from django.urls import reverse
#TestCase for working with database
#SimpleTestCase for working with out data base

# Create your tests here.
class testClass(SimpleTestCase):
    def testUrlMessage(self):
        response = self.client.get('/message/')
        self.assertEqual(response.status_code , 200)
    def testUrlAbout(self):
        response = self.client.get('/message/about/')
        self.assertEqual(response.status_code , 200)
    def testMessageContains(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response , '<h2>Home page</h2>')
    def testAboutContains(self):
        response = self.client.get(reverse('about'))
        self.assertContains(response , "<h2>About page</h2>")
    def testMessageHtmlFile(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response , "home.html")
    def testAboutHtmlFile(self):
        response = self.client.get(reverse('about'))
        self.assertTemplateUsed(response , "about.html")