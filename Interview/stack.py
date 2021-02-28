class Stack:
    '''
    Стек - абстрактный тип данных, представляющий собой список элементов, организованных по принципу LIFO
    (англ. last in — first out, «последним пришёл — первым вышел»). Чаще всего принцип работы стека сравнивают
    со стопкой тарелок: чтобы взять вторую сверху, нужно снять верхнюю. Или с магазином в огнестрельном
    оружии(стрельба начнётся с патрона, заряженного последним).
    '''

    def __init__(self):
        self.elements = []

    def isEmpty(self):
        '''проверка стека на пустоту. Метод возвращает True или False.'''
        if self.size() == 0:
            return True

        return False

    def push(self, elem):
        '''добавляет новый элемент на вершину стека. Метод ничего не возвращает.'''
        self.elements.insert(0, elem)

    def pop(self):
        '''удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека'''
        return self.elements.pop(0)

    def peek(self):
        ''' возвращает верхний элемент стека, но не удаляет его. Стек не меняется.'''
        if self.isEmpty():
            raise Exception("Стек пуст!")
        return self.elements[0]

    def size(self):
        '''возвращает количество элементов в стеке.'''
        return len(self.elements)

    def balance(self, text):
        '''Программа ожидает на вход строку со скобками. На выход сообщение: "Сбалансированно",
        если строка корректная, и "Несбалансированно", если строка составлена неверно.'''
        opening = ['(', '[', '{']
        closing = [')', ']', '}']
        for el in text:
            if el in opening:
                self.elements.insert(opening)
        if self.size() % 2 != 0:
            return 'Несбалансированно'
        for el in stack:



if __name__ == '__main__':
    stack = Stack()
    stack.push(2)
    stack.push('a')
    stack.push('kfnskdjngjfdgjdf')
    print(stack.peek())



'''
статьи полезные по теме:

http://espressocode.top/check-for-balanced-parentheses-in-an-expression/
https://ru.stackoverflow.com/questions/587694/%d0%9f%d1%80%d0%be%d0%b2%d0%b5%d1%80%d0%b8%d1%82%d1%8c-%d0%bf%d1%80%d0%b0%d0%b2%d0%b8%d0%bb%d1%8c%d0%bd%d0%be-%d0%bb%d0%b8-%d0%b2%d0%bb%d0%be%d0%b6%d0%b5%d0%bd%d1%8b-%d1%81%d0%ba%d0%be%d0%b1%d0%ba%d0%b8-%d0%b2-%d1%82%d0%b5%d0%ba%d1%81%d1%82%d0%b5
https://overcoder.net/q/1042471/%D1%80%D0%B5%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F-%D1%81%D1%82%D0%B5%D0%BA%D0%B0-%D1%81-%D0%BF%D0%BE%D0%BC%D0%BE%D1%89%D1%8C%D1%8E-python
'''