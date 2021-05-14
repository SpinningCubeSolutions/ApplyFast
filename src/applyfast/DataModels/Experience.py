from datetime import date


class DateStartEnd:
    def __init__(self, sYear, sMonth, eYear, eMonth):
        self.date_start = date(sYear, sMonth, 1)
        self.date_end = date(eYear, eMonth, 1)

    def __str__(self):
        return self.date_start.strftime("%b %Y") + " - " + self.date_end.strftime("%b %Y")


class JobItem:

    def __init__(self, jobTitle, companyName, location, dates, description, duties, isVolunteer=False):
        self.jobTitle = jobTitle
        self.companyName = companyName
        self.location = location
        self.dates = dates
        self.description = description
        self.duties = duties
        self.isVolunteer = isVolunteer

    def __str__(self):
        base_str = f"{self.jobTitle} at {self.companyName} in {self.location}\n{self.dates}\n"
        if self.description is not None:
            base_str += self.description
        duty_str = "\nDuties included:\n"
        if self.duties is not None:
            if type(self.duties) is not list:
                pass
            else:
                for duty in self.duties:
                    duty_str += f" - {duty}\n"
                base_str += duty_str

        return base_str


class Qualification:
    def __init__(self, qualificationName, subject, dates):
        self.qualificationName = qualificationName
        self.subject = subject
        self.dates = dates

    def __str__(self):
        return f"{self.qualificationName}, {self.dates}"


class EducationItem:
    def __init__(self, educationProvider, qualifications):
        self.educationProvider = educationProvider
        self.qualifications = qualifications

    def __str__(self):
        base_str = f"{self.educationProvider}\n"
        for qual in self.qualifications:
            base_str += f"{qual}\n"

        return base_str
