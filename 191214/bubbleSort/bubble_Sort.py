

def bubble_sort(seq):
    n = len(seq)
    for j in range(n-1):
        i = 0
        while i < n-j-1:
            if seq[i] > seq[i+1]:
                seq[i], seq[i+1] = seq[i+1], seq[i]
            i += 1


s = [5, 9, 2, 4, 10, 3, 0, -1, 100, 34]
print(s)
bubble_sort(s)
print(s)
