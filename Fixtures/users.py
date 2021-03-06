from Fixtures.database import DatabaseHelper
from Model.User import User

class Users:
    def __init__(self):
        # Initialize database helper class
        self.db_helper = DatabaseHelper()
        self.accounts = {}


    def get_users_from_db(self, platform):
        query = "select a.user, u.* from Accounts as a join Users as u " \
                "where a.UserId == u.Id and a.platform == '{0}';".format(platform)
        db_users = self.db_helper.execute_query(query)
        for user in db_users:
            self.accounts[user[0]] = User(user[1:])

    def save_users_to_db(self):
        pass

    def __repr__(self):
        result = ''
        for key in self.accounts:
            result += '{}: {}/n'.format(key, self.accounts[key])
        return result






