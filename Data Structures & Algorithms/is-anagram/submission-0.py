class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        L=list(s)
        R=list(t)
        L.sort()
        R.sort()
        if L==R:
            return True
        else:
            return False
        