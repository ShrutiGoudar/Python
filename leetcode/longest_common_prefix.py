"""
14 . Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
 
Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
Solution by  : Sgoudar
My Algo : 
1. find the shortest string in the list and set it as initial search string for prefix 
2. while prefix is not an empty string
    a. search if this prefix is in the every element of list if yes return  prefix
    b. If not update prefix to prefix[:-1] and repeat search until length of prefix is > 0

"""
''' PEP8 solution from gpt
def find_prefix(strings: list[str]) -> str:
    if not strings:
        return ""
    prefix = min(strings, key=len)
    while prefix:
        if all(string.startswith(prefix) for string in strings):
            return prefix
        prefix = prefix[:-1]
    
    return ""
'''
def find_prefix(strs : list) -> str :
    prefix =""
    if not strs :       #check for empty list
        return prefix
    
    str_len = 200       # use the shortest string in the list as 1st possible prefix
    for s in strs:
        if len(s) < str_len:
            prefix = s
            str_len = len(s)
    while prefix:
        found_prefix = True
        for cur_elem in range(len(strs)):
            if not strs[cur_elem].startswith(prefix):
                found_prefix = False
        if not found_prefix:
            prefix = prefix[:-1]
        else:
            break
    return prefix


def find_suffix(strs:list)->str : 
    if not strs:
        return ""
    suffix_len = 200 # initializing it as length of list
    suffix = ""
    #find shortest str and set as search str
    for s in strs:
        if len(s) < suffix_len:
            suffix = s
            suffix_len = len(s)
    
    while suffix:
        found_suffix = True
        for cur_elem in range(len(strs)) : # search in list 
            if not strs[cur_elem].endswith(suffix):
                found_suffix = False
        if not found_suffix:
            suffix = suffix[:-1]
        else:
            break
    return suffix
        
            


def main():
    strs = ["suffix", "prefix","fix","transfix"]
    strs1= ["fixed","fixer", "fixing"]
    print("Prefix :" + find_prefix(strs1))
    print("Suffix: " + find_suffix(strs))

if __name__ == "__main__":
    main()