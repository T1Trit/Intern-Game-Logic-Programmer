python
def is_even_modulo(value):
  """
  Проверяет, является ли целое число четным, используя оператор остатка от деления.

  Args:
    value: Целое число для проверки.

  Returns:
    True если число четное, иначе False.
  """
  return value % 2 == 0

# Пример использования
print(is_even_modulo(4))  # Output: True
print(is_even_modulo(5))  # Output: False
