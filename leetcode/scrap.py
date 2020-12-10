def bracket_match(text):
  s = []
  for c in text:
    if c == "(":
      s.append("(")
    else:
      if len(s) > 0 and s[-1] == "(":
        s.pop()
      else:
        s.append(")")
  return len(s)

print(bracket_match("()()((())"))