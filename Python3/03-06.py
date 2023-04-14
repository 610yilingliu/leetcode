import collections

data=[['C', 2, 110], ['A', 1, 100],[ 'A', 2, 110],['A', 3, 130], ['A', 3, 120], ['A', 4, 150],['A', 5, 170],
['B', 1, 100],['B', 2, 110], ['B', 3, 120], ['B', 4, 150], ['B', 5, 170], ['C', 1, 100]]

# # purpose: only use the first "TIME" when we have the same "KEY" and same 'STEP"
# step_cnt = collections.defaultdict(int)
# step_sum = collections.defaultdict(int)
# # walked: Set(Tuple(KEY, STEP)), tuple example('A', 3)
# walked_items = dict()
# for i in range(len(data)):
#     key, step, time = data[i]
#     if (key, step) in walked_items:
#         if time < walked_items[(key, step)]:
#             step_sum[step] -= walked_items[(key, step)]
#             step_sum[step] += time
#         else:
#             continue
#     else:
#         walked_items[(key, step)] = time
#         step_cnt[step] += 1
#         step_sum[step] += time

# # although we are using python 3.7+, but the real world data could be ['A', 2, 100],[ 'A', 3, 110],['B', 1, 90], ['A', 1, 100],the key order in dictionary could be [2, 3, 1]. So we cannot simply use the previous key 
# step_cnt_unpacked = sorted((k, v) for k, v in step_cnt.items())
# step_sum_unpacked = sorted((k, v) for k, v in step_sum.items())
# ans = []
# for i in range(1, len(step_cnt_unpacked)):
#     prev_avg = step_sum_unpacked[i - 1][1]/step_cnt_unpacked[i - 1][1]
#     cur_avg = step_sum_unpacked[i][1]/step_cnt_unpacked[i][1]
#     ans.append(cur_avg - prev_avg)
# print(ans)

def count_avg(lists):
    ans_len = max([len(l) for l in lists])
    sums = ans_len * [0]
    occupies = ans_len * [0]
    for l in lists:
        for i in range(len(l)):
            sums[i] += l[i]
            occupies[i] += 1
    ans = []
    for i in range(len(occupies)):
        ans.append(sums[i]/occupies[i])
    return ans

every_item_intervel = collections.defaultdict(dict)
walked_items = dict()
for i in range(len(data)):
    key, step, time = data[i]
    if (key, step) in walked_items:
        if time >= walked_items[(key,step)]:
            continue
        walked_items[(key, step)] = time
    every_item_intervel[key][step] = time

time_ranges = []
for k1, v1 in every_item_intervel.items():
    cur_intervals = []
    v = [pair[1] for pair in sorted((k, v) for k, v in v1.items())]
    for i in range(1, len(v)):
        cur_intervals.append(v[i] -v[i - 1])
    time_ranges.append(cur_intervals)

ans = count_avg(time_ranges)
print(ans)
