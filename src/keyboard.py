from src.item import Item

class Keyboard(Item, MixinLog):
    """
       Класс для представления нового товара в магазине.
       """

    def __init__(self, name: str, price: float, quantity: int, language: str):
        """
        Создание экземпляра дочернего класса phone.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        :param language: Язык ввода (раскладки клавиатуры).
        """
        super().__init__(self, name, price, quantity)
        self.language = language

class MixinLog:
    """Класс MixinLog для добавления в класс функционала по изменению языка (раскладки клавиатуры) без изменения его основной структуры"""
    list_lang = ["EN", "RU"]

    def __init__(self):
        self.language = self.list_lang[0]

    def change_lang(self):
        for language in list_lang:
            if language in range [0]:
                self.language = self.list_lang[0]
            elif language in range [1]:
                self.language = self.list_lang[1]


    # Геттер для language
    @property
    def language(self):
        """Возвращает информацию о языке ввода (раскладке клавиатуры). К атрибуту можно обращаться без вызова."""
        return self.language

    # Cеттер для language
    @language.setter
    def language(self, language):
        """Сеттер проверяет, что что язык ввода (раскладка клавиатуры) соответствует заданным значениям "EN" или "RU"."""
        if language not in list_lang:
            raise AttributeError('property 'language' of 'Keyboard' object has no setter')
        self.language = language