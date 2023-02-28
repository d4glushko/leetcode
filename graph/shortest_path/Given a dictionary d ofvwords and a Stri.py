Given a dictionary d ofvwords and a String s, determine if s can be segmented into a sequence of valid words
from dictionary d

d ["abc", "cat", "etc", "ca", "et"]
s1 "catetc" -> "cat", "etc" => trutrue
s3 "caet" 
s2 "cate" -> "cat" => false

"caet" -> "et"

N * M

M - len (str)
"catet"

"c"
"ca" -> 
"tet"

"ca"
"cat"

["cat", "ca", "et"], "catet"
0-3
"cat"


["cat", "ca", "et"] "et"

N - len dictionary
M - len sequence string
"a", "ab", "abc" "bc" "cd" "de" "ef" "f" "bcd" "cde" "bcde"
"abcdefg"
O(M * N)

import functools

@functools.cache()
def is_valid_sequence(dictionary, sequence) -> bool:
    if sequence in dictionary:
        return True
    
    substr_len = 1
    while substr_len < len(sequence):
        if sequence[:substr_len] in dictionary:
            left_sequence = sequence[substr_len:]
            
            res = is_valid_sequence(dictionary, left_sequence)
            if res:
                return True
        substr_len += 1
        
    return False
    
