
class Animal (object):
    """
    This animal
    """
    def __init__(self, species="", domesticated=False, diet=""):
        self.__species = species
        self.__domesticated = domesticated
        self.__diet = diet



    def __str__(self):
        if self.__domesticated:
            return '{0}s are domestic {1}s. '.format(self.__species, self.__diet)
        else:
            return '{0}s are domestic {1}s. '.format(self.__species, self.__diet)

    def set_species(self, species):
        self._species = species

    def get_species(self):
        return self.__species

    def set_domesticated(self, domesticated):
        self.__domesticated = domesticated

    def get_domesticated(self):
        return self.__domesticated

    def set_diet(self, diet):
        self.__diet = diet

    def get_diet(self):
        return self.__diet




class Dog (Animal):
    """
    Attributes: name, breed
      inherited attributes: species, domesticated, diet
    """
    def __init__(self, name="", breed=""):
        Animal.__init__(self, "Dog", True, "Carnivore")
        self.__name = name
        self.__breed = breed


    def __str__(self):
        desc = 'Your Dog, {0}, is a {1}. '.format(self.__name, self.__breed)
        desc += Animal.__str__(self)
        return desc


    #getters and setters

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_diet(self, breed):
        self.__breed = breed

    def get_breed(self):
return self.__breed
