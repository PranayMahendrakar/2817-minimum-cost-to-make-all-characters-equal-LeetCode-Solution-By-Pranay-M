class Solution:
    def minimumCost(self, s: str) -> int:
        n = len(s)
        cost = 0
        
        # For each pair of adjacent characters that differ
        # We need to flip one side or the other
        # Greedy: at position i, if s[i] != s[i+1], flip the smaller side
        
        for i in range(n - 1):
            if s[i] != s[i + 1]:
                # Cost to flip left side (0 to i) is i + 1
                # Cost to flip right side (i+1 to n-1) is n - i - 1
                cost += min(i + 1, n - i - 1)
        
        return cost