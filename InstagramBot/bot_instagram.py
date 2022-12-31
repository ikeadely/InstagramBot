from instabot import Bot

my_bot = Bot()

my_bot.login(username="", password="")

my_bot.follow("")

my_bot.follow_users(["","",""])

my_bot.unfollow_non_followers()



followers_list = my_bot.get_user_followers("")

following_list = my_bot.get_user_following("")

for each_follower in followers_list:
    print(my_bot.get_username_from_user_id(each_follower))

for each_follower in followers_list:
    print(my_bot.get_username_from_user_id(each_follower))

for each_follower in followers_list:
    print(my_bot.get_username_from_user_id(each_follower))

for count, each_follower in enumerate(followers_list)
