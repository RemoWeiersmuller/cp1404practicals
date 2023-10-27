"""
languages
Estimate: 20 minutes
Actual:   25 minutes
Store a list of programming languages and give back th dynamic typed ones.
"""

from programming_language import ProgrammingLanguage


def main():
    """Store a list of programming languages and give back the dynamic typed ones."""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)

    programminglanguages = [python, ruby, visual_basic]
    print("The dynamically typed languages are:")
    for language in programminglanguages:
        if language.is_dynamic():
            print(language.name)


main()
