Observations:
Alice moves first and picks a number from the sequence.


The game ends when all numbers are removed.


Alice wins if the sum of her selected numbers is even, otherwise Bob wins.


Both players play optimally, meaning they will make moves that maximize their chance of winning.


Key Considerations:
The sum of the total sequence, S, before the game starts determines the possible outcomes:


If S is even, Alice can always ensure that her sum remains even.


If S is odd, no matter what, Alice will always start with an odd sum and be forced into an odd sum at the end.


Strategy:
If S (sum of the entire sequence) is even:


Alice can always pick numbers such that her sum remains even (by either picking even numbers or canceling out odd pairs).


Alice wins.


If S is odd:


No matter how optimally Alice plays, at some point, she will be forced to end with an odd sum.


Bob wins.


Conclusion:
If the sum of all numbers in the sequence is even, Alice wins.


If the sum of all numbers in the sequence is odd, Bob wins.
Python code Implementation:
def determine_winner(n, arr):
    total_sum = sum(arr)
    if total_sum % 2 == 0:
        return "Alice"
    else:
        return "Bob"
n = 5
arr = [1, 2, 3, 4, 5]
print(determine_winner(n, arr))  


Time Complexity : O(n).

