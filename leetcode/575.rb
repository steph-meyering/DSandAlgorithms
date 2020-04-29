# 575. Distribute Candies

# @param {Integer[]} candies
# @return {Integer}
def distribute_candies(candies)
    [candies.uniq.length, candies.length / 2].min
end