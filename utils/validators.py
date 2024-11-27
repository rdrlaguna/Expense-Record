# utils/validators.py

def validate_category_name(name):
    """ Validates a category name. """

    # Treat string case insensitive
    # Validate string is not empty
    if not name.strip():
        raise ValueError(f"Category cannot be empty.")
    
    # Validate string has only letters
    if not name.isalpha():
        raise ValueError(f"The name must have only letters.")
    
    # Validate name lenght
    if len(name) < 4 or len(name) > 16:
        raise ValueError(f"Name must have between 4 to 16 characters.")
    
    return True
