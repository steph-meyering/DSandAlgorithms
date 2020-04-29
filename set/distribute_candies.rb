# 575. Distribute Candies

# Using a Set

# @param {Integer[]} candies
# @return {Integer}
def distribute_candies(candies)
    s = Set.new(candies)
    max = candies.length / 2
    return s.length > max ? max : s.length
end

# Optimized

def distribute_candies(candies)
    [candies.uniq.length, candies.length / 2].min
end

