from src.item import Item

class MixinLang:
    """Класс MixinLang для добавления в класс Keyboard
       функционала по хранению и изменению языка
       (раскладки клавиатуры) без изменения его основной структуры"""


    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        self.__language = "EN"

    def change_lang(self):
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"
        return self

    @property
    def language(self) -> str:
        """Геттер для атрибута language"""
        return self.__language


class Keyboard(MixinLang, Item):
    """Класс для представления товара Keyboard в магазине."""
    def __init__(self, name, price, quantity):
        """
        Создание экземпляра класса Keyboard в результате
        множественного наследования классов Item и MixinLang.
        """
        super().__init__(name, price, quantity)

