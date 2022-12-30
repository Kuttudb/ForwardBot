from os import environ
class Config(object):
    API_ID = environ.get("API_ID", 8281168)
    API_HASH = environ.get("API_HASH", "445ff67ec34858448ac184c7479ce917")
    BOT_TOKEN = environ.get("BOT_TOKEN", "2055718473:AAHGch-ioqCoYkzTkMtw0SDG1UkYK91IQWc")
    STRING_SESSION = environ.get("STRING", "BQAXk0V3LeDyJQx9U-Gni8Lac8BnBZzEexfab1DZUqvNj-XjLr0KdE8ZEzWosE6yEdMflLYn_HeFJuucAzE36nmosTyXI9t5x6wRjWV_TPE3s1DMeolthO9esidP0Mi49KzoZCZENnswy5v6kLvZpZV1sWFJSpmyy4B9i-AUW8zWC2dwK1wVYCWxPMcyXXfaRRnYmPn6H2Sh2HasG2SgmUQlmWJhRUyRnqlnU_KSAfw-_Ky9KLOtpESKDcI9rROW5qqR5FBlb5IcsfpiW3PBFlNdyFbCkJ7vn0D23C6y1uf3f6mkF3Sy3nNyXdf8g74q_GmxLk3-gp9GzVA_wDJB1fqDAAAAADxIpiEA")
    SUDO_USERS = environ.get("SUDO_USERS", None)
    COMMAND_HAND_LER = environ.get("COMMAND_HAND_LER", "^/")
    HELP_MSG = """
    The Commands in the bot are:
    
    **Command :** /forward
    **Usage : ** Forwards messages from a channel to other.
    **Command :** /count
    **Usage : ** Returns the Total message sent using the bot.
    **Command :** /reset
    **Usage : ** Resets the message count to 0.
    **Command :** /restart
    **Usage : ** Updates and Restarts the Bot.
    **Command :** /join
    **Usage : ** Joins the channel.
    **Command :** /help
    **Usage : ** Get the help of this bot.
    **Command :** /status
    **Usage :** Check current status of Bot.
    **Command :** /uptime
    **Usage :** Check uptime of Bot.
    
    Bot is created by @lal_bakthan and @subinps
    """
