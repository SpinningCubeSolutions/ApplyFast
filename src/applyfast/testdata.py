from DataModels.PersonInfo import ApplicantDetails, Referee, Address
from DataModels.Experience import *
from DataModels.CVData import CV

workEx = [
    JobItem(jobTitle="Cat Patter", companyName="Big Purrs Cattery", location="Mew York", dates=DateStartEnd(2017,2,2018,10), description="Was responsible for patting cats and playing with them", duties=["Patted cats", "cuddled cats", "fed cats"], isVolunteer=False),
    JobItem(jobTitle="Clown", companyName="Purry Bros. Circus", location="Funtown", dates=DateStartEnd(2019,2,2019,9), description="Performed tricks in a Muggle circus", duties=["Wore funny costume", "Juggled balls and knives", "Got hit in face with pie"], isVolunteer=False)
]

edEx = [
    EducationItem("Hogwarts School of Witchcraft and Wizardry", [Qualification("NEWTs", "Transfiguration, Charms, Potions", DateStartEnd(2004, 3, 2007, 9))]),
    EducationItem("Rowena Ravenclaw Univesity", [Qualification("Bachelor of Wizardry", "Defensive Magic", DateStartEnd(2008, 2, 2010,10))])
]

volEx = [JobItem(jobTitle="Sales Assistant (intern)", companyName="Borgin and Burkes", location="Knockturn Alley, London", dates=DateStartEnd(2013,4,2012,9), description="Basic shop work", duties=["Stocking shelves", "Serving customers", "Acquiring items"])]

details = ApplicantDetails("Neville", "Augustus", "Shortbottom", "Nev", Address("55 Grimauld Place", "Winnigsby", "London", "London", "HP7 WB8", "England"), "+44 555 1234", "nev@magicnet.uk", None, None)

referees = [Referee("Minerva", "Athena", "McGonagall", "Minnie",
                    Address("Hogwarts School of Witchcraft and Wizardry", "1 Hog Road", "Hogsmeade", "Loch Lomond", "HW1 HM3", "Scotland"),
                    "0800 HOGWARTS", "minerva@hogwarts.edu.uk", "Headmistress", "Hogwarts School of Witchcraft and Wizardry", "www.hogwarts.edu.uk"),
            Referee("Walter", "Waldo", "Wizard", "Wally",
                    Address("88 Zizzy St", "Peckham", "London", "London", "G98 V63", "England"),
                    "0800 WALLYWIZ", "wallythewizard@wizmail.co.uk", "Auror", "Ministry of Magic", "ministryofmagic.govt.uk")
            ]

skills = ["Transfiguration", "Defensive Magic", "Offensive Magic", "Hexes", "Curse breaking"]
achievements = ["Dux of Hogwarts School of Witchcraft and Wizardry", "Winner of Newt Scamander Scholarship", "2nd Place in Witch Weekly's Sexiest Wizard Competition"]
personalProfile = "Highly motivated wizard seeking employment in wizarding world after spending years working in the " \
                  "Muggle world. Expert at offensive and defensive magic, hexes and curse breaking. Previously worked in a Muggle circus and at a cattery"

mycv = CV(personalProfile=personalProfile, applicantDetails=details, workHistory=workEx, volunteerHistory=volEx, educationHistory=edEx, skills=skills, achievements=achievements, referees=referees)
with open("testcv.bigpurrs", "w") as f:
    f.write(str(mycv))