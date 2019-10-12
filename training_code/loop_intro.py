# 1. for loop
s = ''
for i in range(5):
    # print("at each iteration I add one *")
    print("iteration" + str(i))
    s = s + '*'
    print(s)

# 2. for loop
sum = 0
for i in range(10):
    print("I add " + str(i+1) + " to the sum")
    sum = sum + (i+1)
    print("at iteration " + str(i) + ", the sum is " + str(sum))

# 3. while loop - similar to 2.
sum = 0
count = 0
while count < 10:
    sum = sum +(count + 1)
    count = count + 1

print(sum)
