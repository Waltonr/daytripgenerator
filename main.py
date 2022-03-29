destinations = ["Miami", "Houston", "New York City", "Paris", "St.Croix"]
restaurants = ["Joey's Kitchen", "100 Grill", "L'amour", "Scotch Bonnet", "Oak & Reed"]
transportation = ["a rental car", "the train", "a round-trip flight", "the bus", "an uber"]
entertainment = ["watch a movie", "ride a horse and carriage", "go shopping", "take a group tour", "visit historoic areas"]

import random

chosen_destination  = random.choice(destinations)
chosen_transportation  = random.choice(transportation)
chosen_entertainment  = random.choice(entertainment)
chosen_restaurent  = random.choice(restaurants)



def user_destination(destination_list):
    not_satisfied = True
    while not_satisfied:
        # chosen_destination  = random.choice(destinations)
        user_input = input(f"We have chosen {chosen_destination} as your destination! Is this a good choice? Enter yes/no: ")
        if user_input == "yes":
            print("Great choice!")  
            not_satisfied = False
    return chosen_destination

def user_transportation(transportation_list):
    not_satisfied = True
    while not_satisfied:
        # chosen_transportation  = random.choice(transportation)
        user_input = input(f"We have chosen {chosen_transportation} as your transportation! Is this a good choice? Enter yes/no: ")
        if user_input == "yes":
            print("Great choice! Let's continue.")  
            not_satisfied = False
    return chosen_transportation

def user_entertainment(entertainment_list):
    not_satisfied = True
    while not_satisfied:
        # chosen_entertainment  = random.choice(entertainment)
        user_input = input(f"We have chosen {chosen_entertainment} as your entertainment! Is this a good choice? Enter yes/no: ")
        if user_input == "yes":
            print("Great choice!")  
            not_satisfied = False
    return chosen_entertainment

def user_restaurent(restaurent_list):
    not_satisfied = True
    while not_satisfied:
        # chosen_restaurent  = random.choice(restaurants)
        user_input = input(f"We have chosen {chosen_restaurent} for dinner! Is this a good choice? Enter yes/no: ")
        if user_input == "yes":
            print("Great choice!")  
            not_satisfied = False
    return chosen_restaurent
        

def confirm_trip():
    not_satisfed = True
    while not_satisfed:
        print("Congratulations! Your day trip has been completed. Let's just confirm that this is the trip you desire.")
        print("The trip we have genetrated for you is: ")
        print(f"Destination: {chosen_destination}")
        print(f"Transportation: {chosen_transportation}")
        print(f"Entertainment: {chosen_entertainment}")
        print(f"Restaurant: {chosen_restaurent}")
        user_input = input("Would you like to confirm this trip? Enter yes/no: ")
        if user_input == "yes":
            print(f"Your dream vaction just became reality! You'll be arriving to {chosen_destination} by{chosen_transportation}, where you day will be spent {chosen_entertainment}. You'll end your day dining at {chosen_restaurent}, the best in town. ")
            not_satisfed = False
        
        

user_destination(destinations)
user_transportation(transportation)
user_entertainment(entertainment)
user_restaurent(restaurants)
confirm_trip()
