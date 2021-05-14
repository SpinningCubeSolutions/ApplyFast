
class CV:
    def __init__(
            self,
            applicantDetails,
            skills,
            workHistory,
            volunteerHistory,
            personalProfile,
            educationHistory,
            achievements,
            referees
    ):
        self.referees = referees
        self.achievements = achievements
        self.educationHistory = educationHistory
        self.personalProfile = personalProfile
        self.volunteerHistory = volunteerHistory
        self.workHistory = workHistory
        self.applicantDetails = applicantDetails
        self.skills = skills

    def __str__(self):
        base_str = f"{self.applicantDetails}\n{self.personalProfile}\n"
        for a in self.achievements:
            base_str += a + "\n"
        for s in self.skills:
            base_str += s + "\n"
        for w in self.workHistory:
            base_str += str(w) + "\n"
        if self.volunteerHistory is not None:
            for v in self.volunteerHistory:
                base_str += str(v) + "\n"
        for e in self.educationHistory:
            base_str += str(e) + "\n"
        for r in self.referees:
            base_str += str(r) + "\n"

        return base_str
