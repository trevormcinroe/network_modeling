import instaloader

from instaloader import Profile, Post

L = instaloader.Instaloader()


def login_with_credentials():
    import credentials
    L.login(user=credentials.user, passwd=credentials.passwd)
    return L

def get_profile_from_username(username):

    profile = Profile.from_username(L.context, username=username)
    return profile

def get_public_friends_by_username(username):
    profile = get_profile_from_username(username)
    followers = set(profile.get_followers())
    public_followers = []
    for follower in followers:
        if follower.is_private != True:
            print(follower.username)
            public_followers.append(follower)
    return public_followers


def get_posts_from_profile(profile):
    # profile = get_profile_from_username(username)
    posts = []
    for post in profile.get_posts():
        posts.append(post)
    return posts


p_friends = get_public_friends_by_username(username='sammyandrewsmusic')


#     posts_by_like = []
#     profile = Profile.from_username(L.context, username_input)
#
#     posts_sorted_by_likes = sorted(profile.get_posts(), key=lambda p: p.likes + p.comments)
#     posts_by_like.append(posts_sorted_by_likes)
#     return posts_sorted_by_likes

# posts = get_posts_from_profile(username_input='alliekay4')

# profile = Profile.from_username(L.context, 'alliekay4')
#
# followers = set(profile.get_followers())


# followers_ids = []
# followers_dict = {}
#
# for follower in followers:
#     # print(follower.userid)
#     # followers_ids.append(follower._i
#     follower_dict = follower._asdict()
#     follower_id = follower.userid
#     followers_dict[follower_id] = follower_dict


# username='alliekay4'
username='simi.mathur'

def main():
    L = login_with_credentials()
    profile = get_profile_from_username(username=username)
    friends = get_public_friends_by_username(username=username)
    # friends = get_friends_by_username(username=username)
    posts = get_posts_from_user(profile)

