class Qualification:
    def __init__(self, qualificationName, dates):
        self.qualificationName = qualificationName
        self.dates = dates

    def __str__(self):
        return f"{self.qualificationName}, {self.dates}"