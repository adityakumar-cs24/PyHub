def longest_substring_with_k_unique_chars(s, k):
    max_length = 0
    
    for i in range(len(s)):
        unique_chars = set()
        for j in range(i, len(s)):
            unique_chars.add(s[j])
            
            if len(unique_chars) > k:
                break
            
            max_length = max(max_length, j - i + 1)
    
    return max_length

s , k = map(eval,input().split())
print(longest_substring_with_k_unique_chars(s, k))  
