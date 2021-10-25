from unittest import mock
from unittest import TestCase
import hangman


class GuessingGoodAnswerTests(TestCase):

    gSegments = 6
    wordLength = 12

    @mock.patch('hangman.input', create=True)
    def testSingleLetter(self, mocked_input):
        mocked_input.side_effect = ['a']
        assert hangman.guessing(self.gSegments,"aaaaa") == 1
        # self.assertEqual(result, ({}))

    @mock.patch('hangman.input', create=True)
    def testTwoLetters(self, mocked_input):
        mocked_input.side_effect = ['a', 'b']
        assert hangman.guessing(self.gSegments,"babaa") == 1
        # self.assertEqual(result, ({}))

    @mock.patch('hangman.input', create=True)
    def testSingleLetterBad(self, mocked_input):
        mocked_input.side_effect = ['b' for i in range(self.wordLength)]
        assert hangman.guessing(self.gSegments,
                                ''.join(['a' for i in range(self.wordLength)])) == 0
