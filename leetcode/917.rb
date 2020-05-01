# 917. Reverse Only Letters

# @param {String} s
# @return {String}
def reverse_only_letters(s)
    str = s.split("")
    stack = []
    s.each_char do |char|
        stack.push(char) if char.match(/[[:alnum:]]/) # regex to check if char is alphanumeric
    end
    str.map! do |char|
        if char.match(/[[:alpha:]]/)
            char = stack.pop() 
        else
            char
        end
    end
    str.join('')
end

# One pass solution

# @param {String} s
# @return {String}
def reverse_only_letters(s)
    j = s.length - 1
    s.each_char.with_index do |char, i|
        return s if i >= j
        if char.match(/[[:alpha:]]/)
            j -= 1 until s[j].match(/[[:alpha:]]/)
            s[i], s[j] = s[j], s[i]
            j -= 1
        end
    end
end

# better because no nested loop or duplicated conditions

def reverse_only_letters(s)
    i = 0
    j = s.length - 1
    while i < j
        if !s[i].match(/[[:alpha:]]/)
            i += 1
        elsif !s[j].match(/[[:alpha:]]/)
            j -= 1
        else
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        end
    end
    return s
end