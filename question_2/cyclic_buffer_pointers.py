class CyclicBufferFIFO_Pointers:
    def __init__(self, capacity):
        """
        Инициализирует циклический буфер заданной ёмкости.

        Args:
            capacity: Максимальное количество элементов, которое может хранить буфер.
        """
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.head = 0  # Указатель на следующий элемент для чтения
        self.tail = 0  # Указатель на следующую позицию для записи
        self.size = 0  # Текущее количество элементов в буфере

    def enqueue(self, item):
        """Добавляет элемент в хвост буфера."""
        if self.size == self.capacity:
            raise OverflowError("Buffer is full")
        self.buffer[self.tail] = item
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1

    def dequeue(self):
        """Удаляет и возвращает элемент из головы буфера."""
        if self.size == 0:
            raise IndexError("Buffer is empty")
        item = self.buffer[self.head]
        self.buffer[self.head] = None  # Опционально: очистить удаленный элемент
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return item

    def is_empty(self):
        """Проверяет, пуст ли буфер."""
        return self.size == 0

    def is_full(self):
        """Проверяет, полон ли буфер."""
        return self.size == self.capacity
    
    def __len__(self):
        """
        Возвращает текущий размер буфера
        """
        return self.size
