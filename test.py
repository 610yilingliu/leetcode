# nums = [1, 2, 3, 4]
# subsets = []
# n = len(nums)
# sum_sets = 2 ** n
# for i in range(sum_sets):
#     cur_set = []
#     for j in range(n):
#         power = 2 ** j
#         if i & power == power:
#             cur_set.append(nums[j])
#     subsets.append(cur_set)
# print(subsets)



def majorityElement_bit(nums):
    bit_bucket = [0 for i in range(33)]
    for num in nums:
        bit_bucket[32] += (num >> 32) & 1
        for i in range(32):
            bit_bucket[i] += (abs(num) >> i) & 1

    majority_num = 0
    nums_len = len(nums)
    for i in range(32):
        if bit_bucket[i] > nums_len / 2:
            majority_num += 1 << i
    if bit_bucket[32] > nums_len / 2:
        majority_num *= -1
    return majority_num

if __name__ == '__main__':
    a = majorityElement_bit([1,2,1,1])
    print(a)