import wikipedia

@tool
def get_person_details(person_name: str) -> str:
    """
    This look for information about a particular person in wikipedia
    
    Args:
    	person_name: the name of the person that the want to know about
    """
    try:
        # Set the language to English (default is 'en')
        wikipedia.set_lang("en")
        
        # Search for the person and get information
        return wikipedia.page(person_name).content
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Multiple entries found for '{person_name}': {e.options}"
    except wikipedia.exceptions.PageError:
        return f"No Wikipedia page found for '{person_name}'."
    except Exception as e:
        return f"An error occurred: {str(e)}"


