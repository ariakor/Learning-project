# Реализация односвязного списка - один объект ссылается на следующий и так по цепочке до последнего. 
# Методы: добавление объекта в конец списка, извлечение последнего объекта и его удаление, получение списка из объектов односвязного списка.

class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        if type(next) == StackObj or next is None:
            self.__next = next

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data


class Stack:

    def __init__(self):
        self.top = None
        self.last = None

    def push(self, obj):
        if self.top is None:
            self.top = obj
            self.last = obj
            return
        if self.last:
            self.last.next = obj
            self.last = obj

        if self.last is None:
            self.top = None


    def pop(self):
        last = self.last
        top = self.top
        if top is last:
            self.top = None
            return top
        if top:
            while top.next != self.last:
                top = top.next
            top.next = None
            self.last = top
            return last

    def get_data(self):
        s = []
        top = self.top
        while top:
            s.append(top.data)
            top = top.next
        return s


# тесты для проверки стек-подобной структуры
s = Stack()
top = StackObj("obj_1")
s.push(top)
s.push(StackObj("obj_2"))
s.push(StackObj("obj_3"))
s.pop()

res = s.get_data()
assert res == ["obj_1", "obj_2"], f"метод get_data вернул неверные данные: {res}"
assert s.top == top, "атрибут top объекта класса Stack содержит неверное значение"

h = s.top
while h:
    res = h.data
    h = h.next

s = Stack()
top = StackObj("obj_1")
s.push(top)
s.pop()
assert s.get_data() == [], f"метод get_data вернул неверные данные: {s.get_data()}"

n = 0
h = s.top
while h:
    h = h.next
    n += 1

assert n == 0, "при удалении всех объектов, стек-подобная стурктура оказалась не пустой"

s = Stack()
top = StackObj("name_1")
s.push(top)
obj = s.pop()
assert obj == top, "метод pop() должен возвращать удаляемый объект"
