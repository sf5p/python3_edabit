class Name:
    def __init__(self, first_name, last_name):
        self.fname = f'{first_name}'.title()
        self.lname = f'{last_name}'.title()
        self.fullname = f'{first_name} {last_name}'.title()
        self.initials = f'{first_name[0]}.{last_name[0]}'.upper()
