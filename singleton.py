class Singleton:  # позволяет создавать один экземпляр класса
    __instance = None  # приватная переменная

    def __new__(cls, *args, **kwargs):  # cls = class, это наш класс
        if cls.__instance is None:
            cls.__instance = super(Singleton, cls).__new__(cls)
        return cls.__instance


# проверка

obj1 = Singleton()
obj2 = Singleton()

print(f'{obj1 is obj2}\n {obj1}\n {obj2}')
