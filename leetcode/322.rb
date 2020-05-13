# @param {Integer[]} coins
# @param {Integer} amount
# @return {Integer}
def coin_change(coins, amount)
    a = Array.new(amount + 1, Float::INFINITY)
    a[0] = 0
    for i in (1..amount)
        coins.each do |coin|
            if (0 <= i - coin )
                a[i] = [a[i], a[i-coin] +1].min
            end
        end
    end
    return a[amount] == Float::INFINITY ? -1 : a[amount]
end