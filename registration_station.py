"""
Registration Station project
"""

def read_file():

    """
    Read and return contents of text file
    """
    with open('bootcampers.txt', 'r') as file_reader:
        file_contents = file_reader.readlines()

    return file_contents

def input_user_name(file_contents):
    """
    Takes username as input
    """
    user_name = input("Enter username: ")


def correct_or_incorrect():

    """
    Prompt to ask if details are correct or not
    @return correct or incorrect
    """


def correct_details():

    """
    Prompt to correct and write user details to text file, which includes:
    * Username
    * Date
    * Location
    * Experience
    """

def get_file_contents():

    """Return desired text file"""


def find_username(file_name):

    """
    Main functiontion for running Registration Station, which inlcude:
       * get username input from user
       * check if username exists and print corresponding details
    @return corresponding information for username
       """
    


if __name__ == "__main__":
    registrations_file = read_file()
    information = input_user_name(registrations_file)
    while True:
        answer = correct_or_incorrect()
        if answer == "correct":
            print(information)
            break
        else:
            correct_details()