def search(nums, target):

    l, r, m = 0, len(nums) - 1, 0
#  Importante colocar <= em arrays que possuem apenas 1 número
    while l <= r:
      # Importante colocar (l+r) entre parenteses para ser calculado primeiro
        m = (l + r)//2

        if nums[m] == target:
            return m
        elif nums[m] < target:
            l = m + 1 
        else:
            r = m - 1
    return -1