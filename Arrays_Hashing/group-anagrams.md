
- Creates a 26-element count list for each string, representing letter frequencies 

- Uses ord(char) - ord('a') to map characters to list indices 

- Converts count list to tuple as dictionary key for grouping

- Returns dictionary values as grouped anagrams

- Time complexity: O(n * k), where n is the number of strings and k is the length of the longest string


```python

from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        if len(strs) < 2:
            return [strs]

        result = defaultdict(list)
        for string in strs:
            count = [0] * 26
            for char in string:
                count[ord(char) - ord("a")] += 1
            result[tuple(count)].append(string)
        return result.values()

```