def isVerbends_with_e(word):
    if len(word) > 3:

        if word[-1] == 'e':

            return True

    else:

        return False


def isVerbConsonent(word):

    vowels = "aeiou"

    if len(word) != 3:
        return False

    if word[0] not in vowels and word[2] not in vowels:
        if word[1] in vowels:

            return True
    else:

        return False


def add_ing(word):

    if isVerbends_with_e(word):

        return word[:-1] + "ing"

    if isVerbConsonent(word):

        return word + word[-1] + "ing"

    return word + "ing"





# words = ["shave", "comb", "make", "feed", "hope", "save", "tap"]



# for word in words:

#     print add_ing(word)
