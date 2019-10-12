

def list_to_string(list):
    theString = ""

    for i in range(len(list)):
        if i == len(list) - 1:
            theString = theString + "and " + str(list[i]) + "."

        else:
            theString = theString + str(list[i]) + ", "
    return theString

def printListIndex(list):
    for element in list:
        print(element + " " +str(list.index(element)))

def printIndexInRange(list):
    for i in range(len(list)):
        print(list[i] + " " +str(i))

list = ["apple", "banana", "tofu", "cats"]  # "apple, banana, tofu, and cats"
list1 = ["fish", "cat", "dog", "dolphin", "bear", "birds", "cat"]
# print(list_to_string(list1))
printListIndex(list1)
print("\n")
printIndexInRange(list1)



# you want : "fish, cat, dog, dolphin, bear, birds, AND cat"
# you get the wrong result because at the second iteration you compare "cat" (second element of your list)
# to "cat" (last element of your list) and obviously "cat" == "cat", that is why you get
# fish, and cat.dog,
# what you want to do is simply to check whether you are at the last iteration,
# that is why, better to use indices in this case...