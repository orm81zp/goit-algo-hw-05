# Домашнє завдання 5

## Завдання 1

Додати метод `delete` для видалення пар ключ-значення таблиці HashTable, яка реалізована в конспекті.

### Виконання

Домашнє завдання виконано у файлі task_1.py.

### Приклад коду

```
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
```

## Завдання 2

Реалізувати двійковий пошук для відсортованого масиву з дробовими числами. Написана функція для двійкового пошуку повинна повертати кортеж, де першим елементом є кількість ітерацій, потрібних для знаходження елемента. Другим елементом має бути "верхня межа" — це найменший елемент, який є більшим або рівним заданому значенню.

### Виконання

Домашнє завдання виконано у файлі task_2.py.

Наступні параметри будуть використані за замовчуванням, якщо не було передано з командного рядку жодного:

-   набір даних: `[1.1, 1.3, 2.5, 3.8, 4.6, 5.9]`
-   пошуковий набір даних: `[3.5, 4, 6.0]`

### Приклад запуску програми

```
python task_2.py [набір даних, розділений комою] [набір пошукових значень, розділений комою]
```

```
python task_2.py
python task_2.py 1.1,1.3,2.5,3.8,4.6,5.9
python task_2.py 1.1,1.3,2.5,3.8,4.6,5.9 3.5,4,6.0
```

### Приклад роботи програми

Запуск програми

```
python task_2.py
```

Результат виконання

```
Набір даних: [1.1, 1.3, 2.5, 3.8, 4.6, 5.9]
Набір пошукових значень: [3.5, 4, 6.0]

Пошукове значення | Результат
3.5               | (3, 3.8)
4                 | (3, 4.6)
6.0               | (3, 5.9)
```

## Завдання 3

Порівняти ефективність алгоритмів пошуку підрядка: Боєра-Мура, Кнута-Морріса-Пратта та Рабіна-Карпа на основі двох текстових файлів [стаття 1](https://drive.google.com/file/d/18_R5vEQ3eDuy2VdV3K5Lu-R-B-adxXZh/view?usp=sharing), [стаття 2](https://drive.google.com/file/d/13hSt4JkJc11nckZZz2yoFHYL89a4XkMZ/view?usp=sharing). Використовуючи `timeit`, треба виміряти час виконання кожного алгоритму для двох видів підрядків: одного, що дійсно існує в тексті, та іншого — вигаданого (вибір підрядків за вашим бажанням). На основі отриманих даних визначити найшвидший алгоритм для кожного тексту окремо та в цілому.

### Виконання

Домашнє завдання виконано у файлі task_3.py.

Наступні параметри будуть використані за замовчуванням, якщо не було передано з командного рядку жодного:

-   пошуковий підрядок: `структури даних вже давно реалізовані`

### Приклад запуску програми

```
python task_3.py [пошуковий підрядок]
```

```
python task_3.py
python task_3.py Автори публiкації
```

### Приклад роботи програми

Запуск програми

```
python task_3.py
```

Результат виконання

```
Кількість спроб: 10
Набори даних: ['article1.txt', 'article2.txt']
Пошуковий підрядок: "структури даних вже давно реалізовані"

✓ Середній час:
Алгоритм Боєра-Мура: 0.000538
Алгоритм Рабіна-Карпа: 0.007327
Алгоритм Кнута-Морріса-Пратта: 0.003068

✓ Найшвидший алгоритм: Алгоритм Боєра-Мура
Алгоритм Боєра-Мура працює у 13.6 разів швидше ніж Алгоритм Рабіна-Карпа.
Алгоритм Боєра-Мура працює у 5.7 разів швидше ніж Алгоритм Кнута-Морріса-Пратта.
```

### Висновки

На основі отриманих даних можемо визначити найшвидший алгоритм, а саме **Алгоритм Боєра-Мура**, який працює у 13.6 разів швидше ніж Алгоритм Рабіна-Карпа та у 5.7 разів швидше ніж Алгоритм Кнута-Морріса-Пратта.
