import wiki

# Ask the user for a search term
search_term = input("Enter a phrase to search on Wikipedia: ")

# Fetch a summary from Wikipedia
try:
    summary = wiki.summary(search_term, sentences=3)
    print(f"\nSummary for '{search_term}':\n{summary}")
except wiki.exceptions.DisambiguationError as e:
    print(f"\nThe term '{search_term}' is ambiguous. Here are some suggestions:\n{e.options}")
except wiki.exceptions.PageError:
    print(f"\nThe page for '{search_term}' does not exist. Please try another search term.")