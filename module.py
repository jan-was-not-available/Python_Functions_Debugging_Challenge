"""
Debugging Challenge

This module contains functions that should work according
to the descriptions below, but each function contains
one or more bugs.

Your task:
Fix the code so that all tests pass.

Rules:
- Do NOT change function names
- Do NOT change parameters
- Only modify the code inside the functions
"""


# -------------------------------------------------
# double_number
# -------------------------------------------------
# Takes an integer and returns double its value.
#
# Examples:
#   double_number(4) -> 8
#   double_number(-3) -> -6
#
def double_number(num: int) -> int:
    return num * 2


# -------------------------------------------------
# count_vowels
# -------------------------------------------------
# Returns the number of vowels in a string.
# Vowels: a, e, i, o, u (both lowercase and uppercase)
#
# Examples:
#   count_vowels("hello") -> 2
#   count_vowels("AEIOU") -> 5
#
def count_vowels(s: str) -> int:

    count = 0

    for char in s:
        if char.lower() in "aeiou":  
            count += 1

    return count


# -------------------------------------------------
# sum_list
# -------------------------------------------------
# Returns the sum of a list of integers.
#
# Examples:
#   sum_list([1,2,3]) -> 6
#   sum_list([]) -> 0
#
def sum_list(numbers: list) -> int:

    total = 0

    for num in numbers:
        total += num
    return total


# -------------------------------------------------
# reverse_string
# -------------------------------------------------
# Returns the reversed version of a string.
#
# Examples:
#   reverse_string("cat") -> "tac"
#
def reverse_string(s: str) -> str:
    result = ""
    for char in s:
        result = char + result  
    return result

# -------------------------------------------------
# first_character
# -------------------------------------------------
# Returns the first character of a string.
#
# Examples:
#   first_character("cat") -> "c"
#   first_character("hello") -> "h"
#
def first_character(s: str) -> str:
    return s[0] 


# -------------------------------------------------
# max_in_list
# -------------------------------------------------
# Returns the largest number in a list.
#
# Examples:
#   max_in_list([1,5,3]) -> 5
#
def max_in_list(numbers: list) -> int:

    maximum = numbers[0]

    for num in numbers:
        if num > maximum:
            maximum = num

    return maximum


# -------------------------------------------------
# remove_spaces
# -------------------------------------------------
# Returns a new string with all spaces removed.
#
# Examples:
#   remove_spaces("a b c") -> "abc"
#
def remove_spaces(s: str) -> str:

    result = ""

    for char in s:
        if char != " ":   
            result += char
            
    return result

# -------------------------------------------------
# count_positive
# -------------------------------------------------
# Returns how many positive numbers are in a list.
#
# Examples:
#   count_positive([3,-1,2,-5]) -> 2
#

def count_positive(numbers: list) -> int:

    count = 0
    
    for num in numbers:
        if num > 0:
            count += 1

    return count

# -------------------------------------------------
# two_sum (Challenge)
# -------------------------------------------------
# Description:
#   Takes a list of integers and a target.
#   Returns True if there are two integers in the list that add to the target.
#   Retruns False if there are not two integers that add to the target.
# Examples:
#   two_sum([1, 2, 3, 4], 7) -> True
#   two_sum([1, 2, 3, 4], 8) -> False
#   two_sum([0, 2, 0, 2], 4) -> True
#   two_sum([-1, -3, -5], -3) -> False
#   two_sum([], 0) -> False

# Requirements:
#   - The function must return the True or False.
#   - Do NOT print anything.
#
def two_sum(nums: list, target: int) -> bool:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return True
            
    return False        
    pass