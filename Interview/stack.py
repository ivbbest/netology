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
        self.elements.append(elem)

    def pop(self):
        '''удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека'''
        return self.elements.pop()

    def peek(self):
        ''' возвращает верхний элемент стека, но не удаляет его. Стек не меняется.'''
        if self.isEmpty():
            raise Exception("Стек пуст!")
        return self.elements[0]

    def size(self):
        '''возвращает количество элементов в стеке.'''
        return len(self.elements)

def balance(text):
    '''Программа ожидает на вход строку со скобками. На выход сообщение: "Сбалансированно",
    если строка корректная, и "Несбалансированно", если строка составлена неверно.'''
    opening = ['(', '[', '{']
    closing = [')', ']', '}']
    flag = True
    stack = Stack()

    for el in text:
        if el in opening:
            stack.push(el)

        elif el in closing:
            if stack.isEmpty():
                flag = False
                break

            elif el == ')':
                if stack.pop() != opening[0]:
                    flag = False
                    break

            elif el == ']':
                if stack.pop() != opening[1]:
                    flag = False
                    break

            elif el == '}':
                if stack.pop() != opening[2]:
                    flag = False
                    break

    if flag:
        return 'Сбалансированно'
    else:
        return 'Несбалансированно'


if __name__ == '__main__':

    with open('file.txt', encoding='UTF-8') as f:
        for line in f:
            info = balance(line.strip())
            print(f'Строка {line.strip()} является {info}й')