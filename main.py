bracked_list = [
    '(((([{}]))))',
    '[([])((([[[]]])))]{()}',
    '{{[()]}}',
    '}{}',
    '{{[(])]}}',
    '[[{())}]']


class Stack(list):
    def is_empty(self):
        return len(self) == 0

    def push(self, _item):
        self.append(_item)

    def pop(self):
        if not self.is_empty():
            _item = self[-1]
            self.__delitem__(-1)
        return _item

    def peek(self):
        if not self.is_empty():
            return self[-1]

    def size(self):
        return len(self)


def check_ballance(brackeds_string):
    stack = Stack()
    for item in brackeds_string:
        if item in '([{':

            stack.push(item)
        elif item == ')' and stack.peek() == '(':
            stack.pop()
        elif item == '}' and stack.peek() == '{':
            stack.pop()
        elif item == ']' and stack.peek() == '[':
            stack.pop()
        else:
            return 'Несбалансированно'
    if stack.is_empty():
        return 'Сбалансированно'
    else:
        return 'Несбалансированно'


if __name__ == '__main__':
    for list_item in bracked_list:
        print(list_item, '-->', check_ballance(list_item))
