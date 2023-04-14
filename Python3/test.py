# def meetingRoomIII(intervals, rooms, ask):
#     # Write your code here.
#     sum = [0 for i in range(11)];
#     vis = [0 for i in range(11)];
#     length = len(ask);
#     ans = [False for i in range(length)];
#     sum[0] = 0;
#     maxn = 0;
#     for i in range(0, len(intervals)):
#         vis[intervals[i][0]] += 1;
#         vis[intervals[i][1]] -= 1;
#         maxn = max(maxn, intervals[i][1]);
#     tmp = 0;
#     for i in range(0, length):
#         maxn = max(maxn, ask[i][1]);
#     for i in range(1, maxn + 1):
#         tmp += vis[i];
#         if tmp < rooms:
#             sum[i] = 0;
#         else:
#             sum[i] = 1;
#     for i in range(1, maxn + 1):
#         sum[i] += sum[i - 1];
#     for i in range(0, length):
#         if sum[ask[i][0] - 1] == sum[ask[i][1] - 1]:
#             ans[i] = True;
#         else:
#             ans[i] = False;
#     return ans

# a = meetingRoomIII([[1,2],[4,5],[8,10]], 1, [[4,5],[5,6]])
# print(a)

def meetingRoomIII(intervals, rooms, ask):
    """
    query time complexity:
    O(sum([ask[1] - ask[0]])) much longer than the best solution, but works
    """
    mx_time = 0
    # In these two for loop, we get the latest meeting time for building array
    # This will be used if the max meeting time is not provided
    for i in intervals:
        mx_time = max(mx_time, i[1])
    for each_ask in ask:
        mx_time = max(mx_time, each_ask[1])

    # answer
    ans = [False] * len(ask)   
    # start_end_series record the start and the end time of meeting, similar than the vis[] variable provided in official solution
    start_end_series = [0] * (mx_time + 1)
    for i in intervals:
        start_end_series[i[0]] += 1
        start_end_series[i[1]] -= 1

    # occupied_status: how many meetings are hold in the current time
    occupied_status = [0] * (mx_time + 1)
    occupied_status[0] = start_end_series[0]

    # Remember we only insert one meeting into existed meetings at once, so if the number of meeting is less than rooms(smaller than limit)
    # it is no doubt that current time could hold a new meeting
    # variable danger_zone hold the time that cannot hold a new meeting, if we cannot hold a new meeting in time i, danger_zone[i] = 1 
    danger_zone = [0] * (mx_time + 1)
    # You can ask the interviewer if the given "interval" is valid or not, if not, you can say we need to add a pre-checking module rather than
    # solving this question right away. You can also change >= to == if the interviewer says that "interval" is already valid
    if occupied_status[0] >= rooms:
        danger_zone[0] = 1                             
    for i in range(len(occupied_status)):
        occupied_status[i] = occupied_status[i - 1] + start_end_series[i]
        if occupied_status[i] >= rooms:
            danger_zone[i] = 1
    
    # check if there are any danger zone in the current query, that is why my solution is worse than the official solution.add()
    # official solution only spends O(1) for each query, but my solution spent O(n), n == query[1] - query[0]
    for i in range(len(ask)):
        satisfied = True
        for time in range(ask[i][0], ask[i][1]):
            if danger_zone[time] == 1:
                satisfied = False
                break
        if satisfied:
            ans[i] = True
    return ans

a = meetingRoomIII([[1,2],[4,5],[8,10]], 1, [[4,5],[5,6]])
print(a)