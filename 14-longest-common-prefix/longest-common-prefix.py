class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len=min(len(word) for word in strs)
        for i in range(min_len):
            cur_wor=strs[0][i]
            for words in strs:
                if cur_wor!=words[i]:
                    return words[:i]
        return strs[0][:min_len]