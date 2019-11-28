from database import Database
from user import User

Database.initialise()

# Saving to the DB
my_user = User('fredblogs@gmail.com','Fred','Blogs','fblogs001')
print(my_user.email)
my_user.save_to_db()


# Loading From the DB
user_from_db = User.load_from_db_by_email('fredblogs@gmail.com')
print(user_from_db)