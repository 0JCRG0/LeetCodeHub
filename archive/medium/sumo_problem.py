import heapq

def last_sumo_power(weights):
    # Convert the list of weights into a max-heap.
    # In Python, the default implementation is a min-heap, so we insert negative values to simulate a max-heap.
    max_heap = [-w for w in weights]
    heapq.heapify(max_heap)

    # Simulate the fights until there is one or no sumo wrestler left.
    while len(max_heap) > 1:
        # Pop out the two heaviest sumo wrestlers.
        heaviest = -heapq.heappop(max_heap)
        second_heaviest = -heapq.heappop(max_heap)

        # If they are not of equal power, push the difference back into the heap.
        if heaviest != second_heaviest:
            heapq.heappush(max_heap, -(heaviest - second_heaviest))

    # If there is a sumo wrestler left, return its power, otherwise return 0.
    return -max_heap[0] if max_heap else 0

# Example usage:
weights = [2, 7, 4, 1, 8, 1]
print(last_sumo_power(weights))  # Output should be 1
