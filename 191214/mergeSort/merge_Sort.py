
import math


def merge(seq, p, q, r):
    sub_seq1 = seq[p:q+1]
    sub_seq2 = seq[q+1:r+1]
    n1 = q-p+1
    n2 = r-q
    i = 0
    j = 0
    for k in range(r-p+1):
        if i < n1 and j < n2:
            if sub_seq1[i] <= sub_seq2[j]:
                seq[p+k] = sub_seq1[i]
                i += 1
            else:
                seq[p+k] = sub_seq2[j]
                j += 1
        elif i == n1 and j < n2:
            seq[p+k:r+1] = sub_seq2[j:]
            break
        elif i < n1 and j == n2:
            seq[p + k:r + 1] = sub_seq1[i:]
            break


def merge_sort(seq, p, r):
    if p < r:
        q = math.floor((p+r)/2)
        merge_sort(seq, p, q)
        merge_sort(seq, q+1, r)
        merge(seq, p, q, r)


s = [-1, 0, 2, 8, 23, 25, 0, 4, 34, 6]
merge_sort(s, 0, len(s)-1)
print(s)

