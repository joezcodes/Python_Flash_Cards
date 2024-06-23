import random

word1 = {
    'word':'Like',
    'meaning':'Click the Like Button'
}

word2 = {
    'word':'Subscribe',
    'meaning':'Click the subscribe button'
}

word3 = {
    'word':'Bell Notification',
    'meaning':'Click the Bell'
}

word4 = {
    'word':'Comment',
    'meaning':'Leave a comment Down below'
}

word5 = {
    'word':'Ko-fi',
    'meaning':'Check out Joezcodes Ko-fi page'
}

word6 = {
    'word':'CTRL + S',
    'meaning':'Save your progress often'
}

#collects the words together 
group = [word1, word2, word3, word4, word5, word6]

#chooses one word for both instances of print coming up
chosen = random.choice(group)

print('what is the meaning of:', chosen['word'])

print(input('Press Enter...'))

print(chosen['meaning'])