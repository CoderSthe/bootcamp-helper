from xml.dom import UserDataHandler
 
def user_details():
    current_year = 2022
    f_name = input("First Name: ").lower()
    l_name = input("Last Name: ").lower()
    c_year = current_year

    campus = input("Campus: ").title()
    while (campus != "Johannesburg") and (campus != "Durban") and (campus != "Cape Town") and (campus != "Phokeng"):
        print("You have entered an invalid campus. Please try again.")
        campus = input("Campus: ")

    create_user_name(f_name, l_name, c_year, user_campus(campus))


def create_user_name(first_name, last_name, cohort, final_campus):
    if len(first_name) < 3:
        first_name = (first_name + 'o')
    last_three = first_name[-3:]
    first_three = last_name[:3]
    
    username = f"{last_three}{first_three}{final_campus}{cohort}"

    print(f"Final username:\n\n{username}\n")
    print(f"Format for the username:\n\n{last_three.upper()} - Last three letters of first name\n{first_three.upper()} - First three letters of last name")
    print(f"{final_campus} - Abbreviated name for chosen campus\n{cohort} - Year of registration")

    response = input("Is the final name correct? Y/N\n").lower()
    if response == 'n':
        user_details()
    else:
        print("Username saved.")


def user_campus(campus):
    if campus == "Johannesburg":
        abbr = "JHB"
    elif campus == "Cape Town":
        abbr = "CPT"
    elif campus == "Durban":
        abbr = "DBN"
    else:
        abbr = "PHO"
    
    return abbr


if __name__ == '__main__':
    user_details()