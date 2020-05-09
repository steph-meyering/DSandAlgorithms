# 169. Majority Element

# @param {Integer[]} nums
# @return {Integer}
def majority_element(nums)
    curNum = nil
    freq = 1
    nums.each do |num|
        if curNum === num
            freq += 1
        else
            freq -= 1
        end
        if freq === 0
            curNum = num
            freq = 1
        end
    end
    curNum
    
end