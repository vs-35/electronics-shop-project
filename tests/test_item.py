"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item
from src.phone import Phone


def test_calculate_total_price():
    item1 = Item("Смартфон", 10000, 20)
    assert item1.calculate_total_price() == 200000


def test_instantiate_from_csv():
    item1 = Item.all[0]
    assert item1.name == 'Смартфон'


def test_init():
    item1 = Item('Смартфон', 10000, 20)
    assert item1.name == 'Смартфон'
    assert item1.price == 10000
    assert item1.quantity == 20


def test_apply_discount(item1):
    item1 = Item("Смартфон", 10000, 20)
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000.0
    Item.pay_rate = 0
    item1.apply_discount()
    assert item1.price == None


def test_all():
    assert Item.all != []


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_repr_():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_str():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'


def test_add():
     item1 = Item("Смартфон", 10000, 20)
     phone1 = Phone("iPhone 14", 120_000, 5, 2)
     assert item1 + phone1 == 25