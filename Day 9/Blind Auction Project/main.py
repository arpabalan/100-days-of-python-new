from art import logo
print(logo)

bidder = {}
transaction = True
counter = 0
bids = []
while transaction != False:
    # TODO-1: Ask the user for input
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: "))
    # TODO-2: Save data into dictionary {name: price}

    bidder[f"bidder_{counter}"] =  {
        "name":name,
        "bid":bid
    }
    counter += 1
    bids.append(bid)
    # TODO-3: Whether if new bids need to be added

    adding_bidder = input("Are there a new bidder Yes or No? :").lower()
    # TODO-4: Compare bids in dictionary
    print("\n" * 20)
    if adding_bidder == 'no':
        transaction = False
        for x in bidder.values():
            if int(x['bid']) == max(bids):
                print(f"The winner is {x['name']} with the bid off {x['bid']}")








