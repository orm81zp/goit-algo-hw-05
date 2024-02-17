def binary_upper_limit_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    iterations = 0
    upper_limit = arr[high]

    # [1.1, 1.3, 2.5, 3.8, 4.6, 5.9]

    while low <= high:
        iterations += 1
        mid = (high + low) // 2

        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            low = mid + 1

        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > x:
            high = mid - 1
            upper_limit = min(arr[mid:])

        # інакше x присутній на позиції і повертаємо його
        else:
            return (iterations, x)

    # якщо елемент не знайдений
    return (iterations, upper_limit)
