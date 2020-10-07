from linvie.adapters.csv_reader import UserCsvIO
from linvie.adapters.repository import AbstractUserRepository

class UserRepository(AbstractUserRepository):

    def __init__(self):
        self.data = UserCsvIO("linvie/data/user.csv")
        self.data.read()


    def get_user(self,username):
        pass
