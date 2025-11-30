"""
CP1404/CP5632 Practical - Wikipedia API
File: wiki.py
Student: Zhaozhang Huang
wiki URL: https://en.wikipedia.org/wiki/Townsville
"""

import wikipedia
import warnings
from bs4 import GuessedAtParserWarning

# ignore BeautifulSoup warning
warnings.filterwarnings("ignore", category=GuessedAtParserWarning)
def main():
    """Main program to search Wikipedia pages without using while True."""
    print("Wikipedia Search")
    print("Enter a page title or search phrase (blank to quit)")

    search_term = get_user_input()

    while search_term:
        process_search(search_term)
        search_term = get_user_input()

    print("Thank you.")


def get_user_input():
    """Get and return user input."""
    return input("Enter page title: ").strip()


def process_search(search_term):
    """Process a single Wikipedia search."""
    try:
        page = wikipedia.page(search_term, auto_suggest=False)
        display_page_info(page)

    except wikipedia.DisambiguationError as e:
        handle_disambiguation_error(e)

    except wikipedia.PageError:
        handle_page_error(search_term)

    except Exception as e:
        handle_generic_error(e)


def display_page_info(page):
    """Display information about a Wikipedia page."""
    print(page.title)
    print(get_truncated_summary(page.summary))
    print(page.url)
    print()  # Empty line for readability


def handle_disambiguation_error(error):
    """Handle ambiguous search terms."""
    print("We need a more specific title. Try one of the following, or a new search:")
    for option in error.options[:5]:  # Show first 5 options
        print(f"- {option}")
    print("...")


def handle_page_error(search_term):
    """Handle page not found error."""
    print(f'Page id "{search_term}" does not match any pages. Try another id!')


def handle_generic_error(error):
    """Handle other unexpected errors."""
    print(f"An error occurred: {error}")


def get_truncated_summary(summary, max_length=300):
    """Truncate summary to specified length."""
    if len(summary) <= max_length:
        return summary

    # Find the last period within the max_length
    truncated = summary[:max_length]
    last_period = truncated.rfind('.')

    if last_period > 0:
        return truncated[:last_period + 1]
    else:
        return truncated + "..."


if __name__ == '__main__':
    main()