###hakerank questions
# #1.Compare the Triplets------------------------------------------------------------------

#!/bin/python3
import math
import os
import random
import re
import sys
# Complete the 'compareTriplets' function below.
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
def compareTriplets(a, b):
    # Write your code here
    for i in range(3):
        if a[i] > b[i]:
            alice =alice+1
        elif a[i] < b[i]:
            bob = bob+1
    return [alice, bob]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    result = compareTriplets(a, b)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()

# #2.aVeryBigSum---------------------------------------------------------------------------

#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'aVeryBigSum' function below.
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY ar as parameter.
def aVeryBigSum(ar):
    # Write your code here
    return sum(ar)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    ar_count = int(input().strip())
    ar = list(map(int, input().rstrip().split()))
    result = aVeryBigSum(ar)
    fptr.write(str(result) + '\n')
    fptr.close()

# #3.Diagonal Difference----------------------------------------------------------------------

#!/bin/python3
import math
import os
import random
import re
import sys
# Complete the 'diagonalDifference' function below.
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
def diagonalDifference(arr):
    # Write your code here
    n = len(arr)
    sum1 = 0
    sum2 = 0
    for i in range(len(arr)):
        sum1 = sum1 + arr[i][i]
        sum2 = sum2 + arr[i][n - 1 - i]
    res = abs(sum1 - sum2)
    return res
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(arr)
    fptr.write(str(result) + '\n')
    fptr.close()

# #4.Plus Minus ---------------------------------------------------------------------------
#!/bin/python3
import math
import os
import random
import re
import sys
# Complete the 'plusMinus' function below.
# The function accepts INTEGER_ARRAY arr as parameter.
def plusMinus(arr):
    # Write your code here
    n = len(arr)
    positive = 0
    negative = 0
    zero = 0
    for i in range(n):
        if arr[i] > 0:
            positive=positive + 1
        elif arr[i] < 0:
            negative=negative+1
        else:
            zero=zero+1
    print("{:.6f}".format(positive / n))
    print("{:.6f}".format(negative / n))
    print("{:.6f}".format(zero / n))
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)

# #5.---------------------------------------------------------------------------







