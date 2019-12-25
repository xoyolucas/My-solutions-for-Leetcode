class Solution
{
public:
    int majorityElement(vector<int> &nums)
    {
        int count = 0;
        int res;
        for (auto &num : nums)
        {
            if (count == 0)
            {
                res = num;
                count += 1;
            }
            else
            {
                count += (res == num) ? 1 : -1;
            }
        }
        return res;
    }
};