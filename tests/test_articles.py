import unittest
from app.models import Articles

class TestArticles(unittest.TestCase):

    def setUp(self):

        self.new_article = Articles(1,'derrick', 'Manchester United sign Bruno Fernandes', 'Manchester United have announced the signing of Portugese midfielder Bruno Fernandes for 68 million after a month long transfer saga', 'https://derricknews.com', 'https://image.com', '2020-01-21T14:50:05Z', )

    def test_instance(self):

        self.assertTrue(isinstance(self.new_article,Articles))

    def test_init(self):

        self.assertEqual(self.new_article.id, 1)
        self.assertEqual(self.new_article.author, 'derrick')
        self.assertEqual(self.new_article.title, 'Manchester United sign Bruno Fernandes')
        self.assertEqual(self.new_article.description, 'Manchester United have announced the signing of Portugese midfielder Bruno Fernandes for 68 million after a month long transfer saga')
        self.assertEqual(self.new_article.url, 'https://derricknews.com')
        self.assertEqual(self.new_article.urlToImage, 'https://image.com')
        self.assertEqual(self.new_article.publishedAt, '2020-01-21T14:50:05Z')

if __name__ == '__main__':
    unittest.main()