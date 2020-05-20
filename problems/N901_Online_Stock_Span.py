class StockSpanner:

    def __init__(self):
        self.prices = []

    def next(self, price: int) -> int:
        if not self.prices:
            self.prices.append((price,1))
            return 1
        else:
            count = 1
            while self.prices:
                previous, num = self.prices[-1]
                if price < previous:
                    break
                else:
                    self.prices.pop()
                    count += num
            self.prices.append((price,count))
            return count

if __name__ == "__main__":
    stock = StockSpanner()
    for price in [100, 80, 60, 70, 60, 75, 85]:
        n = stock.next(price)
        print(n)