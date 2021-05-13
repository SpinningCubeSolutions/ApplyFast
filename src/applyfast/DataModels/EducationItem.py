class EducationItem:
    def __init__(self, educationProvider, qualifications):
        self.educationProvider = educationProvider
        self.qualifications = qualifications

    def __str__(self):
        base_str = f"{self.educationProvider}\n"
        for qual in self.qualifications:
            base_str += f"{qual}\n"

        return base_str

