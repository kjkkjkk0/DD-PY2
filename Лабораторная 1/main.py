import doctest


class Animal:
    slovar_pishi = {'Травоядное': ["grass"], 'Плотоядное': ['meat'], 'Всеядное': ['meat, grass']}

    def __init__(self, status: bool, kingdom: str, name: str, meal_category: str):
        """
        Подготовка и создание объекта 'Animal'

        :param status: Можно ли приручить животное
        :param kingdom: К какому царству относится животное
        :param name: Название животного
        :param meal_category: Плотоядное/траваядное/всеядное

        Примеры:
        >>> tiger = Animal(False, "Cats", "Тигр", "Плотоядное")
        """
        if not isinstance(status, bool):
            raise TypeError("Статус животного должент быть типа bool")
        self.status = status
        if not isinstance(kingdom, str):
            raise TypeError("Название царства животного должно быть типа str")
        self.kingdom = kingdom
        if not isinstance(name, str):
            raise TypeError("Название животного должно быть типа str")
        self.name = name
        if not isinstance(meal_category, str):
            raise TypeError("Вид пищи животного должен быть типа str")
        self.meal_category = meal_category

    def tame(self, points: int) -> str:
        """
        Приручение животного

        :param points: Насколько хорошо у вас развит навык приручения
        :return: Приручилось ли животное

        Примеры:
        >>> tiger = Animal(True, "Cats", "Тигр", "Плотоядное")
        >>> tiger.tame(10)
        """
        ...
        if not isinstance(points, int):
            raise TypeError("Число навыка приручения должно быть типа int")
        if 10 < points < 0:
            raise ValueError("Число навыка приручения должно быть от 0 до 10")
        if not self.status:
            return f'{self.name} нельзя приручить'

    def feed(self, food: str):
        """
        Кормление животного

        :param food: Еда которой будете кормить

        Примеры:
        >>> tiger = Animal(False, "Cats", "Тигр", "Плотоядное")
        >>> tiger.feed('meat')
        """
        ...
        if not isinstance(food, str):
            raise TypeError("Название пищи должно быть типа str")
        if food not in Animal.slovar_pishi[self.meal_category]:
            raise ValueError("Этой едой нельзя кормить " f'{self.name}')


class KitchenTech:

    def __init__(self, tech: dict, count_sits: int):
        """
        Подготовка и создание объекта 'KitchenTech'

        :param tech: Техника на кухне (ключ: название, значение: id)
        :param count_sits: Число мест на кухне

        Примеры:

        """
        if not isinstance(tech, dict):
            raise TypeError("Техника должна быть зарегестрировна в виде словаря dict")
        self.tech = tech
        if not isinstance(count_sits, int):
            raise TypeError("Число мест на кухне должно быть типа int")
        if count_sits < 0:
            raise ValueError("Число мест на кухне должно быть неотрицательным")
        self.count_sits = count_sits

    def stop_start_tech(self, name: str) -> None:
        """
        Включение или отключение техники

        :param name: Название техники

        Примеры:

        """
        ...
        if not isinstance(name, str):
            raise TypeError("Название техники должно быть типа str")
        if name not in self.tech:
            raise ValueError("Такой техники нет на кухне")

    def invite_friend(self, count_friends: int):
        """
        Приглашение людей в гости на кухню

        :param count_friends: Число приглашаемых

        Примеры:

        """
        ...
        if not isinstance(count_friends, int):
            raise TypeError("Число приглашенных должно быть типа int")
        if count_friends > self.count_sits:
            raise ValueError("На кухне не достаточно места")
        if count_friends <= 0:
            raise ValueError("Число приглашенных должно быть положительным")

    def clean(self, name: str):
        """
        Чистка техники

        :param name: Название техники

        Примеры:

        """
        ...
        if not isinstance(name, str):
            raise TypeError("Название техники должно быть типа str")

        if name not in self.tech:
            raise ValueError("Такой техники нет на кухне")


class Lego:

    def __init__(self, count: int, universe: str, length_object: float = 0, weight_object: float = 0):
        """
        Подготовка и создание объекта 'Lego'

        :param count: Число блоков (деталей)
        :param universe: К какой вселенной (тематике) относится конструктор
        :param lenght_object: Длина собранного конструктора
        :param weight_object: Ширина собранного конструктора

        Примеры:

        """
        if not isinstance(count, int):
            raise TypeError("Число блоков должно быть типа int")
        if count <= 0:
            raise ValueError("Число блоков должно быть положительным")
        self.count = count
        if not isinstance(universe, str):
            raise TypeError("Тема лего должна быть типа str")
        self.universe = universe
        if not isinstance(length_object, float):
            raise TypeError("Длина постройки должна быть типа float")
        if length_object < 0:
            raise ValueError("Длина постройки должна быть неотрицательной")
        self.length_object = length_object
        if not isinstance(weight_object, float):
            raise TypeError("Ширина постройки должна быть типа float")
        if weight_object < 0:
            raise ValueError("Ширина постройки должна быть неотрицательной")
        self.weight_object = weight_object

    def build(self, length: float, weight: float) -> tuple:
        """
        Сборка конструктора

        :param length: Увеличение длины сборки на length
        :param weight: Увеличение ширины сборки на weight
        :return: Кортеж новой длины и ширины сборки

        Примеры:

        """
        ...
        if not isinstance(length, float):
            raise TypeError("Длина постройки должна быть типа float")
        if length <= 0:
            raise ValueError("Длина постройки должна быть положительной")
        if not isinstance(weight, float):
            raise TypeError("Ширина постройки должна быть типа float")
        if weight <= 0:
            raise ValueError("Ширина постройки должна быть положительной")
        return (self.length_object, self.weight_object)

    def destroy(self, length: float, weight: float) -> tuple:
        """
        Разборка конструктора

        :param length: Уменьшение длины сборки на length
        :param weight: Уменьшение ширины сборки на weight
        :return: Кортеж новой длины и ширины сборки
        """
        ...
        if not isinstance(length, float):
            raise TypeError("Длина разборки должна быть типа float")
        if length <= 0:
            raise ValueError("Длина разборки должна быть положительной")
        if self.length_object < length:
            raise ValueError("Длина разборки должна быть меньше или равна собранной конструкции")
        if not isinstance(weight, float):
            raise TypeError("Ширина разборки должна быть типа float")
        if weight <= 0:
            raise ValueError("Ширина разборки должна быть положительной")
        if self.weight_object < weight:
            raise ValueError("Ширина разборки должна быть меньше или равна собранной конструкции")
        return (self.length_object, self.weight_object)

    def create_block(self, add_count: int) -> None:
        """
        Создание/закупка новых блоков (деталей)

        :param add_count: Число новых блоков (деталей)

        Примеры:

        """
        self.count += add_count


if __name__ == '__main__':
    doctest.testmod()
