#https://leetcode.com/problems/group-anagrams

from collections import defaultdict

def groupAnagrams(self,strs: List[str])->List[List[str]]:
    anagrams = defaultdict(list)

    for s in strs:
        anagrams[''.join(sorted(s))].append(s)

    return list(anagrams.values())