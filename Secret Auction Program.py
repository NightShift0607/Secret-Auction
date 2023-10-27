print('''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                         `'-------'`
                       .-------------.
                      /_______________\\
''')
print("Welcome to the secret auction program.")

import subprocess

bidding_details = {}  #global variable

def add_data(name_add, bid_add):
    bidding_details[name_add] = bid_add

def highest_bidder():
    max_bid = 0
    max_bid_name = ""
    for name in bidding_details:
        if max_bid < bidding_details[name]:
            max_bid = bidding_details[name]
            max_bid_name = name
    subprocess.run("cls", shell=True)     #for clearing screen
    print(f"The winner is {max_bid_name} with a bid of ${max_bid}.")

while True:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    add_data(name, bid)
    more = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if more == "no":
        highest_bidder()
        break
    else:
        subprocess.run("cls", shell=True)     #for clearing screen
