class Animal:

    def __init__(self, name, color):
        self.name = name
        self.color = color

    @classmethod
    def get_list(cls):
        animals = [
            cls("Jirafa", "Naranja"),
            cls("Cebra", "Blanco y negro"),
            cls("Xenomorfo", "Negro")
        ]
        return animals