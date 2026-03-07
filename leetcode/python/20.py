# Valid Parentheses


class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        p = {")": "(", "}": "{", "]": "["}
        for i in s:
            if i not in p:
                st.append(i)
            else:
                if not st or st.pop() != p[i]:
                    return False
        return not st
