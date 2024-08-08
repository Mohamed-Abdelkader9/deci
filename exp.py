import os
import time
import google.generativeai as genai
import sys
from codes import list

API_KEY = "AIzaSyBzYcCOWRhjK1XrjJvoBHzOg59NJ012TZc"
genai.configure(api_key=API_KEY)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def delayed_print(message, timee=1.5):
    print(message)
    time.sleep(timee)
    clear_screen()

    

def collect_user_info():
    user_info = {}

    # Bad Habits
    while True:
        clear_screen()
        print("Do you have any bad habits? (yes/no)")
        bad_habits = input().lower()
        if bad_habits == "yes":
            user_info["bad_habits"] = input("Please describe your bad habits: ")
            break
        elif bad_habits == "no":
            print("This app is used to help who have bad habits")
            sys.exit()
        else:
            delayed_print("please enter a valid input")


    # Job
    while True:
        clear_screen()
        user_info["job"] = input("What is your job title? ")
        if user_info["job"].strip() != "":
            break
        else:
            delayed_print("Invalid input. Please enter a valid job title.")

    # Family Role
    while True:
        clear_screen()
        print("What is your family role? (e.g. mother, father, sibling, etc.)")
        user_info["family_role"] = input()
        if user_info["family_role"].strip() != "":
            break
        else:
            delayed_print("Invalid input. Please enter a valid family role.")

    # Allergies
    while True:
        clear_screen()
        print("Do you have any allergies? (yes/no)")
        allergies = input().lower()
        if allergies in ["yes", "no"]:
            if allergies == "yes":
                user_info["allergies"] = input("Please describe your allergies: ")
            else:
                user_info["allergies"] = "None"
            break
        else:
            delayed_print("Invalid input. Please enter 'yes' or 'no'.")

    # Other Relevant Information
    while True:
        clear_screen()
        user_info["other_info"] = input("Is there any other relevant information you'd like to share? ")
        if user_info["other_info"].strip() != "":
            break
        else:
            delayed_print("Invalid input. Please enter some information.")
        
    return user_info

def program():
    user_info = {}

    while True:
        clear_screen()
        name = input("What's your name? ")
        if name.isalpha():  # Check if the input contains only letters
            user_info["name"] = name.upper()
            break
        else:
            delayed_print("Invalid input. Please enter your name.")

    while True:
        clear_screen()
        code = input("Enter your cash code:")
        if code in list:
            user_info["cash_code"] = code
            break
        else:
            delayed_print("Invalid code. Please enter your cash code.")

    while True:
        clear_screen()
        email = input("Enter your email address:")
        if "@" in email and email.count("@") == 1:
            local_part, domain = email.split("@")
            if local_part and domain:  # Check if there's something before and after the @ symbol
                domain_parts = domain.split(".")
                if len(domain_parts) == 2:  # Check if there's a top-level domain
                    tld = domain_parts[1]
                    if tld in ["com", "org", "net", "edu", "gov", "mil", "biz", "info"]:  # Check if the TLD is valid
                        user_info["email"] = email
                        break
                    else:
                        delayed_print("Invalid email address. Please use a valid top-level domain (e.g. .com, .org, etc.).")
                else:
                    delayed_print("Invalid email address. Please enter a valid domain (e.g. example.com).")
            else:
                delayed_print("Invalid email address. Please enter something before and after the @ symbol.")
        else:
            delayed_print("Invalid email address. Please try again.")

    clear_screen()
    print("\nUser Information:")
    for key, value in user_info.items():
        print(f"{key.capitalize()}: {value}")
    time.sleep(2)  # wait for 2 seconds before clearing the screen

    clear_screen()
    user_info2 = collect_user_info()
    #delayed_print("Bad Habits: " + user_info2["bad_habits"])
    #delayed_print("Job: " + user_info2["job"])
    #delayed_print("Family Role: " + user_info2["family_role"])
    #delayed_print("Allergies: " + user_info2["allergies"])

    model = genai.GenerativeModel(model_name='gemini-1.5-flash')
    user_info2_str = "Bad Habits: " + user_info2["bad_habits"] + "\nJob: " + user_info2["job"] + "\nFamily Role: " + user_info2["family_role"] + "\nAllergies: " + user_info2["allergies"] + "  if the previous text is not understandable reply with your data seems to be incorrect so i cannot help you and if there is nothing wrong with it reply with advices to his case but use raw text only (no markup)"
    try:
        response = model.generate_content(user_info2_str)
        print(response.text)
    except Exception as e:
        print(f"An error occurred: {e}")
        

    def try_agains():
        try_again = input("Do you want any other help? (yes/no) ")
        if try_again.lower() == "yes":
            program()
        elif try_again.lower() == "no":
            print("Thanks for using our app...Good Bye")
            sys.exit()
        else:
            print("Invalid input. Please enter yes or no.")
            try_agains()
    try_agains()
    
    

program()
