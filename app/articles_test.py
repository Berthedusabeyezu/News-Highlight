import unittest
from models import articles
Articles = articles.Articles

class ArticlesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Articles class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_articles = Articles('Romain Dillet','Coinbase users can now withdraw Bitcoin SV following BCH fork','https://www.newsbtc.com/2019/02/19/ethereum-price-analysis-eth-rally-takes-break-uptrend-intact-above-140','https://techcrunch.com/wp-content/uploads/2017/08/bitcoin-split-2017a.jpg?w=711','2019-02-15T14:53:40Z','ETH price extended the recent rally and traded above the $144 and $148 resistances against the US Dollar')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_articles,Articles))


if __name__ == '__main__':
    unittest.main()  