def ratfood(r, unit, arr, n):
    # edge case
    if r is None or n == 0:
        return -1

    totalfood = r * unit
    current_sum = 0

    for i in range(n):
        current_sum += arr[i]

        if current_sum >= totalfood:
            return i + 1

    return 0


if __name__ == "__main__":
    r = 7
    unit = 2
    arr = [2, 8, 3, 5, 7, 4, 1, 2]
    n = len(arr)

    result = ratfood(r, unit, arr, n)
    print(result)