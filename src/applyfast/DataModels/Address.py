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
