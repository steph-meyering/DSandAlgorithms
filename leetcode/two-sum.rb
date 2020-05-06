require 'byebug'

def two_sum(nums, target)
    nums.each_with_index do |num , idx|
        comp = target-num
        compidx = nums.index(comp)
        if !compidx.nil? && compidx != idx
            return [nums.index(num), nums.index(comp)]
        end
    end
end