def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    i = 0
    h = high

 
    while low <= high:
 
        i =+ 1
        mid = (high + low) // 2

 
        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            
            low = mid + 1
 
        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > x:
            h = arr[mid]
            high = mid - 1
 
        # інакше x присутній на позиції і повертаємо його
        else:
            return [i,arr[mid]]
 
    # якщо елемент не знайдений
    return [i,h]


if __name__ == "__main__":
    arr = [2.1, 3.2, 4.3, 10.4, 21.1, 32.2, 34.3, 40.4, 40.5]
    x = 34
    print(binary_search(arr, x))
   
