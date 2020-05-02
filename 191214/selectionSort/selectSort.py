
def select_sort(seq):
    n = len(seq)
    for j in range(0, n-1):
        i = j
        min_value = seq[i]
        min_idx = i
        while i < n-1:
            if min_value > seq[i+1]:
                min_value = seq[i+1]
                min_idx = i + 1
            i += 1
        seq[j], seq[min_idx] = seq[min_idx], seq[j]


s = [5, 9, 2, 4, 10, 3, 0, -1, 100, 34]
print(s)
select_sort(s)
print(s)

