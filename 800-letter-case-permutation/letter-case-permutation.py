# class Solution:
#     def letterCasePermutation(self, s: str) -> List[str]:
#         def dfs(i):
#             if i == len(s):
#                 result.append(''.join(curr))
#                 return
#             if s[i].isalpha():
#                 curr[i] = s[i].lower()
#                 dfs(i + 1)
#                 curr[i] = s[i].upper()
#                 dfs(i + 1)
#             else:
#                 curr[i] = s[i]
#                 dfs(i + 1)

#         result = []
#         curr = [''] * len(s)
#         dfs(0)
#         return result

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        output = []
        for word in s :
            output.append([word] if word.isdigit() else [word.lower(), word.upper()])

        return [''.join(w) for w in itertools.product(*output)]