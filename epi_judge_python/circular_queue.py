from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Queue:
    def __init__(self, capacity):
        self.queue = [0] * capacity
        self.begin = self.count = self.end = 0
        return

    def enqueue(self, x):
        if self.count == len(self.queue):
            # Make queue elements appear consequtively.
            self.queue = self.queue[self.begin:] +self.queue[:self.begin]
            # Reset begin and end
            self.begin , self.end = 0, self.count
            self.queue += [0] * len(self.queue)
        self.queue[self.end] = x
        self.end = (self.end + 1) % len(self.queue)
        self.count += 1
        return

    def dequeue(self):
        self.count -= 1
        x = self.queue[self.begin]
        self.begin = (self.begin + 1) % len(self.queue)
        return x

    def size(self):
        return self.count


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure(
                    "Dequeue: expected " + str(arg) + ", got " + str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure(
                    "Size: expected " + str(arg) + ", got " + str(result))
        else:
            raise RuntimeError("Unsupported queue operation: " + op)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("circular_queue.py",
                                       'circular_queue.tsv', queue_tester))
