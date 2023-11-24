"""
Estimate: 30 min
Actual Time: 35 min
"""
import wikipedia


def main():
    """Get input from user to return a Wikipedia page and its summary."""
    user_input = input('Search Wikipedia: ')
    while user_input != '':
        try:
            wikipedia_page = wikipedia.page(user_input)
        except wikipedia.exceptions.DisambiguationError as e:
            print(e.options)
            wikipedia_page = None

        if wikipedia_page:
            print(wikipedia_page.title)
            print(wikipedia_page.summary)
        user_input = input('Search Wikipedia: ')


main()
