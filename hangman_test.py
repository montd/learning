"""Automated test of hangman.py"""
from hangman import guessing

def test_guessing() -> None:
    guessing(5,"aaaaa") == 5