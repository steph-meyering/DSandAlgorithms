# 70. Climbing Stairs

# @param {Integer} n
# @return {Integer}
def climb_stairs(n, mem = {})
    return 1 if n == 1
    return 2 if n == 2
    a = mem[n-1] || climb_stairs(n-1, mem)
    b = mem[n-2] || climb_stairs(n-2, mem)
    mem[n] = a + b
end

