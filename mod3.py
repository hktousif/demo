from collections import defaultdict


def dict(A, B):
    A_dict = defaultdict(list)
    for i, word in enumerate(A):
        A_dict[word].append(i + 1)
    for j in B:
        if j in A_dict:
            print(' '.join([str(t) for t in A_dict[j]]))
        else:
            print("-1")


if __name__ == "__main__":
    n, m = map(int, input().split())
    A = [input() for _ in range(n)]
    B = [input() for _ in range(m)]
    dict(A, B)
