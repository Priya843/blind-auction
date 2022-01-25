import art

print(art.logo)

from replit import clear
#HINT: You can call clear() to clear the output in the console.
bids = {}  #creating an empty dict to add key and value


def find_highest_bidder(bidding_record):
    highest_bid = 0
    # bidding_record = {"priya":200,"bts": 500}
    #in dict if we use for loop , it loops each of the key
    winner = ""
    for bidder in bidding_record: #in 1st loop #bidder=priy #bid_amount=200 
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
        print(f"the winner is {winner} with the bid of ${highest_bid}")


bidding_finished = False
while not bidding_finished:
    name = input("What is your name?:")
    price = int(input("What is your bid amount?:$"))
    bids[name] = price
    bidders = input("Is there any other bidders? yes or no:")

    if bidders == "no":
      bidding_finished = True
      find_highest_bidder(bids)
        #print(f"The winner is {name} with the bid of {price} ")
    elif bidders == "yes":
      clear()
        
        #break
