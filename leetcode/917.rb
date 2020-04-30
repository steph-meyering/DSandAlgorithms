# 917. Reverse Only Letters

# @param {String} s
# @return {String}
def reverse_only_letters(s)
    str = s.split("")
    stack = []
    s.each_char do |char|
        stack.push(char) if char.match(/^[[:alpha:]]$/) # regex to check if char is alphanumeric
    end
    str.map! do |char|
        if char.match(/^[[:alpha:]]$/)
            char = stack.pop() 
        else
            char
        end
    end
    str.join('')
end