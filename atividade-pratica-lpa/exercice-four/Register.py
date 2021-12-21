
class Register:

    def __init__(self, userName, userEmail, userPhone, userCourse, userActive):
        self.userName = userName
        self.userEmail = userEmail
        self.userPhone = userPhone
        self.userCourse = userCourse
        self.userActive = userActive

    def getUserName(self):
        return self.userName

    def getUserEmail(self):
        return self.userEmail

    def getUserPhone(self):
        return self.userPhone

    def getUserCourse(self):
        return self.userCourse

    def setUserName(self, userName):
        self.userName = userName

    def setUserEmail(self, userEmail):
        self.userEmail = userEmail

    def setUserPhone(self, userPhone):
        self.userPhone = userPhone

    def setUserCourse(self, userCourse):
        self.userCourse = userCourse

    def disable(self):
        self.userActive = False
        print("OFF")

if __name__ == "__main__":

    register1 = Register("Null", "Null", "Null", "Null", True)

    print(register1.getUserName())
