import unittest


def find_rotation_point(words):
    # Find the rotation point in the list
    # look left if:
    # cur word char < 1st word char
    # look right if:
    # 1st word char < cur word char
    # words[lo] will always be in the later half of the dict (ie: [n..z]),
    # and words[hi] will be in the earlier half [a..n]
    # THAT is why we want to return the very last 'hi' index since it will be the lowest word in dictionary
    # 'lo' index will be pointing to highest word in dict

    lo, hi = 0, len(words) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if words[mid] < words[0]:
            hi = mid
        else:
            lo = mid
        if lo + 1 == hi:
            return hi


# Tests

class Test(unittest.TestCase):

    def test_small_list(self):
        actual = find_rotation_point(['cape', 'cake'])
        expected = 1
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_rotation_point(['grape', 'orange', 'plum',
                                      'radish', 'apple'])
        expected = 4
        self.assertEqual(actual, expected)

    def test_large_list(self):
        actual = find_rotation_point(['ptolemaic', 'retrograde', 'supplant',
                                      'undulate', 'xenoepist', 'asymptote',
                                      'babka', 'banoffee', 'engender',
                                      'karpatka', 'othellolagkage'])
        expected = 5
        self.assertEqual(actual, expected)

    # Are we missing any edge cases?


unittest.main(verbosity=2)
