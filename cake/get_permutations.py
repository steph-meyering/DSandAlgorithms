import unittest


def get_permutations(string):
    # Generate all permutations of the input string
    if len(string) < 2:
        return set([string])
    
    last_char = string[-1]
    shorter_string = string[:-1]
    
    prev_permutations = get_permutations(shorter_string) # WHAT GOES ON HERE
    result = set()
    
    for permutation in prev_permutations:
        for i in range(len(shorter_string) + 1):
            result.add(permutation[:i] + last_char + permutation[i:])
    
    return result
    



  # Tests

class Test(unittest.TestCase):

    def test_empty_string(self):
        actual = get_permutations('')
        expected = set([''])
        self.assertEqual(actual, expected)

    def test_one_character_string(self):
        actual = get_permutations('a')
        expected = set(['a'])
        self.assertEqual(actual, expected)

    def test_two_character_string(self):
        actual = get_permutations('ab')
        expected = set(['ab', 'ba'])
        self.assertEqual(actual, expected)

    def test_three_character_string(self):
        actual = get_permutations('abc')
        expected = set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)