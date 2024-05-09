class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Create a frequency array to keep track of the count of each task
        freq = [0] * 26
        for task in tasks:
            freq[ord(task) - ord('A')] += 1

        # Sort the frequency array in non-decreasing order
        freq.sort()
        # Calculate the maximum frequency of any task
        max_freq = freq[25] - 1
        # Calculate the number of idle slots that will be required
        idle_slots = max_freq * n
        # Iterate over the frequency array from the second highest frequency to the lowest frequency

        for i in range(24, -1, -1):
            # Subtract the minimum of the maximum frequency and the current frequency from the idle slots
            idle_slots -= min(max_freq, freq[i])

        # If there are any idle slots left, add them to the total number of tasks
        return idle_slots + len(tasks) if idle_slots > 0 else len(tasks)

# class Solution:
#     def leastInterval(self, tasks: List[str], n: int) -> int:
#         # freq array to store the frequency of each task
#         freq = [0] * 26
#         mx_cnt = 0

#         # Count the frequency of each task and find the maximnum frequency
#         for task in tasks :
#             freq[ord(task) - ord("A")] += 1
#             mx_cnt = max(mx_cnt, freq[ord(task) - ord("A")])

#         # Calculate the total time needed for execution
#         time = (mx_cnt - 1) * (n + 1)
#         for f in freq :
#             if f == mx_cnt :
#                 time += 1

#         # Return the miximum of total time neede and the length of the task list
#         return max(len(tasks), time)

# class Solution:
#     def leastInterval(self, tasks: List[str], n: int) -> int:
#         # Create a frequency array to keep track of the count of each task
#         freq = [0] * 26
#         for task in tasks:
#             freq[ord(task) - ord('A')] += 1

#         # Sort the frequency array in non-decreasing order
#         freq.sort()
#         # Calculate the maximum frequency of any task
#         max_freq = freq[25] - 1
#         # Calculate the number of idle slots that will be required
#         idle_slots = max_freq * n
#         # Iterate over the frequency array from the second highest frequency to the lowest frequency

#         for i in range(24, -1, -1):
#             # Subtract the minimum of the maximum frequency and the current frequency from the idle slots
#             idle_slots -= min(max_freq, freq[i])

#         # If there are any idle slots left, add them to the total number of tasks
#         return idle_slots + len(tasks) if idle_slots > 0 else len(tasks)

# class Solution:
#     def leastInterval(self, tasks: List[str], n: int) -> int:
#         # Build frequency map
#         freq = [0] * 26
#         for ch in tasks:
#             freq[ord(ch) - ord('A')] += 1
        
#         # Max heap to store frequencies
#         pq = [-f for f in freq if f > 0]
#         heapq.heapify(pq)

#         time = 0
#         # Process tasks until the heap is empty
#         while pq:
#             cycle = n + 1
#             store = []
#             task_count = 0
#             # Execute tasks in each cycle
#             while cycle > 0 and pq:
#                 current_freq = -heapq.heappop(pq)
#                 if current_freq > 1:
#                     store.append(-(current_freq - 1))
#                 task_count += 1
#                 cycle -= 1
#             # Restore updated frequencies to the heap
#             for x in store:
#                 heapq.heappush(pq, x)
#             # Add time for the completed cycle
#             time += task_count if not pq else n + 1
#         return time