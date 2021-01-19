import unittest


def is_valid(code):
    # Determine if the input code is valid

    openers = set(["[", "{", "("])
    closers = {
        ")": "(",
        "}": "{",
        "]": "["
    }
    stack = []
    for char in code:
        if char in openers:
            stack.append(char)
        elif char in closers:
            if stack and closers[char] == stack[-1]:
                stack.pop()
            else:
                return False
    return not stack


# Tests

class Test(unittest.TestCase):

    def test_valid_short_code(self):
        result = is_valid('()')
        self.assertTrue(result)

    def test_valid_longer_code(self):
        result = is_valid('([]{[]})[]{{}()}')
        self.assertTrue(result)

    def test_interleaved_openers_and_closers(self):
        result = is_valid('([)]')
        self.assertFalse(result)

    def test_mismatched_opener_and_closer(self):
        result = is_valid('([][]}')
        self.assertFalse(result)

    def test_missing_closer(self):
        result = is_valid('[[]()')
        self.assertFalse(result)

    def test_extra_closer(self):
        result = is_valid('[[]]())')
        self.assertFalse(result)

    def test_empty_string(self):
        result = is_valid('')
        self.assertTrue(result)


unittest.main(verbosity=2)
