from models.person import Person

class Patient(Person):
    def __init__(self, id, name, age, ailment):
        super().__init__(id, name, age)
        self.ailment = ailment

    def display_info(self):
        details = super().display_info()
        details["Ailment"] = self.ailment
        return details