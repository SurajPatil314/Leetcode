'''
Given a wordlist, we want to implement a spellchecker that converts a query word into a correct word.

For a given query word, the spell checker handles two categories of spelling mistakes:

Capitalization: If the query matches a word in the wordlist (case-insensitive), then the query word is returned
with the same case as the case in the wordlist.
Example: wordlist = ["yellow"], query = "YellOw": correct = "yellow"
Example: wordlist = ["Yellow"], query = "yellow": correct = "Yellow"
Example: wordlist = ["yellow"], query = "yellow": correct = "yellow"
Vowel Errors: If after replacing the vowels ('a', 'e', 'i', 'o', 'u') of the query word with any vowel individually,
 it matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the match
  in the wordlist.
Example: wordlist = ["YellOw"], query = "yollow": correct = "YellOw"
Example: wordlist = ["YellOw"], query = "yeellow": correct = "" (no match)
Example: wordlist = ["YellOw"], query = "yllw": correct = "" (no match)
In addition, the spell checker operates under the following precedence rules:

When the query exactly matches a word in the wordlist (case-sensitive), you should return the same word back.
When the query matches a word up to capitlization, you should return the first such match in the wordlist.
When the query matches a word up to vowel errors, you should return the first such match in the wordlist.
If the query has no matches in the wordlist, you should return the empty string.
Given some queries, return a list of words answer, where answer[i] is the correct word for query = queries[i].

'''

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:

        vowels = ['a', 'e', 'i', 'o', 'u']
        wordlist1 = set(wordlist)
        ans = []

        for case in queries:
            # print(case)
            # print('@@@')
            grandflag = 0
            if case in wordlist1:
                ans.append(case)
                # print('found word directly')
                grandflag = 1
            else:
                for word in wordlist1:

                    # print(word)
                    # print('%%%')
                    if case.lower() == word.lower():
                        ans.append(word)
                        # print('found match lower or upper')
                        grandflag = 1
                        break
                    else:
                        if len(case) == len(word):
                            flag = 0
                            for i in range(0, len(case)):
                                if case[i].lower() == word[i].lower():
                                    flag = 1
                                else:
                                    if ((case[i].lower() in vowels) and (word[i].lower() in vowels)):
                                        flag = 1
                                    else:
                                        flag = 0
                                        break

                            if flag == 1:
                                # print('found match after replacing vowels')
                                ans.append(word)
                                grandflag = 1
                                break
                            else:
                                grandflag = 0
                                # print('not a match')

            if grandflag == 0:
                ans.append('')

        return ans
