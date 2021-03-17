from InternetSpeedBot import InternetSpeedTwitterBot

PROMISED_DOWN = 300
PROMISED_UP = 100

bot = InternetSpeedTwitterBot()

test_speed = bot.get_internet_speed()
bot.post_on_twitter(test_speed, PROMISED_DOWN, PROMISED_UP)