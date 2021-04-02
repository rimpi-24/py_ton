#This script helps to scape instagram data of user having open profile

import instaloader
bot = instaloader.Instaloader()

# Load a profile from an Instagram
profile = instaloader.Profile.from_username(bot.context, 'shaazjung')
posts = profile.get_posts()

#Print details
print("Username: ", profile.username)
print("User ID: ", profile.userid)
print("Number of Posts: ", profile.mediacount)
print("Followers: ", profile.followers)
print("Followees: ", profile.followees)
print("Bio: ", profile.biography,profile.external_url)


# Iterate and download post data
for index, post in enumerate(posts, 1):
     bot.download_post(post, target=f"{profile.username}_{index}")
     #break to get only latest one
