from .. wordl import get_random_word, val_guess, load_words
import pytest
from string import ascii_letters

guess_tests = [("UVWXY","ABCDE","00000"),
               ("ABDEY","ABCDE","11??0")]

word_validators = [("is 5 long", lambda word: len(word)==5),
                   ("is ascii", lambda word: all(c in ascii_letters for c in word)),
                   ("is upper", lambda word: word.isupper()),
                   ]

@pytest.fixture()
def words():
    return load_words()

@pytest.mark.parametrize("guess,word,result",guess_tests)
def test_val_guess(guess,word,result):
    res = val_guess(guess,word)
    assert res==result

def test_load_words(words):
    assert len(words)>0

def test_get_random_word(words):
    assert get_random_word(words) in words

@pytest.mark.parametrize("val_name, val_fct",word_validators)
def test_load_words_are_valid(words, val_name, val_fct):
    assert all(val_fct(word) for word in words)

