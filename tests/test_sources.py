import unittest
from app.models import Sources

class TestSources(unittest.TestCase):

    def setUp(self):

        self.new_source = Sources('espn', 'ESPN', 'Get all the latest news on football across Europe', 'https://espn.com', 'sports', 'USA')

    def test_insistance(self):

        self.assertTrue(isinstance(self.new_source,Sources))

    def test_init(self):

        self.assertEquals(self.new_source.id,'espn')
        self.assertEquals(self.new_source.name, 'ESPN')
        self.assertEquals(self.new_source.description, 'Get all the latest news on football across Europe')
        self.assertEquals(self.new_source.url, 'https://espn.com')
        self.assertEquals(self.new_source.category, 'sports')
        self.assertEquals(self.new_source.country, 'USA')

if __name__ == '__main__':
    unittest.main()