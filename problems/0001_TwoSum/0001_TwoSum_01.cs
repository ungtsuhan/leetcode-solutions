public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int, int> dict = new Dictionary<int, int>();
        for(var i = 0; i < nums.Length; i++)
        {
            var complement = target - nums[i];
            if(dict.ContainsKey(complement))
            {
                return new int[] {dict[complement], i};
            }
            else
            {
                dict[nums[i]] = i;
            }
        }
        return new int[] {};
    }
}