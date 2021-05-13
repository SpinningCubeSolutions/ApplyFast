class JobItem:

    def __init__(self, jobTitle, companyName, location, dates, description, duties):
        self.jobTitle = jobTitle
        self.companyName = companyName
        self.location = location
        self.dates = dates
        self.description = description
        self.duties = duties

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
