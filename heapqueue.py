from typing import List, Tuple, Any


class MinHeap:
    def __init__(self):
        self.heap: List[Tuple[float, Any]] = []

    def push(self, item: Tuple[float, Any]) -> None:
        self.heap.append(item)
        self._bubble_up(len(self.heap) - 1)

    def pop(self) -> Tuple[float, Any]:
        if not self.heap:
            raise IndexError("pop from empty heap")

        if len(self.heap) == 1:
            return self.heap.pop()

        min_item = self.heap[0]

        self.heap[0] = self.heap.pop()

        self._bubble_down(0)

        return min_item

    def _bubble_up(self, index: int) -> None:
        parent_index = (index - 1) // 2

        if index == 0 or self.heap[parent_index] <= self.heap[index]:
            return

        self.heap[index], self.heap[parent_index] = (
            self.heap[parent_index],
            self.heap[index],
        )

        self._bubble_up(parent_index)

    def _bubble_down(self, index: int) -> None:
        size = len(self.heap)
        smallest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2

        if left_child < size and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child

        if right_child < size and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child

        if smallest != index:
            self.heap[index], self.heap[smallest] = (
                self.heap[smallest],
                self.heap[index],
            )

            self._bubble_down(smallest)

    def __len__(self) -> int:
        return len(self.heap)

    def __bool__(self) -> bool:
        return len(self.heap) > 0


def heappush(heap: MinHeap, item: Tuple[float, Any]) -> None:
    heap.push(item)


def heappop(heap: MinHeap) -> Tuple[float, Any]:
    return heap.pop()
