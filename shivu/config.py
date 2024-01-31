class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "1784606556"
    sudo_users = "1784606556"
    GROUP_ID = -1002133191051
    TOKEN = "5970924128:AAExV-nLSyXssUyD_8M4eSBgYppdME4PfMw"
    mongo_url = "mongodb+srv://HaremDBBot:ThisIsPasswordForHaremDB@haremdb.swzjngj.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "csbsupport"
    UPDATE_CHAT = "ciliksmall"
    BOT_USERNAME = "ciliksmall9bot"
    CHARA_CHANNEL_ID = "-1002092786983"
    api_id = 26626068
    api_hash = "bf423698bcbe33cfd58b11c78c42caa2"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
