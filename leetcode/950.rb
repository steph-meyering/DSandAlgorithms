# 950. Reveal Cards In Increasing Order


# @param {Integer[]} deck
# @return {Integer[]}

def deck_revealed_increasing(deck)
  deck.sort!
  result = []

  result.unshift(deck.pop)

  deck.reverse_each do |val|
    el = result.pop
    result.unshift(el)
    result.unshift(val)
  end

  result
end