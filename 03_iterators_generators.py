price = [1, 2, 3, 9, 8];

price_iter = price.__iter__()

print(price_iter.__next__())
print(price_iter.__next__())
print(price_iter.__next__())
print()

while True:
    try:
        print(price_iter.__next__())
    except StopIteration:
        break
    
def return_values():
    yield 1
    yield 2
    yield "three"
    
value = return_values()
print(value.__next__())