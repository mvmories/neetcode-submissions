import heapq
from typing import List


def heapify_strings(strings: List[str]) -> List[str]:
    heap = heapq.heapify(strings)
    return heap


def heapify_integers(integers: List[int]) -> List[int]:
    heap = heapq.heapify(integers)
    return heap


def heap_sort(nums: List[int]) -> List[int]:
    heap = heapq.heapify(nums)
    return heap


# do not modify below this line
print(heapify_strings(["b", "a", "e", "c", "d"]))
print(heapify_integers([3, 4, 5, 1, 2, 6]))
print(heap_sort([3, 4, 5, 1, 2, 6]))
