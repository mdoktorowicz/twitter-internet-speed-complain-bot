# twitter-internet-speed-complain-bot
A Twitter bot which tweets only if the tested internet speed is lower than speed in contract with Internet Provider.

The bot first test the internet speed on speedtest.net.
Then, if either the download or the upload speed is lower than the threshold speed (e.g. speed the Provider pledged to deliver in the user agreement), the bot logs in to Twitter and sends a tweet with the internet speed.

A tag to refer to the Internet Provider Twitter could be added to ensure real functionality. I'm not doing this because it's a project I did to learn (and I'm happy with my internet speed 😉)

It takes the bot around 1 min 30 secs to run on my PC (most of which is doing the internet speed test).

Twitter login & password are set as environment variables.
