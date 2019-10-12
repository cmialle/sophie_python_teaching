# 1. what is in my bag?
bag = {"pens": 10, "books": 3, "lipsticks": 25, "umbrella": 2}
print("in my bag i have "
      + str(bag.get('pens', 0)) + " pens, \n"
      + str(bag.get("books", 0)) + " books, \n"
      + str(bag.get("lipsticks", 0)) + " lipsticks, \n"
      + str(bag.get("umbrella", 0)) + " umbrella, \n"
      + str(bag.get("bananas", 0)) + " bananas.")

bag["bananas"] = 4
bag["tissues"] = 23

print("in my bag i have")
for k, v in bag.items():
    print(str(v) + " " + k)

# 2. count number of occurences for each word in words
words = ["hello", "cat", "bat", "pig", "cat", "cat", "pig", "pig", "bat", "booboo"]
result = {}

for element in words:
    if element not in result:
        result[element] = 1
    else:
        val = result[element]
        result[element] = val + 1

# same as above but more elegant
# for element in words:
#     result.setdefault(element, 0)
#     val = result[element]
#     result[element] = val + 1

for k, v in result.items():
    print(k + ":" + str(v))

