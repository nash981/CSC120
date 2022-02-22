class Counter:
    def __init__(self):
        self.count =0
    
    def increment(self):
        self.count += 1
    def output(self):
        print(self.count)

def main():
    a = Counter()
    b = Counter()
    c = Counter()
    a.increment()
    b.increment()
    c.increment()
    b.increment()
    c.increment()
    c.increment()
    a.output()
    b.output()
    c.output()

if __name__ == "__main__":
    main()