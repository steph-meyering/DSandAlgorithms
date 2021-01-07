import unittest
from collections import deque


def get_path(graph, start_node, end_node):

    # Find the shortest route in the network between the two users
    if start_node not in graph or end_node not in graph:
        raise Exception("Invalid params")

    q = deque()
    q.append(([], start_node))
    seen = set()
    while q:
        path, node = q.popleft()
        path.append(node)
        if node == end_node:
            return path

        seen.add(node)
        for neighbor in graph[node]:
            if neighbor not in seen:
                q.append((path[:], neighbor))
    return None


#     queue = deque()
#     visited = set()
#     if not graph or not start_node or not end_node:
#         return None
#     visited.add(start_node)
#     for neighbor in graph[start_node]:
#         queue.append(([start_node], neighbor))
#         visited.add(neighbor)
#     while queue:
#         current_route, node = queue.popleft()
#         current_route.append(node)
#         if node == end_node:
#             return current_route
#         else:
#             for neighbor in graph[node]:
#                 if neighbor not in visited:
#                     visited.add(neighbor)
#                     queue.append((current_route, neighbor))

#     return None

# def process_node(queue):


# Tests

class Test(unittest.TestCase):

    def setUp(self):
        self.graph = {
            'a': ['b', 'c', 'd'],
            'b': ['a', 'd'],
            'c': ['a', 'e'],
            'd': ['a', 'b'],
            'e': ['c'],
            'f': ['g'],
            'g': ['f'],
        }

    def test_two_hop_path_1(self):
        actual = get_path(self.graph, 'a', 'e')
        expected = ['a', 'c', 'e']
        self.assertEqual(actual, expected)

    def test_two_hop_path_2(self):
        actual = get_path(self.graph, 'd', 'c')
        expected = ['d', 'a', 'c']
        self.assertEqual(actual, expected)

    def test_one_hop_path_1(self):
        actual = get_path(self.graph, 'a', 'c')
        expected = ['a', 'c']
        self.assertEqual(actual, expected)

    def test_one_hop_path_2(self):
        actual = get_path(self.graph, 'f', 'g')
        expected = ['f', 'g']
        self.assertEqual(actual, expected)

    def test_one_hop_path_3(self):
        actual = get_path(self.graph, 'g', 'f')
        expected = ['g', 'f']
        self.assertEqual(actual, expected)

    def test_zero_hop_path(self):
        actual = get_path(self.graph, 'a', 'a')
        expected = ['a']
        self.assertEqual(actual, expected)

    def test_no_path(self):
        actual = get_path(self.graph, 'a', 'f')
        expected = None
        self.assertEqual(actual, expected)

    def test_start_node_not_present(self):
        with self.assertRaises(Exception):
            get_path(self.graph, 'h', 'a')

    def test_end_node_not_present(self):
        with self.assertRaises(Exception):
            get_path(self.graph, 'a', 'h')


unittest.main(verbosity=2)
