from collections import deque

class CyclicBufferFIFO_Deque:
    def __init__(self, capacity):
        """
        Инициализирует циклический буфер заданной ёмкости.

        Args:
            capacity: Максимальное количество элементов, которое может хранить буфер.
        """
        self.capacity = capacity
        self.buffer = deque(maxlen=capacity)

    def enqueue(self, item):
        """Добавляет элемент в буфер. Если буфер полон, перезаписывает самый старый элемент."""
        if self.is_full():
            self.buffer.popleft()
        self.buffer.append(item)

    def dequeue(self):
        """Удаляет и возвращает самый старый элемент из буфера."""
        if not self.buffer:
            raise IndexError("Buffer is empty")
        return self.buffer.popleft()

    def is_empty(self):
        """Проверяет, пуст ли буфер."""
        return len(self.buffer) == 0

    def is_full(self):
        """Проверяет, полон ли буфер."""
        return len(self.buffer) == self.capacity
    
    def __len__(self):
        """
        Возвращает текущий размер буфера
        """
        return len(self.buffer)
