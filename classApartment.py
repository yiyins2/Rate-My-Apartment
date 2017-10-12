class Apartment:
    'This class represents apartments.'
    apartCount = 0
    def __init__(self, zpid = 0):
        self.__zpid = zpid
        self.__address = ''
        self.__rentPerMonth = 0
        Apartment.apartCount += 1
    def get_zpid(self):
        return self.__zpid

    def set_address(self, address = ''):
        self.__address = address
    def get_address(self):
        return self.__address


    def set_rate(self, rent = 0):
        self.__rentPerMonth = rent
    def get_rate(self):
        return self.__rentPerMonth

    def display_info(self):
        print('\nzpid: ', self.get_zpid(), '\naddress: ', self.get_address(),
            '\nrentPerMonth: ', self.get_rate(), '\n')
