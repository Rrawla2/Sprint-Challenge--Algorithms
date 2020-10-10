'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurrences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    
    # This is the base case, if the word is less than 2 letters it cannot match 'th', return 0
    if len(word) < 2:
        return 0
    # if the word is equal to 2 letters, check if they match lower case 'th'
    # if they match, return 1, if they don't match, return 0
    if len(word) == 2:
        if word == 'th':
            return 1
        else:
            return 0
    # check for 'th' recursively until the end of the word is reached.
    if word[:2] == 'th':
        return count_th(word[2:]) + 1
    else:
        return count_th(word[1:])

