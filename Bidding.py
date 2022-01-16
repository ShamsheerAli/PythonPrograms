from turtle import clear


bids={}
def highest(record):
    high=0
    winner=""
    for i in record:
        amount=record[i]
        if amount > high:
            high=amount
            winner=i
    print(f"The winner is{winner} with Amount of{high}")        
name=input("Enter The Name")
value=int(input("Enter The Price"))
bidding_finished= False
while not bidding_finished:
    bids[name]=value
    extra=input("Are There Any Bidders To add? y or n")
    if extra=="n":
     bidding_finished=True
    elif extra=="y":
      clear()
highest(bids)      