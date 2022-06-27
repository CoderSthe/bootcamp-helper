'''
    This is the team allocator project solution example project
'''


def student_list():
    return ['zakithikhDBN2022 - 4 April - Johannesburg Physical - seat 3', 'ddhaalJHB2022 - 2 May - Cape Town Virtual',
    'thandohDBN2022 - 4 April - Phokeng Physical - seat 3', 'zaneleJHB2022 - 2 May - Durban Virtual',
    'ntobekoDBN2022 - 4 April - Phokeng Physical - seat 2', 'BusiJHB2022 - 2 May - Durban Virtual',
    'zinhlehDBN2022 - 4 April - Phokeng Physical - seat 1', 'CebiJHB2022 - 2 May - Durban Virtual',
    'lukhona - 4 April - Phokeng Virtual', 'ddhaalJHB2022 - 2 May - Durban Physical - seat 4',
    'gabiDBN2022 - 4 April - Phokeng Virtual', 'ngakithilJHB2022 - 2 May - Durban Physical - seat 5',
    'zimthembilehDBN2022 - 4 April - Phokeng Virtual', 'ngakuyelJHB2022 - 2 May - Durban Physical - seat 2',
    'zimlindilehDBN2022 - 4 April - Phokeng Virtual', 'yenzileJHB2022 - 2 May - Durban Physical - seat 3',
    'zimthandilehDBN2022 - 4 April - Johannesburg Virtual','kuhlengaweDBN2022 - 4 April - Durban Physical - seat 1',
    'zimkhonzileDBN2022 - 4 April - Johannesburg Virtual','hlelokuhlehDBN2022 - 4 April - Durban Physical - seat 3',
    'zizonkehDBN2022 - 4 April - Johannesburg Virtual','sibusisohDBN2022 - 4 April - Durban Physical - seat 2',
    'kholekileDBN2022 - 4 April - Johannesburg Virtual','vusiDBN2022 - 4 April - Durban Physical - seat 9',
    'kholelwahDBN2022 - 4 April - Johannesburg Virtual','zuzumuzihDBN2022 - 4 April - Durban Physical - seat 10',
    'thembelahDBN2022 - 4 April - Johannesburg Virtual','babazileDBN2022 - 4 April - Durban Physical - seat 11',
    'thembisileDBN2022 - 4 April - Johannesburg Virtual','owenkosiDBN2022 - 4 April - Durban Physical - seat 8',
    'thembisiweDBN2022 - 4 April - Johannesburg Physical - seat 5', 'nobuhleJHB2022 - 2 May - Cape Town Physical',
    'thenjisiweDBN2022 - 4 April - Johannesburg Physical - seat 6', 'nonkonzoJHB2022 - 2 May - Cape Town Physical',
    'thethelelileDBN2022 - 4 April - Johannesburg Physical - seat 7', 'nombusoJHB2022 - 2 May - Cape Town Virtual',
    'thembiDBN2022 - 4 April - Johannesburg Physical - seat 4', 'nozizweJHB2022 - 2 May - Cape Town Virtual']


def dbn_campus_students(student_list):
    dbn_students = []

    for student in student_list:
        if "Durban" in student:
            dbn_students.append(student)

    return dbn_students


def cpt_campus_students(student_list):
    cpt_students = []

    for student in student_list:
        if "Cape Town" in student:
            cpt_students.append(student)

    return cpt_students


def jhb_campus_students(student_list):
    jhb_students = []

    for student in student_list:
        if "Johannesburg" in student:
            jhb_students.append(student)

    return jhb_students


def nw_campus_students(student_list):
    nw_students = []

    for student in student_list:
        if "Phokeng" in student:
            nw_students.append(student)

    return nw_students

    
def dbn_physical_students(dbn_students):
    dbn_physical_students = []

    for student in dbn_students:
        if "Physical" in student:
            dbn_physical_students.append(student)

    return dbn_physical_students


def dbn_physical_teams(dbn_physical_students):
    """Handling of surplus users still needs to be handled.
    Grouping into groups of four handled correctly? Please revisit."""
    dbn_physical_teams = [dbn_physical_students[x : x + 4] for x in range(0, len(dbn_physical_students), 4)]

    return dbn_physical_teams


def dbn_teams_file(durban_physical_teams):
    with open('durban_teams.txt', 'w') as f_reader:
        for team in durban_physical_teams:
            f_reader.write("\n".join(team))
    
    print("Durban teams successfully saved to durban_teams.txt!")



def cpt_physical_students(cpt_students):
    cpt_physical_students = []

    for student in cpt_students:
        if "Physical" in student:
            cpt_physical_students.append(student)
    
    return cpt_physical_students


def cpt_physical_teams(cpt_physical_students):

    cpt_physical_teams = [cpt_physical_students[x : x + 4] for x in range(0, len(cpt_physical_students), 4)]
    
    return cpt_physical_teams


def cpt_teams_file(capetown_physical_teams):
    with open('capetown_teams.txt', 'w') as file_reader:
        for team in capetown_physical_teams:
            file_reader.write("\n".join(team))

    print("Cape Town successfully saved to capetown_teams.txt!")


def jhb_physical_students(jhb_students):
    jhb_physical_students = []

    for student in jhb_students:
        if "Physical" in student:
            jhb_physical_students.append(student)

    return jhb_physical_students


def jhb_physical_teams(jhb_physical_students):

    jhb_physical_teams = [jhb_physical_students[x : x + 4] for x in range(0, len(jhb_physical_students), 4)]

    return jhb_physical_teams

def jhb_teams_file(jhb_physical_teams):
    with open('jhb_teams.txt', 'w') as file_reader:
        for team in jhb_physical_teams:
            file_reader.write("\n".join(team))
    
    print("Johannesburg teams successfully saved to jhb_teams.txt!")


def nw_physical_students(nw_students):
    nw_physical_students = []

    for student in nw_students:
        if "Physical" in student:
            nw_physical_students.append(student)

    return nw_physical_students


def nw_physical_teams(nw_physical_students):

    nw_physical_teams = [nw_physical_students[x : x + 4] for x in range(0, len(nw_physical_students), 4)]

    return nw_physical_teams


def nw_teams_file(nw_physical_teams):
    with open('northwest_teams.txt', 'w') as file_reader:
        for team in nw_physical_teams:
            file_reader.write("\n".join(team))

    print("North West teams successfully saved to northwest_teams.txt!")


def get_virtual_students(student_list):
    virtual_campus = []

    for student in student_list:
        if "Virtual" in student:
            virtual_campus.append(student)

    return virtual_campus


def virtual_teams(virtual_campus):

    virtual_teams = [virtual_campus[x : x + 4] for x in range(0, len(virtual_campus), 4)]

    return virtual_teams


def virtual_teams_file(virtual_teams):
    '''
    write and save the information in the virtual_teams into a textfile
    '''
    with open('virtual_teams.txt', 'w') as file_reader:
        for team in virtual_teams:
            file_reader.write("\n".join(team))

    print("Virtual teams successfully saved to virtual_teams.txt!")


if __name__ == '__main__':
    '''
    call all your functions below to make your program execute    
    '''
    student_list()

    dbn_campus_students(student_list=student_list())
    cpt_campus_students(student_list=student_list())
    jhb_campus_students(student_list=student_list())
    nw_campus_students(student_list=student_list())
    get_virtual_students(student_list=student_list())

    dbn_physical_students(dbn_students=dbn_campus_students(student_list()))
    cpt_physical_students(cpt_students=cpt_campus_students(student_list()))
    jhb_physical_students(jhb_students=jhb_campus_students(student_list()))
    nw_physical_students(nw_students=nw_campus_students(student_list()))

    dbn_physical_teams(dbn_physical_students=dbn_physical_students(dbn_campus_students(student_list())))
    cpt_physical_teams(cpt_physical_students=cpt_physical_students(cpt_campus_students(student_list())))
    jhb_physical_teams(jhb_physical_students=jhb_physical_students(jhb_campus_students(student_list())))
    nw_physical_teams(nw_physical_students=nw_physical_students(nw_campus_students(student_list())))
    virtual_teams(virtual_campus=get_virtual_students(student_list()))

    dbn_teams_file(durban_physical_teams=(dbn_physical_teams(dbn_physical_students(dbn_campus_students(student_list())))))
    cpt_teams_file(capetown_physical_teams=(cpt_physical_teams(cpt_physical_students(cpt_campus_students(student_list())))))
    jhb_teams_file(jhb_physical_teams=(jhb_physical_teams(jhb_physical_students(jhb_campus_students(student_list())))))
    nw_teams_file(nw_physical_teams=(nw_physical_teams(nw_physical_students(nw_campus_students(student_list())))))
    virtual_teams_file(virtual_teams=virtual_teams(get_virtual_students(student_list())))