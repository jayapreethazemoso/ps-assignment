def determine_winner(n, arr):
    total_sum = sum(arr)
    if total_sum % 2 == 0:
        return "Alice"
    else:
        return "Bob"
n = 5
arr = [1, 2, 3, 4, 5]
print(determine_winner(n, arr))
