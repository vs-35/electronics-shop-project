from src.item import Item
class MixinLog:
    """Класс MixinLog для добавления в класс Keyboard
       функционала по хранению и изменению языка
       (раскладки клавиатуры) без изменения его основной структуры"""

    LANG = "EN"

    def init(self):
        super().__init__()
        self.__language = self.LANG


    def __str__(self):
        """Метод для отображения информации об объекте класса (о языке (раскладки клавиатуры) для пользователей"""
        return self.__language

    def change_lang(self):
        if self.__language == "EN":
            return self.__language == "RU"
        if self.__language == "RU":
            return self.__language == "EN"

    @property
    def language(self):
        return self.LANG


    @language.setter
    def language(self, lang):
        if lang != "EN":
            if lang != "RU":
                print("AttributeError: property 'language' of 'KeyBoard' object has no setter")


class Keyboard(Item, MixinLog):
    """Класс для представления товара Keyboard в магазине."""
    def __init__(self, name, price, quantity):
        """
        Создание экземпляра класса Keyboard в результате
        множественного наследования классов Item и MixinLog.
        """
        super().__init__(name, price, quantity)
        self.name = name


    def __str__(self) -> str:
        """Метод для отображения информации об объекте класса для пользователей"""
        return self.name