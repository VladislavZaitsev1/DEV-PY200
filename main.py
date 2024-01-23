# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
from typing import Union

class Horsehouse:
    def __init__(self, stalls: int, horses_in_stalls: int ):
        if not isinstance(stalls, int):
            raise TypeError('Ошибка типа! Параметр должен быть int')
        if stalls < 0:
            raise ValueError('Количество стоил не может быть отрицательным')
        self.stalls = stalls

        if not isinstance(horses_in_stalls, int):
            raise TypeError('Ошибка типа! Параметр должен быть int')
        if horses_in_stalls < 0:
            raise ValueError('Количество  лошадей в стойлах не может быть отрицательным')
        self.stalls = stalls
        self.horses = horses_in_stalls

    def add_horses_to_stalls(self, add_horses: int) -> None:
        """
        Добавление лошадей в стойла.
        :param add_horses: Количество добавляемых лошадей

        :raise ValueError: Если количество добавляемых лошадей больше свободных стоил, то вызываем ошибку

        Примеры:
        >>> horsehouse = Horsehouse(10, 0)
        >>> horsehouse.add_horses_to_stalls(7)
        """
        if not isinstance(add_horses, int):
            raise TypeError("Добавляемые лошади должны быть типа int")
        if add_horses < 0:
            raise ValueError("Добавляемые лошади должны быть больше 0")

    def remove_horses_from_stalls(self, remove_horses: int) -> None:
        """
        Удаление лошадей из стойла

        :param remove_horses: Количество удаляемых лошадей
        :raise ValueError: Если количество лошадей превышает количество стоил,
        то возвращается ошибка.

        :return: Количество удаленных лошадей

        Примеры:
        >>> horsehouse = Horsehouse(10, 0)
        >>> horsehouse.remove_horses_from_stalls(7)
        """


class Parking:
    def __init__(self, free_packing_places: int, full_parking_places: int):
        if not isinstance(free_packing_places, int):
            raise TypeError('Ошибка типа! Параметр должен быть int')
        if free_packing_places < 0:
            raise ValueError('Количество свободных парковочных мест не может быть отрицательным')

        if not isinstance(full_parking_places, int):
            raise TypeError('Ошибка типа! Параметр должен быть int')
        if full_parking_places < 0:
            raise ValueError('Количество занятых мест не может быть отрицательным')
        self.free_packing_places = free_packing_places
        self.full_parking_places = full_parking_places

    def add_cars_to_parking(self, add_cars: int) -> None:
        """
        Добавление машин на парковку.
        :param add_cars: Количество добавляемых машин

        :raise ValueError: Если количество добавляемых машин больше мест, то вызываем ошибку

        Примеры:
        >>> parking = Parking(10, 0)
        >>> parking.add_cars_to_parking(10)
        """
        if not isinstance(add_cars, int):
            raise TypeError("Занятые парковочные местадолжны быть типа int")
        if add_cars < 0:
            raise ValueError("Занятые парковочные местадолжны быть больше 0")

    def remove_cars_from_parking(self, remove_cars: int) -> None:
        """
        Удаление машин с парковки

        :param remove_cars: Количество удаляемых машин
        :raise ValueError: Если количество уехавших машин превышает количество парковочных мест,
        то возвращается ошибка.

        :return: Количество уехавших машин

        Примеры:
        >>> parking = Parking(10, 10)
        >>> parking.remove_cars_from_parking(7)
        """

class Scales:
    def __init__(self, max_weight: Union[int, float], weight_now: Union[int, float]):
        if not isinstance(max_weight, (int, float)):
            raise TypeError('Ошибка типа! Параметр должен быть int или float')
        if max_weight <= 0:
            raise ValueError('Максимальный вес, который выдерживают весы должен быть положительным')

        if not isinstance(weight_now, (int, float)):
            raise TypeError('Ошибка типа! Параметр должен быть int или float')
        if weight_now < 0:
            raise ValueError('Вес, положенный на весы, не может быть отрицательным')
        self.max_weight = max_weight
        self.weight_now = weight_now

    def add_weight_to_scales(self, add_weight: Union[int, float]) -> None:
        """
        Добавление веса на весы.
        :param add_weight: Количество добавляемого веса

        :raise ValueError: Если масса, добавляемая на весы, больше максимально допустимой,
         то вызываем ошибку

        Примеры:
        >>> scales = Scales(100, 50)
        >>> scales.add_weight_to_scales(40)
        """
        if not isinstance(add_weight, (int, float)):
            raise TypeError("Добавляемые вес должен быть int или float'")
        if add_weight < 0:
            raise ValueError("Добавляемый вес долже быть больше 0")

    def remove_weight_from_scales(self, remove_weight: Union[int, float]) -> None:
        """
        Удаление веса с весов

        :param remove_weight: Вес, удаляемый с весов
        :raise ValueError: Если масса, удаляемая с весов больше, чем масса, которая была на весах
        то возвращается ошибка.

        :return: Удаляемая с весов масса

        Примеры:
        >>> scales = Scales(100, 50)
        >>> scales.remove_weight_from_scales(45)
        """

if __name__ == "__main__":
    doctest.testmod()