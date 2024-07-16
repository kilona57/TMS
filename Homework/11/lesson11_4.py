def longest_common_prefix(strs: list) -> str:
    if not strs:
        return ""
    min_len = min(len(s) for s in strs)
    for i in range(min_len):
        char = strs[0][i]
        if all(s[i] == char for s in strs):
            continue
        else:
            return strs[0][:i]
    return strs[0][:min_len]


print(longest_common_prefix(["flower","flow", "flight"]))
print(longest_common_prefix(["flower","cat", "dog"]))
print(longest_common_prefix(["hello","hello word", "hello dad"]))
