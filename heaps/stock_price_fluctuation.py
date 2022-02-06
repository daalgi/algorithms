"""
https://leetcode.com/problems/stock-price-fluctuation/

You are given a stream of records about a particular stock. 
Each record contains a timestamp and the corresponding 
price of the stock at that timestamp.

Unfortunately due to the volatile nature of the stock 
market, the records do not come in order. Even worse, 
some records may be incorrect. Another record with the 
same timestamp may appear later in the stream correcting 
the price of the previous wrong record.

Design an algorithm that:
- Updates the price of the stock at a particular timestamp, 
correcting the price from any previous records at 
the timestamp.
- Finds the latest price of the stock based on the current 
records. The latest price is the price at the latest 
timestamp recorded.
- Finds the maximum price the stock has been based on 
the current records.
- Finds the minimum price the stock has been based on 
- the current records.

Implement the StockPrice class:
- StockPrice() Initializes the object with no 
price records.
- void update(int timestamp, int price) Updates the 
price of the stock at the given timestamp.
- int current() Returns the latest price of the stock.
- int maximum() Returns the maximum price of the stock.
- int minimum() Returns the minimum price of the stock.
 
Example 1:
Input
["StockPrice", "update", "update", "current", "maximum", 
"update", "maximum", "update", "minimum"]
[[], [1, 10], [2, 5], [], [], [1, 3], [], [4, 2], []]
Output
[null, null, null, 5, 10, null, 5, null, 2]

Explanation
StockPrice stockPrice = new StockPrice();
// Timestamps are [1] with corresponding prices [10].
stockPrice.update(1, 10);
// Timestamps are [1,2] with corresponding prices [10,5].
stockPrice.update(2, 5);
// return 5, the latest timestamp is 2 with the price being 5.
stockPrice.current();
// return 10, the maximum price is 10 at timestamp 1.
stockPrice.maximum();
// The previous timestamp 1 had the wrong price, so it is updated to 3.
// Timestamps are [1,2] with corresponding prices [3,5].
stockPrice.update(1, 3);
// return 5, the maximum price is 5 after the correction.                          
stockPrice.maximum();
// Timestamps are [1,2,4] with corresponding prices [3,5,2].
stockPrice.update(4, 2);
// return 2, the minimum price is 2 at timestamp 4.
stockPrice.minimum();

Constraints:
1 <= timestamp, price <= 10^9
At most 105 calls will be made in total to update, 
current, maximum, and minimum.
current, maximum, and minimum will be called only 
after update has been called at least once.
"""
import heapq


class StockPriceTwoHeaps:
    def __init__(self):
        # Time complexity: O(1)
        # Space complexity: O(n) as the prices are `updated`
        self.last_timestamp = 0
        # Hashmap to store the current state of prices
        # { timestamp: price }
        self.prices = {}
        # max-heap of tuples (-price, timestamp)
        self.max_prices = []
        # min-heap of tuples (+price, timestamp)
        self.min_prices = []

    def update(self, timestamp: int, price: int) -> None:
        # Time complexity: O(logn)
        self.prices[timestamp] = price
        heapq.heappush(self.max_prices, (-price, timestamp))
        heapq.heappush(self.min_prices, (price, timestamp))
        if timestamp > self.last_timestamp:
            self.last_timestamp = timestamp

    def current(self) -> int:
        # Time complexity: O(1)
        return self.prices[self.last_timestamp]

    def maximum(self) -> int:
        # Time complexity: O(logn)
        # The heap stores all the history of values if not popped,
        # so the top elements might not correspond with the current
        # state of `prices`.
        # To solve that, pop all the values until the timestamp
        # between the last updated value stored in in the hasmap
        # `prices` and the `max_prices` heap coincides.
        while self.prices[self.max_prices[0][1]] != -self.max_prices[0][0]:
            heapq.heappop(self.max_prices)
        return -self.max_prices[0][0]

    def minimum(self) -> int:
        # Time complexity: O(logn)
        while self.prices[self.min_prices[0][1]] != self.min_prices[0][0]:
            heapq.heappop(self.min_prices)
        return self.min_prices[0][0]


if __name__ == "__main__":
    print("-" * 60)
    print("Stock price fluctuation")
    print("-" * 60)

    prices = [
        (1, 8),
        (2, 9),
        (3, 10),
        (2, 13),
        (2, 3),
    ]

    sp = StockPriceTwoHeaps()

    for timestamp, price in prices:

        print("Timestamp:", timestamp)
        print("Price:", price)

        sp.update(timestamp, price)
        output = "   two_heaps.update()"
        output += f"\n   two_heaps.current() = {sp.current()}"
        output += f"\n   two_heaps.maximum() = {sp.maximum()}"
        output += f"\n   two_heaps.minimum() = {sp.minimum()}"

        print(output)

        print()
