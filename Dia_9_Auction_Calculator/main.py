logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
price = {}
add = ""

while add != "no":
    print(logo)
    name = input("What is your name?:  ")
    bid = int(input("What is your bid: $"))
    price[name] = bid
    add = input("Type 'yes' if you want to add a new bid, or type 'no' if you want to start the auction: ").lower()
    print("\n"*100)

winner_bid = 0
winner_name = ""
for person in price:
    if winner_bid <= price[person]:
        winner_name = person
        winner_bid = price[person]
print(f"The winner is {winner_name} with a bid of ${winner_bid}")
