

def insert_sort(seq):
    n = len(seq)
    for j in range(1, n):
        key = seq[j]
        i = j-1
        while i >= 0 and seq[i] > key:
            seq[i+1] = seq[i]
            i = i-1
        seq[i+1] = key


a = [5, 1, 2, 9, 3, 8]
print(a)
insert_sort(a)
print(a)
