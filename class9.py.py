#9. Palindrome Number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        original = x
        reversed_num = 0
        
        while x != 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10
        
        return original == reversed_num


        # Given a time in 12-hour AM/PM format,
# convert it to military (24-hour) time.

# Note:
# - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
def timeConversion(s):
    # Separate the string into parts
    hour = s[:2]               # Example: "07"
    minutes_seconds = s[2:8]   # Example: ":05:45"
    meridiem = s[8:]           # Example: "PM"

    if meridiem == "AM":
        if hour == "12":
            hour = "00"
    else: # It is PM
        if hour != "12":
            # Add 12 to the hour (e.g., "07" becomes "19")
            hour = str(int(hour) + 12)
            
    return hour + minutes_seconds

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()



# You are given a 2D list (accounts) where:
# - Each row represents a customer
# - Each column represents money in a specific bank

# Goal:
# Find the maximum total wealth among all customers

# Approach:
# 1. For each customer (row), calculate the sum of all bank balances
# 2. Compare each customer's total wealth
# 3. Return the maximum wealth found

from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = []
        
        for i in accounts:
            total = 0
            for j in range(len(i)):
                total += i[j]
            wealth.append(total)
        
        return max(wealth)


        # You have been given an array A of size
#  N consisting of positive integers.
# You need to find and print the product
#  of all the number in this array Modulo (10^9 + 7).

n = int(input())
arr = list(map(int, input().split()))

mod = 10**9 + 7
result = 1

for num in arr:
    result = (result * num) % mod

print(result)


# This is a staircase of size N.
# Its base and height are both equal to N.
# It is drawn using # symbols and spaces.
# The last line is not preceded by any spaces.

if __name__ == '__main__':
    n = int(input())

    for i in range(1, n + 1):
        print(" " * (n - i) + "#" * i)



        # Given five positive integers,
# find the minimum and maximum values that can be calculated
# by summing exactly four of the five integers.
# Then print the respective minimum and maximum values
# as a single line of two space-separated long integers.

def miniMaxSum(arr):
    total = sum(arr)
    min_sum = total - max(arr)
    max_sum = total - min(arr)
    print(min_sum, max_sum)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)


    # You are in charge of the cake for a child's birthday.
# It will have one candle for each year of their total age.
# They will only be able to blow out the tallest of the candles.
# Your task is to count how many candles are the tallest.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
