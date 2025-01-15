def is_even_bitwise(value):
  """
  Проверяет, является ли целое число четным, используя побитовую операцию И.

  Args:
    value: Целое число для проверки.

  Returns:
    True если число четное, иначе False.
  """
  return (value & 1) == 0

# Пример использования
print(is_even_bitwise(4))  # Output: True
print(is_even_bitwise(5))  # Output: False
