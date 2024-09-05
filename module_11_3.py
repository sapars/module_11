'''
Необходимо создать функцию, которая принимает объект (любого типа) в качестве аргумента и
проводит интроспекцию этого объекта, чтобы определить его тип, атрибуты, методы, модуль, и другие свойства.

1. Создайте функцию introspection_info(obj), которая принимает объект obj.
2. Используйте встроенные функции и методы интроспекции Python для получения информации о переданном объекте.
3. Верните словарь или строки с данными об объекте, включающий следующую информацию:
  - Тип объекта.
  - Атрибуты объекта.
  - Методы объекта.
  - Модуль, к которому объект принадлежит.
'''


def introspection_info(obj):
    info = {
        'type': type(obj),
        'attributes': dir(obj),
        'methods': [method for method in dir(obj) if callable(getattr(obj, method))],
        'module': type(obj).__module__

    }
    return info


class MyClass:
    def method1(self):
        pass

    def method2(self, x):
        pass


info = introspection_info(MyClass)
for i in info:
    print(i, info[i])

