from unittest import TestCase
from elang.word2vec.utils import remove_region_id, remove_stopwords_id, remove_vulgarity_id

class TestRemove(TestCase):
    def test_remove_region(self):
        sen = "Sudah pernah naik kereta dari Jakarta ke Bandung dari stasiun nggak?"
        res = remove_region_id(sen)
        self.assertLess(len(res.split(" ")), len(sen.split(" ")))

        