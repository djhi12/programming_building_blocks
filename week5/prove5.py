print()

# Adventure Game
items = input("You are walking through the dark forest and find two items: a MATCH and a FLASHLIGHT. Which one do you want to pick up? ")

print()

# Match
if items.lower() == "match":
    run_walk_hide = input("You pick up the match and strike it, and for an instant, the forest around you is illuminated. You see a large grizzly bear, and then the match burns out. Do you want to RUN, WALK SLOWLY, or HIDE behind the tree? ")

    # Run
    if run_walk_hide.lower() == "run":
        print("You have to run as fast as you could so that the bear cannot catch you. \n")

    # Hide
    elif run_walk_hide.lower() == "hide":
        print("Try not to panic; remain as quiet as possible \n")

    # Walk slowly
    elif run_walk_hide.lower() == "walk slowly":
        print("Walk away slowly, if the bear is not approaching \n")

    else:
        print("Remain still and calm. \n")

elif items.lower() == "flashlight":
    follow_look = input("You pick up the flashlight and turn it on. You see the pathway lit up in front of you, but you thought you also heard something off to the side. Do you want to FOLLOW the path or LOOK in the trees for the thing that made the noise? ")

    print()

    # Follw
    if follow_look.lower() == "follow":
        print("Move away quietly. \n")

    # Look
    elif follow_look.lower() == "look":
        print("If you see it, fight back with anything at hand (knife, sticks, rocks, or by kicking it). \n")

    else:
        print("Remain still and calm. \n")

# Bear spray
else:
    print("Use a bear spray and if the bear is within ten yeards (30 feet), spray in a zigzag pattern to put a cloud of spray between yourself and the bear. \n")



