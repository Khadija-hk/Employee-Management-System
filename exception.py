'''This file contains the custom exception classes defined by the user'''

'''This class checks if the entered string contains only alphabetic values'''
class NonAlphabeticNameErrror(Exception):
    def __init__(self, message = "Enter only aplhabetic values!"):
        self.message = message
        super().__init__(self.message)

'''This class checks if the entered date matches the correct format'''
class InvalidDateFormat(Exception):
    def __init__(self, message = "The date format is incorrect!"):
        self.message = message
        super().__init__(self.message)