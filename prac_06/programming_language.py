class ProgrammingLanguage:
    def __init__(self, name="", typing="Static", is_reflection=False, year=0):
        self.name = name
        self.typing = typing
        self.is_reflection = is_reflection
        self.year = year

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.is_reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        return self.typing == "Dynamic"
