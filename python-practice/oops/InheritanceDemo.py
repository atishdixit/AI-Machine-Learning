import datetime as dt


class Member:
    expire_date = 365

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.expire_date = dt.date.today() + dt.timedelta(days=self.expire_date)

    def showExpiry(self):
        return f"{self.first_name} {self.last_name} expires on {self.expire_date}"

    def getStatus(self):
        return f"{self.first_name} is a Member"


class Admin(Member):
    expire_date = 365 * 100

    def __init__(self, first_name, last_name, secret_code):
        super().__init__(first_name, last_name)
        self.secret_code = secret_code

    def getStatus(self):
        return f"{self.first_name} is an Admin"


class User(Member):
    def getStatus(self):
        return f"{self.first_name} is a User"


# Here we will test it
member = Member('Hello', 'Hi')
print(member)
print(member.last_name)
print(member.last_name)
print(member.expire_date)
print(member.showExpiry())
print(member.getStatus())

admin = Admin('Admin', 'Admin', "WEDRF")
print(admin)
print(admin.last_name)
print(admin.last_name)
print(admin.expire_date)
print(admin.secret_code)
print(admin.showExpiry())
print(admin.getStatus())

user = User('user', 'user')
print(user)
print(user.last_name)
print(user.last_name)
print(user.expire_date)
print(user.showExpiry())
print(user.getStatus())
