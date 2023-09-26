class Solution:
    def thirdLargest(self, a, n):
        # code here
        n = len(a)

        x = max(a)
        a.remove(x)

        y = max(a)
        a.remove(y)

        z = max(a)

        return z

    