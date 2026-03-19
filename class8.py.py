#Given an array of integers nums and an integer 
# target, return indices of the two numbers such that they
#  add up to target.
#You may assume that each 
# input would have exactly one solution,
#  and you may not use the same element twice.
#You can return the answer in any order.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans=[]
        for i in range(len(nums)-1):
            for j in range (i+1,len(nums)):
             if nums[i]+nums[j]==target:
                return [i,j]

                #Given an array nums. We define a running sum of an
#  array as runningSum[i] = sum(nums[0]…nums[i]).
#Return the running sum of nums.

class Solution:
    def runningSum(self, nums):
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums

        #Given an integer n, return a string array answer (1-indexed) where:

#answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
#answer[i] == "Fizz" if i is divisible by 3.
#answer[i] == "Buzz" if i is divisible by 5.
#answer[i] == i (as a string) if none of the above conditions are true.

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans=[]
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                ans.append('FizzBuzz')
            elif i%3==0:
                ans.append('Fizz')
            elif i%5==0:
                ans.append("Buzz")
            else:
             ans.append(str(i))
        return ans