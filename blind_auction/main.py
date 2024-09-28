from replit import clear

from art import logo

def find_highest_bidder(bidder_record):
  highest_bid = 0
  winner = ""
  for bids in bidder_record:
    bid_amount = int(bidder_record[bids])
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bids
  print(f"the winner is {winner} with a bid of ${highest_bid}")    

print(logo)
print("welcome to the secert auction program")
bidders_avail = True
bid_dict = {}
while bidders_avail:
 name = input("What is your name?")
 bid = input("what is your bid $")
 bid_dict[name] = bid
 other_bidders = input("Are there any other bidders? Type 'yes' or 'no'")
 if other_bidders == "no":
   bidders_avail = False
   clear()
 else:
   clear()
find_highest_bidder(bid_dict)



   
  


