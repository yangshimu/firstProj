import random


def stack_empty(s):
    if len(s) == 0:
        return True
    else:
        return False


def push(s, key):
    s.append(key)


def pop(s):
    assert stack_empty(s) is False
    x = s[-1]
    s.pop()
    return x


s1 = [random.randint(-100, 200) for _ in range(10)]
print(s1)
print(stack_empty(s1))
push(s1, 0)
print(s1)
x = pop(s1)
print(s1, x)
