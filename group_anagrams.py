"""
Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

"""


def groupAnagrams(strs):
    words = dict()
    for i in strs:
        x = tuple(sorted(list(i)))
        if x in words:
            words[x].append(i)
        else:
            words[x] = [i]

    print(words)
    print(list(words.values()))

strs = ["eat","tea","tan","ate","nat","bat"]
groupAnagrams(strs)