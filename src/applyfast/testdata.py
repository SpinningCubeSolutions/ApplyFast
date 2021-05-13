from DataModels import PersonalDetails, Address

addy = Address.Address("555 Meow st","Meow Gardens", "Mew York City", "Mew York","55555","Mew Zealand")
pd = PersonalDetails.PersonalDetails("Robert", "John", "The Builder", "Bob", addy, "0800 BobCanFixIt", "bob@bob.com")
print(pd)

