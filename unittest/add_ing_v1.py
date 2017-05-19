"""This is a program to add verb+ing form.

1. For word end with `e` drop `e`
2. For word ends in consonent-vowel-consonent
double the last letter
3. For other words just add `ing` at the end
"""


def isVerbends_with_e(word):
    """ This function will find the give word ends with `e`
    Args:
        word (str): english verb

    Returns:
       True or False (bool): It the verb ends with `e`
       it will return True or else false
    """
    if len(word) > 3:
        if word[-1] == 'e':
            return True
    else:
        return False


def isVerbConsonent(word):
    """ This function will find the given wors is in
    consonent-vowel-consonent format.

    Args:
        word (str): english verb

    Returns:
       True or False (bool): It the verb is of
       consonent-vowel-consonent format then
       it will return True or else false
    """
    vowels = "aeiou"

    if word[0] not in vowels and word[2] not in vowels:
        if word[1] in vowels:
            return True
    else:
        return False


def add_ing(word):
    """This function will add `ing` format to the given word

    Args:
        word (str): Verb

    Returns:
       This function will add `ing` and return the verb
    """

    if isVerbends_with_e(word):
        return word[:-1] + "ing"

    if isVerbConsonent(word):
        return word + word[-1] + "ing"

    return word + "ing"
