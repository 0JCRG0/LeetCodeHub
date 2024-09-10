

```python
# MOST OPTIMIZED SOLUTION:

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        counter_s, counter_t = {}, {}

        for i in range(len(s)):
            counter_s[s[i]] = 1 + counter_s.get(s[i], 0)
            counter_t[t[i]] = 1 + counter_t.get(t[i], 0)
        
        for key in counter_s:
            if counter_s.get(key, 0) != counter_t.get(key, 0):
                return False
        
        return True


# SOLUTION 1:

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        i = 0
        while i < len(s):
            if s[i] not in t or s.count(s[i]) != t.count(s[i]):
                return False
            i += 1
        return True


# SOLUTION 2:

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


# SOLUTION 3:

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


```