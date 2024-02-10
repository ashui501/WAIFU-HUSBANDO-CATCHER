class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6649432492"
    sudo_users = "6649432492", "5843270062"
    GROUP_ID = -1002015833205
    TOKEN = "6713160483:AAFewv6EyBO0DXWhm8gbrL9sAJar54tDlmM"
    mongo_url = "mongodb+srv://memek:memek@cluster0.xktxnyr.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://telegra.ph/file/43345aa900233f7649309.jpg", "https://telegra.ph/file/ee98b297887d361544b3c.jpg"]
    SUPPORT_CHAT = "gcanimecommunity"
    UPDATE_CHAT = "Origanimeinfo"
    BOT_USERNAME = "Guess_harem_bot"
    CHARA_CHANNEL_ID = "-1002124487227"
    api_id = 17204044
    api_hash = "db2dd5d8401971aa433ef3c0f9a108da"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
