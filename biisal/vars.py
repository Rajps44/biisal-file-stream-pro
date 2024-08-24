import os
from dotenv import load_dotenv
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)

# Load environment variables from a .env file
load_dotenv()

class Var(object):
    # Bot configuration
    bot_name = "Netflixmovielakh_bot"
    bisal_channel = "https://t.me/netfilixmo_ch"
    bisal_grp = "https://t.me/n_flixmovie"
    
    MULTI_CLIENT = False
    API_ID = int(os.getenv('API_ID', '27002519'))
    API_HASH = str(os.getenv('API_HASH', '1033ee721101d78366b4ac46aadf3930'))
    BOT_TOKEN = str(os.getenv('BOT_TOKEN', '7478730845:AAGTeTsmm7ToeQc7lW3jimEPiAlddFySsNo'))
    name = str(os.getenv('name', 'Netflixmovielakh_bot'))
    SLEEP_THRESHOLD = int(os.getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(os.getenv('WORKERS', '4'))
    BIN_CHANNEL = int(os.getenv('BIN_CHANNEL', '-1001924382977'))
    NEW_USER_LOG = int(os.getenv('NEW_USER_LOG', '-1001924382977'))
    PORT = int(os.getenv('PORT', '8080'))
    BIND_ADDRESS = str(os.getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(os.getenv('PING_INTERVAL', '1200'))  # 20 minutes
    OWNER_ID = [int(x) for x in os.getenv("OWNER_ID", "6508598835").split()]
    NO_PORT = bool(os.getenv('NO_PORT', 'False') == 'True')
    APP_NAME = None
    OWNER_USERNAME = str(os.getenv('OWNER_USERNAME', 'Rajps33'))
    APP_NAME = str(os.getenv('APP_NAME', ''))  # The app name on Heroku, if any
    API = os.getenv("API", "fa2a0768fc8d2a51b22e46293634a52670a73c7a")  # Shortlink API
    URL = os.getenv("URL", "shortxlinks.com")  # Shortlink domain without https://
    VERIFY_TUTORIAL = os.getenv("VERIFY_TUTORIAL", "")  # How to open the verification link
    VERIFY = os.getenv("VERIFY", "True")  # Verification setting

    if 'DYNO' in os.environ:
        ON_HEROKU = True
    else:
        ON_HEROKU = False

    # Determine FQDN (Fully Qualified Domain Name) based on whether it's running on Heroku or not
    FQDN = str(os.getenv('FQDN', 'BIND_ADDRESS:PORT')) if not ON_HEROKU or os.getenv('FQDN', '') else APP_NAME + '.herokuapp.com'
    HAS_SSL = bool(os.getenv('HAS_SSL', 'True') == 'True')  # Check if SSL is enabled

    # Set the URL with or without SSL
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)

    # MongoDB database URL
    DATABASE_URL = str(os.getenv('DATABASE_URL', 'mongodb+srv://t54s2lqiv6:2mOV4n1iL21cMcMH@cluster0.ma3sm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'))
    UPDATES_CHANNEL = str(os.getenv('UPDATES_CHANNEL', 'netfilixmo_ch'))
    BANNED_CHANNELS = list(set(int(x) for x in str(os.getenv("BANNED_CHANNELS", "-1002244711970")).split()))
    BAN_CHNL = list(set(int(x) for x in str(os.getenv("BAN_CHNL", "")).split()))
    BAN_ALERT = str(os.getenv('BAN_ALERT', '<b>ʏᴏᴜʀ ᴀʀᴇ ʙᴀɴɴᴇᴅ ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ.Pʟᴇᴀsᴇ ᴄᴏɴᴛᴀᴄᴛ @biisal_bot ᴛᴏ ʀᴇsᴏʟᴠᴇ ᴛʜᴇ ɪssᴜᴇ!!</b>'))

# Log the value of VERIFY to ensure it is loaded correctly
logging.info(f"VERIFY value: {Var.VERIFY}")
