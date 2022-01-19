"""
https://leetcode.com/problems/logger-rate-limiter/

Design a logger system that receives a stream of messages 
along with their timestamps. Each unique message should 
only be printed at most every 10 seconds (i.e. a message 
printed at timestamp t will prevent other identical 
messages from being printed until timestamp t + 10).

All messages will come in chronological order. Several 
messages may arrive at the same timestamp.

Implement the Logger class:
- Logger() Initializes the logger object.
- bool shouldPrintMessage(int timestamp, string message) 
Returns true if the message should be printed in the given timestamp, 
otherwise returns false.

Example 1:
Input
["Logger", "shouldPrintMessage", "shouldPrintMessage", 
"shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", 
"shouldPrintMessage"]
[[], [1, "foo"], [2, "bar"], [3, "foo"], [8, "bar"], 
[10, "foo"], [11, "foo"]]
Output
[null, true, true, false, false, false, true]

Explanation
Logger logger = new Logger();
logger.shouldPrintMessage(1, "foo");  
// return true, next allowed timestamp for "foo" is 1 + 10 = 11
logger.shouldPrintMessage(2, "bar");  
// return true, next allowed timestamp for "bar" is 2 + 10 = 12
logger.shouldPrintMessage(3, "foo");  
// 3 < 11, return false
logger.shouldPrintMessage(8, "bar");  
// 8 < 12, return false
logger.shouldPrintMessage(10, "foo"); 
// 10 < 11, return false
logger.shouldPrintMessage(11, "foo"); 
// 11 >= 11, return true, next allowed timestamp for "foo" is 11 + 10 = 21
 

Constraints:
0 <= timestamp <= 10^9
Every timestamp will be passed in non-decreasing order (chronological order).
1 <= message.length <= 30
At most 10^4 calls will be made to shouldPrintMessage.
"""
from typing import List


class LoggerHashtable:
    def __init__(self):
        # Time complexity: O(1)
        # Space complexity: O(n),
        # where `n` is the number of messages

        # Use a hashtable to map { message: next_valid_time }
        self.next_valid_time = {}

    def should_print_message(self, timestamp: int, message: str) -> bool:
        print_it = True

        if message in self.next_valid_time:
            print_it = self.next_valid_time[message] <= timestamp

        if print_it:
            self.next_valid_time[message] = timestamp + 10

        return print_it


class LoggerTwoHashtables:
    def __init__(self):
        # Time complexity: O(1)
        # Space complexity: O(m),
        # where `m` is the max number of messages recevied
        # in 20 seconds.

        # Use two hashtables to map { messsage: next_valid_time }
        # We use `new` hashtable to store the messages from
        # the last 10 seconds. After 10 seconds, all those messages will
        # be moved to `old` hashtable.
        # This way, we can keep the memory requirements low, and
        # still have constant time complexity.
        # Moving all the messages from `new` to `old` is O(1),
        # so no need to track which messages can be removed.
        self.old = {}
        self.new = {}
        self.last_time = 0

    def should_print_message(self, timestamp: int, message: str) -> bool:
        if timestamp >= self.last_time + 20:
            # If the last message is older than 20 seconds,
            # we can clear the hashtables, there won't be any conflicts
            self.old.clear()
            self.new.clear()
            self.last_time = timestamp

        elif timestamp >= self.last_time + 10:
            # If the last message is older than 10 seconds (< 20 seconds),
            # move the messages in `new` hashtable to `old`
            self.old = self.new
            self.new = {}
            self.last_time = timestamp

        if message in self.new:
            # If `message` is in the `new` hashtable, it's not old enough,
            # so we can't print it
            return False
        if message in self.old and timestamp < self.old[message] + 10:
            # If `message` is in the `old` hashtable but not old enough,
            # we can't print it
            return False

        self.new[message] = timestamp
        return True


if __name__ == "__main__":
    print("-" * 60)
    print("Logger rate limiter")
    print("-" * 60)

    test_cases = [
        (
            [(1, "foo"), (2, "bar"), (3, "foo"), (8, "bar"), (10, "foo"), (11, "foo")],
            [True, True, False, False, False, True],
        ),
    ]

    for messages, solution in test_cases:

        log_hashtable = LoggerHashtable()
        log_two_hashtables = LoggerTwoHashtables()

        for (timestamp, message), sol in zip(messages, solution):
            print(f"({timestamp}, {message})")

            res = log_hashtable.should_print_message(timestamp, message)
            output = "         hashtable = "
            output += str(res)
            output += " " * (50 - len(output))
            test_ok = res == sol
            output += f'Test: {"OK" if test_ok else "NOT OK"}'
            print(output)

            res = log_two_hashtables.should_print_message(timestamp, message)
            output = "    two_hashtables = "
            output += str(res)
            output += " " * (50 - len(output))
            test_ok = res == sol
            output += f'Test: {"OK" if test_ok else "NOT OK"}'
            print(output)
            print()
