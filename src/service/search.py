from src.service.challenges import searchChallenge
from src.service.examples import searchExample
from src.service.posts import searchPost

def searchContent(text):
    try:
        challenges = searchChallenge(text)
        examples = searchExample(text)
        posts = searchPost(text)

        results = {
            "posts": posts,
            "ejemplos": examples,
            "retos": challenges
        }

        if not results:
            return None
        return results
    except Exception as e:
        print("Error: ", e)
        return None