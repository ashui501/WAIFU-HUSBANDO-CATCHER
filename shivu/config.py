class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6534367642"
    sudo_users = "7370080350" ,"6679467894", "1837623818"
    GROUP_ID = -1002004197830
    TOKEN = "7256020855:AAHpSYc9yepMl4haN1JdG5Mj8UCGSOvDMj0"
    mongo_url = "mongodb+srv://tiwarireeta004:peqxLEd36RAg7ors@cluster0.furypd3.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL =["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "LovelyXSuppprt"
    UPDATE_CHAT = "LovelyXSuppprt"
    BOT_USERNAME = "GUESSEM_ALL_ROBOT"
    CHARA_CHANNEL_ID = "-1002004197830"
    api_id = 24074986
    api_hash = "f4f6272a85d0e50e39a24cb378be118d"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
