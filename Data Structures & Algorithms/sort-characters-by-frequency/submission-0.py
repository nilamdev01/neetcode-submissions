class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        result = []
        for ch, count in sorted(freq.items(), key=lambda x: x[1], reverse=True):
            result.append(ch * count)

        return ''.join(result)