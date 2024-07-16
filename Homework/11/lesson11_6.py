def str_to_strs(haystack: str, needle: str) -> int:
    if not needle:
        return 0
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1

print(str_to_strs("hello", "ll"))
print(str_to_strs("black", "bl"))
print(str_to_strs("black", "lb"))
print(str_to_strs("black", ""))
print(str_to_strs("", ""))