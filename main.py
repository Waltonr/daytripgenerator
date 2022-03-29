destinations = ["Miami", "Houston", "New York City", "Paris", "St.Croix"]
restaurants = ["Joey's Kitchen", "100 Grill", "L'amour", "Scotch Bonnet", "Oak & Reed"]
transportations = ["a rental car", "the train", "a round-trip flight", " the bus", "an uber"]
entertainments = ["watch a movie", "ride a horse and carriage", "go shopping", "take a group tour", "visit historoic areas"]

import random

# chosen_destination  = random.choice(destinations)
# chosen_transportation  = random.choice(transportation)
# chosen_entertainment  = random.choice(entertainment)
# chosen_restaurent  = random.choice(restaurants)



def user_destination(destination_list):
    not_satisfied = True
    while not_satisfied:
        chosen_destination = random.choice(destinations)
        user_input = input(f"We have chosen {chosen_destination} as your destination! Is this a good choice? Enter yes/no: ")
        if user_input == "yes":
            print("Great choice!")  
            not_satisfied = False
        elif user_input == "no":
            chosen_destination = random.choice(destinations)
    return chosen_destination
 

def user_transportation(transportation_list):
    not_satisfied = True
    while not_satisfied:
        chosen_transportation  = random.choice(transportations)
        user_input = input(f"We have chosen {chosen_transportation} as your transportation! Is this a good choice? Enter yes/no: ")
        if user_input == "yes":
            print("Great choice! Let's continue.")  
            not_satisfied = False
    return chosen_transportation

# the_transportation = chosen_transportation

def user_entertainment(entertainment_list):
    not_satisfied = True
    while not_satisfied:
        chosen_entertainment  = random.choice(entertainments)
        user_input = input(f"We have chosen {chosen_entertainment} as your entertainment! Is this a good choice? Enter yes/no: ")
        if user_input == "yes":
            print("Great choice!")  
            not_satisfied = False
    return chosen_entertainment

# the_entertainment = chosen_entertainment

def user_restaurent(restaurent_list):
    not_satisfied = True
    while not_satisfied:
        chosen_restaurent  = random.choice(restaurants)
        user_input = input(f"We have chosen {chosen_restaurent} for dinner! Is this a good choice? Enter yes/no: ")
        if user_input == "yes":
            print("Great choice!")  
            not_satisfied = False
    return chosen_restaurent

# the_resaturant = chosen_restaurent
      

def confirm_trip(destination, transportation, entertainment, restaurant):
    print("Congratulations! Your day trip has been completed. Let's just confirm that this is the trip you desire.")
    print("The trip we have genetrated for you is: ")
    print(f"Destination: {the_destination}")
    print(f"Transportation: {the_transportation}")
    print(f"Entertainment: {the_entertainment}")
    print(f"Restaurant: {the_restaurant}")
    not_satisfed = True
    while not_satisfed:
        user_input = input("Would you like to confirm this trip? Enter yes/no: ")
        if user_input == "yes":
            print(f"Your dream vaction just became reality! You'll be arriving to {the_destination} via {the_transportation}, where you day will be spent {the_entertainment}. You'll end your day dining at {the_restaurant}, the best in town. ")
            not_satisfed = False
        
        
the_destination = user_destination(destinations)
the_transportation = user_transportation(transportations)
the_entertainment = user_entertainment(entertainments)
the_restaurant = user_restaurent(restaurants)

confirm_trip(the_destination, the_transportation, the_entertainment, the_restaurant)
