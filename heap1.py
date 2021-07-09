from heapq import heappop , heappush , heapify

heap = []
nums = [12,3,5,-2,8,4]
for num in nums:
    heappush(heap,num)

while heap:
    print(heappop(heap))
