# @param {Integer[]} nums
# @return {Integer}
def find_numbers(nums)
    res = 0
    nums.each do |num|
       res += 1 if num.to_s.length.even?
    end
    return res
end