class dataScientist():
    employees = []
    def __init__(self):
        self.languages = []
        self.department = ''
    def add_language(self, new_language):
        self.languages.append(new_language)        

dilara = dataScientist()
pitircik = dataScientist()

pitircik.add_language("R")
print(pitircik.languages)
print(dilara.languages)