heap = [0]
while True:
    num = int(input())
    if num == -1:
        break
    elif num == 0:
        print(heap[1])
        heap[1] = heap[len(heap)-1]
        heap.pop()
        idx = 1
        left = 2
        right = 3
        while idx <= (len(heap)-1)//2:
            smallidx = left
            if right <= len(heap)-1 and heap[right] < heap[left]:
                smallidx = right
            if heap[idx] > heap[smallidx]:
                heap[idx], heap[smallidx] = heap[smallidx], heap[idx]
            idx = smallidx
            left = 2 * idx
            right = 2 * idx + 1
    else:
        heap.append(num)
        idx = len(heap) - 1
        while idx != 1 and heap[idx//2] > num:
            heap[idx//2], heap[idx] = heap[idx], heap[idx//2]
            idx = idx // 2
