import os
print("***** Welcome to silent auction program *******")
def find_winner(member_details):
    highest_auction = 0
    winner = ""
    for member in member_details:
        member_price = member_details[member]
        if member_price > highest_auction:
            highest_auction = member_price
            winner = member
    print(f"Here is the list of all the members: {member_details}")
    print(f"The winner is {winner} with highest_price of{highest_auction}")
member_data = {}
end_of_auction = False
while not end_of_auction:
    name = input("Enter your name : ")
    price = int(input("Enter your auction price : "))
    member_data[name] = price
    more_members = input("are there more auction members? Type: yes or no: ").lower()
    if more_members == 'no':
        end_of_auction = True
        find_winner(member_data)
    elif more_members == 'yes':
        os.system('cls'if os.name == 'nt' else 'clear')





