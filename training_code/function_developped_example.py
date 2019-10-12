import random

def askBookPrice():
    # return a random number between 10 and 80
    price = random.randint(10, 80)
    return price

def canBuyBook(money, price):
    # return True / False
    if price <= money:
        return True
    else:
        return False

def buyBook(money, price):
    # assume that canBuyBook is True here
    # return the amount of money left
    return money - price

def shopAtKinokuniya():
    # the whole logic is here:
    # - returns the number of books bought
    # - as long as have (while) money left, try to buy more books
    # for that, you ask for the price, check if you can buy and buy if you can
    # - if cannot buy book, then exit (break) the loop
    money = random.randint(30, 100)
    print("I have $" + str(money) + " to start with")
    number_of_book = 0
    while money > 0:
        price = askBookPrice()
        print("book price is $" + str(price))
        if canBuyBook(money, price):
            print("I can buy the book")
            money = buyBook(money, price)
            print("I now have $" + str(money) + " left")
            number_of_book = number_of_book + 1
        else:
            print("I cannot buy the book")
            break

    return number_of_book

def isSophieHappy():
    # returns True if Sophie can buy more than 1 book
    # when she goes shopping at Kinokuniya
    num_book = shopAtKinokuniya()
    print("I bought " + str(num_book) + " books")
    if num_book > 1:
        print("Sophie is happy")
    else:
        print("Sophie is not happy")

############### RUN ################
isSophieHappy()