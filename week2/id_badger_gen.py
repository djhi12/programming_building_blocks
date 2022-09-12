
# type first name
first_name = input("\nWhat is your first name? ")

# type last name
last_name = input("What is your last name? ")

# type email address
email_add = input("What is your email address? ")

# type phone number
phone_num = input("What is your phone number? ")

# type job title
job_title = input("What is you job title? ")

# type id number
id_num = input("What is your id number? ")

# stretch activity
hair_color = input("What is your hair color? ")
eye_color = input("What is your eye color? ")
month_start = input("Type month started: ")
training = input("Do you have training? ")

# next line
print()

# ID Card
print("The ID Card is:")
print("--------------------")
print(f"{last_name.upper()}, {first_name}\n{job_title.title()}\nID: {id_num}\n{email_add.lower()}\n{phone_num} \nHair color: {hair_color}   Eyes color: {eye_color} \nMonth:{month_start}  Training: {training}")
print("-------------------- \n")
