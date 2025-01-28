import wikipedia

search_term = input("Enter a phrase to search on Wikipedia: ")

try:
    summary = wikipedia.summary(search_term, sentences=3)
    print(f"\nSummary for '{search_term}':\n{summary}")
except wikipedia.exceptions.DisambiguationError as e:
    print(f"\nThe term '{search_term}' is ambiguous. Here are some suggestions:\n{e.options}")
except wikipedia.exceptions.PageError:
    print(f"\nThe page for '{search_term}' does not exist. Please try another search term.")