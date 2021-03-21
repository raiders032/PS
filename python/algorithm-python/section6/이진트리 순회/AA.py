def preOrder(idx):
    if idx > N:
        return
    print(arr[idx], end=' ')
    preOrder(2 * idx)
    preOrder(2 * idx + 1)


def inOrder(idx):
    if idx > N:
        return
    inOrder(2 * idx)
    print(arr[idx], end=' ')
    inOrder(2 * idx + 1)


def postOrder(idx):
    if idx > N:
        return
    postOrder(2 * idx)
    postOrder(2 * idx + 1)
    print(arr[idx], end=' ')


arr = [x for x in range(8)]
N = len(arr) - 1
preOrder(1)
print()
inOrder(1)
print()
postOrder(1)
