# 819. Most Common Word

def most_common_word(paragraph, banned)
    new_paragraph = paragraph.gsub(/[!?',;.]/, " ") # regex to remove all punct
    words = new_paragraph.split(" ")
    hash = Hash.new(0)
    words.each do |word|
        w = word.downcase 
        hash[w] += 1 if !banned.include?(w)
    end
    return hash.max_by{ |k, v| v}[0] # [0] bcs returns an array [k, v]
end