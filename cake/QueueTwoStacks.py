import unittest


class QueueTwoStacks(object):

    # Implement the enqueue and dequeue methods
    def __init__(self):
        self.in_stack = []
        self.out_stack = []
        self.stack_size = 0

    def enqueue(self, item):
        self.in_stack.append(item)
        self.stack_size += 1

    def dequeue(self):
        if 0 < self.stack_size:
            if not self.out_stack:
                for i in range(1, self.stack_size + 1):
                    self.out_stack.append(self.in_stack[-i])
            self.stack_size -= 1
            return self.out_stack.pop()
        else:
            raise Exception('No elements in queue')


# Tests

class Test(unittest.TestCase):

    def test_basic_queue_operations(self):
        queue = QueueTwoStacks()

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        actual = queue.dequeue()
        expected = 1
        self.assertEqual(actual, expected)

        actual = queue.dequeue()
        expected = 2
        self.assertEqual(actual, expected)

        queue.enqueue(4)

        actual = queue.dequeue()
        expected = 3
        self.assertEqual(actual, expected)

        actual = queue.dequeue()
        expected = 4
        self.assertEqual(actual, expected)

    def test_error_when_dequeue_from_new_queue(self):
        queue = QueueTwoStacks()

        with self.assertRaises(Exception):
            queue.dequeue()

    def test_error_when_dequeue_from_empty_queue(self):
        queue = QueueTwoStacks()

        queue.enqueue(1)
        queue.enqueue(2)

        actual = queue.dequeue()
        expected = 1
        self.assertEqual(actual, expected)

        actual = queue.dequeue()
        expected = 2
        self.assertEqual(actual, expected)

        with self.assertRaises(Exception):
            queue.dequeue()


unittest.main(verbosity=2)
