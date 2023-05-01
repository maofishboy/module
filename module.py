import random
r = random.randint(1,100)
print(r)
g = 0
while g != r:
    g = input("請猜一組數字: ")
    g = int(g)
    if g == r:
        print('終於猜對了')
    else:
        if g > r:
            print('比答案大')
        elif g < r:
        	print('比答案小')