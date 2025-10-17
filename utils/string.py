import re


def validate_email(value: str):
    """
    Validate a given email address to ensure it is within the correct length and format

    Validates the following:
    - length is between 5 and 60 characters
    - contains exactly one '@'
    - does not start with '@'
    - does not contain '..'
    - does not contain spaces or commas
    - does not contain any of the following prohibited patterns:
        - &quot;
        - &lt;
        - &gt;
        - &<;
        - &>;;
        - &;#
        - http:
        - https:
        - javascript
        - www.
        - WWW.
        - &lt;script&gt;
        - &lt;/script&gt;
        - &lt;script
        - &lt;/scrip

    Raises a ValueError if the email does not pass any of the above checks
    """
    if not (5 <= len(value) <= 60):
        raise ValueError("Invalid length")

    if value.count("@") != 1 or value.startswith("@") or ".." in value:
        raise ValueError("Invalid format")

    if " " in value or "," in value:
        raise ValueError("Spaces and commas are not allowed")

    prohibited_patterns = [
        "&quot;",
        "&lt;",
        "&gt;",
        "&<;",
        "&>;",
        '&";',
        "&;#",
        "http:",
        "https:",
        "javascript",
        "www.",
        "WWW.",
        "&lt;script&gt;",
        "&lt;/script&gt;",
        "&lt;script",
        "&lt;/scrip",
    ]

    pattern = re.compile("|".join(map(re.escape, prohibited_patterns)), re.IGNORECASE)

    if re.search(pattern, value):
        raise ValueError("Email contains prohibited patterns")

    return value
