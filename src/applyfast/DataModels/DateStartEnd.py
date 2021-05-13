from datetime import date

class DateStartEnd:
    def __init__(self, s_year, s_month, e_year, e_month):
        self.date_start = date(s_year, s_month, 1)
        self.date_end = date(e_year, e_month, 1)

    def __str__(self):
        return self.date_start.strftime("%b %Y") + " - " + self.date_end.strftime("%b %Y")