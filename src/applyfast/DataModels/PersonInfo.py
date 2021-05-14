class Address:
    def __init__(self, address1, address2, city, state, postcode, country):
        self.address1 = address1
        self.address2 = address2
        self.city = city
        self.state = state
        self.postcode = postcode
        self.country = country

    def __str__(self):
        base_str = self.address1 + "\n"
        if self.address2 is not None:
            base_str += self.address2 + "\n"
        base_str += f"{self.city} {self.postcode}\n"
        if self.state is not None:
            base_str += self.state + "\n"
        base_str += self.country
        return base_str


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


class JobPersonDetails(PersonalDetails):
    def __init__(self,
                 givenName1,
                 givenName2,
                 surname,
                 preferredName,
                 address,
                 phoneNumber,
                 email,
                 jobTitle,
                 companyName):
        super(JobPersonDetails, self).__init__(givenName1, givenName2, surname, preferredName, address, phoneNumber,
                                               email)
        self.jobTitle = jobTitle
        self.companyName = companyName

    def __str__(self):
        return f"{self.fullName}\n{self.jobTitle}, {self.companyName}\n{self.address}\n{self.phoneNumber}\n{self.email}"


class ApplicantDetails(PersonalDetails):
    def __init__(self,
                 givenName1,
                 givenName2,
                 surname,
                 preferredName,
                 address,
                 phoneNumber,
                 email,
                 website,
                 linkedInProfile):
        super(ApplicantDetails, self).__init__(givenName1, givenName2, surname, preferredName, address, phoneNumber,
                                               email)
        self.website = website
        self.linkedInProfile = linkedInProfile

    def __str__(self):
        return f"{self.fullName}\n{self.address}\n{self.phoneNumber}\n{self.email}\n{self.website}\n{self.linkedInProfile}"


class Referee(JobPersonDetails):
    def __init__(self,
                 givenName1,
                 givenName2,
                 surname,
                 preferredName,
                 address,
                 phoneNumber,
                 email,
                 jobTitle,
                 companyName,
                 website):
        super(Referee, self).__init__(givenName1, givenName2, surname, preferredName, address, phoneNumber, email, jobTitle, companyName)
        self.website = website

    def __str__(self):
        return f"{self.fullName}\n{self.jobTitle}, {self.companyName}\n{self.address}\n{self.phoneNumber}\n{self.email}\n{self.website}"

