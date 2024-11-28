from .users import createFirstUser
from .topics import insertTopics
from .posts import insertPosts
from .examples import insertExamples
from .challenges import insertChallenges

def insertInitalData():
    createFirstUser()
    insertTopics()
    insertPosts()
    insertExamples()
    insertChallenges()