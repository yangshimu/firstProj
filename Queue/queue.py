import random


def enqueue(s, key):
    s.append(key)


def dequeue(s):
    assert len(s) > 0
    return s.pop(0)


s1 = [random.randint(-100, 200) for _ in range(10)]
print(s1)
enqueue(s1, 0)
print(s1)
x = dequeue(s1)
print(s1, x)
