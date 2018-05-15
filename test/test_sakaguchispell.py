
import unittest

import shorttext.spell.sakaguchi as sk

class TestSCRNN(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def generalproc(self, operation):
        corrector = sk.SCRNNSpellCorrector(operation)
        corrector.train('I am a nerd . Natural language processing is sosad .')
        self.assertEqual(corrector.correct('langudge'), 'language')

    def test_NOISE_INSERT(self):
        self.generalproc('NOISE-INSERT')

    def test_NOISE_DELETE(self):
        self.generalproc('NOISE-DELETE')

    def test_NOISE_REPLACE(self):
        self.generalproc('NOISE-REPLACE')

    def test_JUMBLE_WHOLE(self):
        self.generalproc('NOISE-WHOLE')

    def test_JUMBLE_BEG(self):
        self.generalproc('JUMBLE-BEG')

    def test_JUMBLE_END(self):
        self.generalproc('JUMBLE-END')

    def test_JUMBLE_INT(self):
        self.generalproc('JUMBLE-INT')


if __name__ == '__main__':
    unittest.main()

