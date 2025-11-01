class ProgrammingLanguage:
    """Represents a programming language, including information such as type, reflection, and year of appearance"""
    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
    def is_dynamic(self):
        """Determines if it is a dynamically typed language and returns a boolean value"""
        return self.typing.lower() == "dynamic"
    def __str__(self):
        """Returns a formatted string representation"""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"