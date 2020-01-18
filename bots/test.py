import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler(
    "ZWDrd0Aa80p1oEd6dUAs96sNk",
    "kqZDbG8fnSGX1G1khgzl1tsiW8RlH9NtafHrJ5vd8vL6w2hLl4")
auth.set_access_token(
    "1211469743493746688-2ppf6rBRwLSGe8UQBpzLxc8ReIPnUE",
    "UlitYRU0VY04ecAhVopcksUyQNOYDgt9DqErBEMphzO8t")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")
