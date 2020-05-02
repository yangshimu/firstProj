import collections



S="asgsdgdasd"

print(S.__contains__('agsd'))


print(dict(collections.Counter(S)))


print([i for i, e in enumerate(S, start=3)])

