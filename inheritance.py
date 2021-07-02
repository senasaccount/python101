#using of __init__(self) with inheritance

class employee():
    def __init__(self):
        self.firstName = ""
        self.lastName = ""
        self.address = ""

class dataScience(employee):
    def __init__(self):
        self.language = ""

class marketing(employee):
    def __init__(self):
        self.storytelling = ""

nurkiz = dataScience()
nurkiz.firstName = "nurkiz"
nurkiz.lastName = "yildiz"
nurkiz.address = "aydin mahallesi"
nurkiz.language = "python"

nurkiz.lastName
nurkiz.language