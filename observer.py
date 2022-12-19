from abc import ABC, abstractmethod


# Cистема наблюдения
class CameraSystem:

    def __init__(self):
        self.__observers = set()

    # Подключить камеру к системе
    def connect(self, observer):
        self.__observers.add(observer)

    # Отключить камеру от системы
    def disconnect(self, observer):
        self.__observers.remove(observer)

    # Отправка команды всем подключенным камерам
    def alert(self):
        for observer in self.__observers:
            observer.make_photo()


# Абстрактный класс наблюдателя
class AbstractObserver(ABC):
    @abstractmethod
    def make_photo(self):  # Абстрактный наблюдатель задает метод make_photo
        pass


# Камера наблюдения
class Camera(AbstractObserver):

    def __init__(self, name):
        self.name = name

    def make_photo(self):
        print(f'{self.name} сделала фото')


# Камеры
cam1 = Camera('Камера №1')
cam2 = Camera('Камера №2')
cam3 = Camera('Камера №3')

# Создание системы камер
cam_system = CameraSystem()

# Подключние камер к системе
cam_system.connect(cam1)
cam_system.connect(cam2)
cam_system.connect(cam3)

# Команда всем подключенным камерам, о том что что-то произошло и нужно сделать фото
cam_system.alert()
