class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        ta, tb, tc = target
        fa = fb = fc = False
        for a, b, c in triplets:
            if not fa and a == ta and b <= tb and c <= tc:
                fa = True
            if not fb and b == tb and a <= ta and c <= tc:
                fb = True
            if not fc and c == tc and a <= ta and b <= tb:
                fc = True
            if fa and fb and fc:
                return True
        return False
