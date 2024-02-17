"""Перевірка роботи Алгоритму Хеш-Таблиця"""

from algorithms import HashTable

# створення хеш таблиці
hashTable = HashTable(5)

# вставка значень в таблицю
hashTable.insert("apple", 10)
hashTable.insert("orange", 20)

# Видалити значення "orange"
hashTable.delete("orange")

# вставлення нового значення в таблицю
hashTable.insert("pineapple", 101)

# виведення всіх значень з таблиці
print(hashTable) # "pineapple: 101, apple: 10" або "apple: 10, pineapple: 101"
