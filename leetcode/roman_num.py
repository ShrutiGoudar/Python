''' 
Given a roman numeral, convert it to an integer.
Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
'''
""" My Algorithm:
1. check if given symbol is a roman numeral or not
2. 
"""
def romanToInt(s):
        """
        :type s: str
        :rtype: int
        """
        int_val = 0
        roman_sym = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        for index in range(len(s)):
            pos = s[index]
            if pos not in roman_sym : 
                print("Not a Roman Numeral")
                int_val = -1
            if pos == 'I' and index < len(s)-1 and (s[index+1] == 'V' or s[index+1] == 'X'):
                int_val += -1
                continue
            if pos == 'X' and index < len(s)-1 and (s[index+1] == 'L' or s[index+1] == 'C'):
                int_val += -10
                continue
            if pos == 'C' and index < len(s)-1 and (s[index+1] == 'D' or s[index+1] == 'M'):
                int_val += -100
                continue
            int_val += roman_sym[pos]
        return int_val

def romanToInt_optimized(s: str) -> int:
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    for i in range(len(s)):
        if i < len(s) - 1 and roman_map[s[i]] < roman_map[s[i+1]]:
            total -= roman_map[s[i]]
        else:
            total += roman_map[s[i]]
    return total


# Test cases
test_cases = ["IV", "IX", "XL", "XC", "CD", "CM", "LVIII", "MCMXC", "MMXXIV"]

print("Testing romanToInt_optimized:")
for test in test_cases:
    result = romanToInt_optimized(test)
    print(f"{test} = {result}")

# Test the specific case
s = "IV"  # Changed from "XM" which isn't valid
print(f"\nTesting {s}: {romanToInt_optimized(s)}")


"""
Feedback on my solution:
My solution is correct and works well for converting Roman numerals to integers. However, the optimized version is more efficient and concise.
It reduces the number of conditional checks by leveraging the properties of Roman numerals, specifically the subtraction rule. 
This makes the code easier to read and maintain. Overall, both implementations are valid, 
but the optimized version is preferred for its clarity and efficiency.

Redundant Input Validation:
Unnecessary print Statement: LeetCode does not require print statements for invalid input handling.
"""


        