import sys
import random
import heap

def test_with_heap(size):
    priority_queue = heap.Heap()
    for i in range(size):
        rand = random.randint(1, size)
        priority_queue.push(rand)

    top10 = [priority_queue.pop() for _ in range(10)]
    print("Top 10 (with heap):", top10)

def test_with_sort(size):
    data = []
    for i in range(size):
        rand = random.randint(1, size)
        data.append(i)
    sorted_data = sorted(data, reverse=True)
    top10 = sorted_data[0:10]
    print("Top 10 (with sort):", top10)

def test_with_max(size):
    data = []
    for i in range(size):
        rand = random.randint(1, size)
        data.append(i)

    top10 = []
    for i in range(10):
        m = max(data)
        data.remove(m)
        top10.append(m)

    print("Top 10 (with sort):", top10)

if __name__ == "__main__":
    size = 1000000
    if sys.argv[1] == 'heap':
        test_with_heap(size)
    if sys.argv[1] == 'sort':
        test_with_heap(size)
    if sys.argv[1] == 'max':
        test_with_heap(size)

