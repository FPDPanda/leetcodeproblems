import numpy as np


# 1 TwoSum (07.18.2020)
def twoSum(nums, target):
    for i, n1 in enumerate(nums):
        for j, n2 in enumerate(nums):
            if i == j:
                continue
            if n1 + n2 == target:
                return [i, j]


# 2 Kids With the Greatest Number of Candies (07.18.2020)
def kidsWithCandies(candies, extraCandies):
    highest_candies = max(candies)
    for i, n1 in enumerate(candies):
        if n1 + extraCandies >= highest_candies:
            candies[i] = True
        else:
            candies[i] = False
    return (candies)


# 3 Running Sum of 1D Array (07.20.2020)
def runningSum(nums):
    sum = 0
    for i, n1 in enumerate(nums):
        sum += n1
        nums[i] = sum
    return nums


# 4 Number of Good Pairs (07.20.2020)
def numIdenticalPairs(nums):
    good_pairs = 0
    for i, n1 in enumerate(nums):
        for j, n2 in enumerate(nums):
            if j == i:
                continue
            if n1 == n2 and i < j:
                good_pairs += 1
    return good_pairs


# 5 Shuffle the Array (07.20.2020)
def shuffle(nums, n):
    list1 = [nums[i] for i in range(0, n)]
    list2 = [nums[i] for i in range(n, len(nums))]
    j = 0
    k = 0
    for i, n1 in enumerate(nums):
        if i % 2 == 0:
            nums[i] = list1[j]
            j += 1
        else:
            nums[i] = list2[k]
            k += 1
    return (nums)


# 6 Defanging an IP address (07.20.2020)
def defangIPaddr(address):
    return address.replace('.', '[.]')


# 7 Number of Steps to Reduce a Number to Zero (07.20.2020)
def numberOfSteps(num):
    step = 0
    while num != 0:
        if num % 2 == 0:
            num /= 2
        else:
            num -= 1
        step += 1
    return step


# 8 Jewels and Stones (07.20.2020)
def numJewelsInStones(J, S):
    sum = 0
    for i in J:
        for j in S:
            if i == j:
                sum += 1
    return sum


# 9 How Many Numbers Are Smaller Than the Current Number (07.20.2020)
def smallerNumbersThanCurrent(nums):
    count = 0
    temp = []
    for i, n1 in enumerate(nums):
        for j, n2 in enumerate(nums):
            if n1 > n2:
                count += 1
        temp.append(count)
        count = 0
    return temp


# 10 XOR Operator in an Array (No idea what this is) (07.30.2020)
def xorOperation(n, start):
    nums = [0] * n
    xor = 0
    for i in range(0,n):
        nums[i] = start
        start += 2
    for i in nums:
        xor ^= i
    return xor

# 11 Decompress Run-Length Encoded List (07.22.2020)
def decompressRLElist(nums):
    ans = []
    n = len(nums)
    for i in range(0, n // 2):
        ans.extend([nums[2 * i + 1] for j in range(nums[2 * i])])
    return ans


# 12 Subtract the Product and Sum of Digits of an Integer (07.23.2020)
def subtractProductAndSum(n):
    digits = [int(i) for i in list(str(n))]
    d = 1
    for i in digits:
        d *= i
    return d - sum(digits)


# 13 Create Target Array in the Given Order (07.23.2020)
def createTargetArray(nums, index):
    target = []
    for i in range(len(nums)):
        target.insert(index[i], nums[i])
    return target


# 14 Split a String in Balanced Strings (07.23.2020)
def balancedStringSplit(s):
    count = 0
    result = 0
    for char in s:
        if char == 'R':
            count += 1
        else:
            count -= 1
        if count == 0:
            result += 1
    return result


# 15 Find Numbers with Even Number of Digits (07.23.2020)
def findNumbers(nums):
    count = 0
    for i in nums:
        if len(str(i))%2 == 0:
            count += 1
    return count

# 16 Reverse Integer (07.23.2020)
def reverse(x):
    if x == 0 or x not in range(-2**31, 2**31-1):
        return 0
    while x % 10 == 0:
        x //= 10
    if x < 0:
        ans = f"{str(-x)}-" [::-1]
        if int(ans) not in range(-2**31, 2**31-1):
            return 0
        return ans
    if int(str(x) [::-1]) not in range(-2 ** 31, 2 ** 31 - 1):
        return 0
    return str(x) [::-1]

# 17 Palindrome Number (07.24.2020)
def isPalindrome(x):
    orig_x = x
    x_backwards = 0
    while x > 0:
        x_backwards = (x_backwards * 10) + (x % 10)
        x  //= 10
    return x_backwards == orig_x

# 18 Roman to Integer (07.24.2020)
def romanToInt(s):
    numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    count,temp = 0,0
    for i, n1 in list(enumerate(s)):
        if i < len(list(s))-1 and numerals[n1] == numerals[s[i+1]]:
            temp += numerals[n1]
        elif i < len(list(s))-1 and numerals[n1] < numerals[s[i+1]]:
            count -= numerals[n1] + temp
            temp = 0
        else:
            count += numerals[n1] + temp
            temp = 0
        print(count)
    return count + temp

# 19 Longest Common Prefix
def longestCommonPrefix(strs):
    pre = ''
    for char in zip(*strs):
        if len(set(char)) != 1:
            return pre
        pre += char[0]
    return pre

# 20 Valid Parentheses: (07.24.2020)
def isValid(s):
    values = {
        '(': 1,
        ')': -1,
        '[': 2,
        ']': -2,
        '{': 3,
        '}': -3
    }
    counter = []
    for i in range(0, len(s)):
        counter.append(values.get(s[i]))
    new_list = []
    j = 0
    for i, n1 in enumerate(counter):
        new_list.append(n1)
        if i > 0:
            if sum(counter) != 0:
                return False
            if j < len(counter) and new_list[j] + n1 < 0:
                return False
            if new_list[j] == -n1:
                new_list.pop()
                new_list.pop()
                j -= 2
            j+=1
    return not new_list

# 21 Range Sum of BST (07.25.2020)
def rangeSumBST(root, L, R):
    total = 0
    for i in root:
        if i >= L and i <= R:
            total += i
    return total

# 22 Shuffle String (07.30.2020)
def restoreString(s, indices):
    string = [''] * len(s)
    for i, char in enumerate(s):
        string[indices[i]] = char
    return "".join(string)