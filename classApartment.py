class Apartment:
    'This class represents apartments.'
    apartCount = 0
    def __init__(self, zpid = 0):
        self.zpid = zpid
        self.address = ''
        self.rentPerMonth = 0
        Apartment.apartCount += 1

    def set_address(self, address = ''):
        self.address = address

    def set_rate(self, rent = 0):
        self.rentPerMonth = rent

    def display_info(self):
        print('\nzpid: ', self.zpid, '\naddress: ', self.address,
            '\nrentPerMonth: ', self.rentPerMonth, '\n')
