class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return None
        elif len(nums) == 1:
            return nums[0]
        else:
            i = 0
            tans = []
            ans = 0
            result = []
            for i in range(0, len(nums)):
                if len(tans) == 0:
                    tans.append(nums[i])
                    ans = sum(tans)
                    result.append(ans)

                else:
                    if nums[i] > 0 and sum(tans) < 0:
                        tans = []
                        tans.append(nums[i])
                        ans = sum(tans)
                        result.append(ans)

                    else:
                        if (sum(tans) + nums[i]) > nums[i]:
                            ans = sum(tans) + nums[i]  # oblivously
                            tans.append(nums[i])
                            result.append(ans)
                        else:
                            if (sum(tans) + nums[
                                i]) > 0:  # if previous sum is greater than 0, we keep that sum and wait for next big number
                                ans = sum(tans) + nums[i]
                                tans.append(nums[i])
                                result.append(ans)
                            else:
                                ans = nums[i]
                                result.append(ans)

            return max(result)

