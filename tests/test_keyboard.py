import pytest
from src.keyboard import Keyboard

def test_str():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb) == "Dark Project KD87A"


def test_init():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert kb.name == 'Dark Project KD87A'
    assert kb.price == 9600
    assert kb.quantity == 5
    assert kb.language == "EN"


def test_change_lang():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    kb.change_lang()
    assert str(kb.language) == "RU"
    kb.change_lang().change_lang()
    assert str(kb.language) == "RU"

    # Сделали RU -> EN -> RU
    kb.change_lang().change_lang()
    assert str(kb.language) == "RU"