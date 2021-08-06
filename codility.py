def stars(num_rows):
    for row in range(1, num_rows + 1):
        s = " " * (row - 1) + "*" * (2 * num_rows - (1 + 2 * (row - 1)))
        print(s)


def fibonacci(n):
    numbers = [0, 1]
    next_number = 1
    while next_number <= n:
        numbers.append(next_number)
        next_number = numbers[-1] + numbers[-2]
    print(numbers)


def solution(N):
    binary_n = bin(N)
    zeros_ones = binary_n.split("b")[1].strip("0")
    gaps = zeros_ones.split("1")
    len_gaps = [len(gap) for gap in gaps]
    return max(len_gaps)


def rotation(a, k):
    new_a = []
    if len(a) in (0, 1, k) or k == 0:
        return a
    for i in range(k):
        new_a = [a[-1]] + a[0:-1]
        a = new_a
    return new_a


def find_unpaired(numbers):
    if len(numbers) == 1:
        return numbers[0]
    numbers.sort()
    total = len(numbers)
    for i, num in enumerate(numbers):
        if i == 0:
            edge, len_num = numbers[0], 1
            continue
        if num != edge:
            if len_num % 2 != 0:
                return edge
            edge = num
            len_num = 0
        len_num += 1
        if i == (total - 1) and len_num % 2 != 0:
            return num


def missing_element(arr):
    n = len(arr) + 1
    expected_sum = int(n * (n + 1) / 2)
    arr_sum = sum(arr)
    return expected_sum - arr_sum


def site_host():
    for i in range(1, 101):
        s = ""
        if i % 3 == 0:
            s += "Site"
        if i % 5 == 0:
            s += "Host"
        elif i % 3 != 0:
            s = i
        print(s)


def tape_equilibrium(arr):
    arr_len = len(arr)
    sum_first = arr[0]
    sum_second = sum(arr) - arr[0]
    min_diff = abs(sum_second - sum_first)
    for i in range(1, arr_len - 1):
        sum_first += arr[i]
        sum_second -= arr[i]
        diff = abs(sum_second - sum_first)
        if diff < min_diff:
            min_diff = diff
    return min_diff


def frog_jump(X, A):
    if not X in A:
        return -1
    earliest_times = [""] * X
    for i in range(len(A)):
        if earliest_times[A[i] - 1] == "":
            earliest_times[A[i] - 1] = i
    if "" in earliest_times:
        return -1
    return max(earliest_times)


def permutation(A):
    n = len(A)
    expected_sum = n * (n + 1) / 2
    if sum(A) != expected_sum:
        return 0
    num_times = [0] * (n + 1)
    for i in range(n):
        if A[i] > n:
            return 0
        num_times[A[i]] += 1
    if max(num_times) == 1 and sum(num_times) == n:
        return 1
    return 0


def prefix_sums(arr):
    n = len(arr)
    p = [0] * (n + 1)
    for k in range(1, n + 1):
        p[k] = p[k - 1] + arr[k - 1]
    return p


def count_total(p, x, y):
    return p[y + 1] - p[x]


def mushrooms(arr, k, m):
    n = len(arr)
    result = 0
    pref = prefix_sums(arr)
    for p in range(min(m, k) + 1):
        left_pos = k - p
        right_pos = min(n - 1, max(k, k + m - 2 * p))
        result = max(result, count_total(pref, left_pos, right_pos))
    for p in range(min(m + 1, n - k)):
        right_pos = k + p
        left_pos = max(0, min(k, k - (m - 2 * p)))
        result = max(result, count_total(pref, left_pos, right_pos))
    return result


def passing_cars(A):
    n = len(A)
    if n > 1000000000:
        return -1
    pref = prefix_sums(A)
    res = 0
    for i, car in enumerate(A):
        if car == 0:
            res += count_total(pref, i, n - 1)
    return res


if __name__ == "__main__":
    print(passing_cars([0, 0]))
