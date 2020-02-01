import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("7OxsgBl37Tz5PsJ89kTNPlRf1", "QLqbRMAnRPVGj3IYuPg92FMzzgr9XHCAzHqsZgrThO1VncwZXD")
auth.set_access_token("1223421197762924544-UQRR4A81yrl1X3X9obGc2r6DiKdlIb", "2JsovQn41J3Cbj1rntG6ReDGB7bxTBzOUqiQDktLlOYPQ")

# Create API object
api = tweepy.API(auth)

# Create a tweet
#api.