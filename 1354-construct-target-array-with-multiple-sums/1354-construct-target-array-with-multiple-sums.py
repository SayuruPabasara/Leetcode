class Solution(object):
    def isPossible(self, target):
        import heapq

class Solution:
    def isPossible(self, target):
        # Convert to max heap (Python has min heap, so use negatives)
        heap = [-x for x in target]
        heapq.heapify(heap)

        total = sum(target)

        while True:
            largest = -heapq.heappop(heap)
            rest = total - largest

            # Base cases
            if largest == 1 or rest == 1:
                return True

            # Impossible cases
            if rest == 0 or largest <= rest:
                return False

            # Reverse the operation
            prev = largest % rest
            if prev == 0:
                return False

            # Push back
            heapq.heappush(heap, -prev)
            total = rest + prev
