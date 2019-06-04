class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        #accepts an item as a param and appends it to the end of the list. and returns nothing.
        # O(1) runtime
        self.items.append(item)

    def pop(self):
        #removes the last time for the list, which is also the top item
        #O(1) runtime
        return self.items.pop()

    def peek(self):
        # shows the last index in the list
        if self.items[-1]:
            return self.items[-1]
        return None

    def size(self):
        #removes the last time for the list, which is also the top item
        #O(1) runtime
        return len(self.items)

    def is_empty(self):
        return self.items == []


# print('type a paran: ')
# INPUT = input()

def balance(input):
    my_stack = Stack()

    symbol_pairs = {
        '(':')',
        '{':'}',
        '[':']'
    }

    openers = symbol_pairs.keys()

    for i in input:
        symbol = i

        if symbol in openers:
            my_stack.push(symbol)
        else:
            if my_stack.is_empty():
                return False
            else:
                top_item = my_stack.pop()
                if symbol != symbol_pairs(top_item):
                    return False
    if my_stack.is_empty():
        return True
    return False

print( balance([]) )
print( balance(['(][{']) )
print( balance(['()()']) )
