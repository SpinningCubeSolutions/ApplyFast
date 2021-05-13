class PersonalDetails:
    def __init__(self, givenName1, givenName2, surname, preferredName, address, phoneNumber, email):
        self.givenName1 = givenName1
        self.givenName2 = givenName2
        self.surname = surname
        self.preferredName = preferredName
        self.fullName = f"{self.preferredName} {self.surname}"
        self.address = address
        self.phoneNumber = phoneNumber
        self.email = email

    def __str__(self):
        return f"{self.fullName}\n{self.address}\n{self.phoneNumber}\n{self.email}"
