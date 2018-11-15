import random
rate = random.random()
print (rate)
print (random.randint(0,99))
print (random.uniform(10, 20))
items = [1, 2, 3, 4, 5, 6]
print (random.choice(items))
random.shuffle(items)
print (items)
print (random.sample('abcdefghij',3))
print (random.randrange(0, 101, 2))