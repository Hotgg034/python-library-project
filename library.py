def borrow_book(available, title):
    if available:
        return "You borrowed: " + title
    return "Not available"


def return_book(title):
    if not title:
        return "Error: No title provided"
    return "Returned: " + title
