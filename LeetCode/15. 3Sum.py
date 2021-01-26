nums = [-2, 0, 0, 2, 2]
nums.sort()
res = []
for i in range(len(nums)-2):
    if i > 0 and nums[i] == nums[i-1]:
        continue
    l, r = i+1, len(nums)-1
    while l < r:
        sum = nums[i] + nums[l] + nums[r]
        if sum > 0:
            r -= 1
        elif sum < 0:
            l += 1
        else:
            res.append([nums[i], nums[l], nums[r]])
            l += 1
            r -= 1
        while l < r and nums[l-1] == nums[l]:
            l += 1
        while l < r and nums[r+1] == nums[r]:
            r -= 1
print(res)
