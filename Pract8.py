# ID : 20CE048
# Name : Maharshi Limbachiya

# AIM:Write a Program in Python to implement a Stack Data Structure using Class and Objects, with push, pop, and traversal method.

# github repository link : https://github.com/Maharshi04/Python-Practical/blob/main/Pract8.py


class Stack:
    def __init__(self):
	    self.items = []

    def isEmpty(self):
	    return self.items == []

    def push(self, item):
	    self.items.insert(0, item)

    def pop(self):
	    return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
	    return len(self.items)

s = Stack()
s.push('hello')
s.push('true')
print(s.pop())