import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7024490050:AAHdgZvq_H_i0EL-8vK4yFiC78Nxxh22dpg")

    APP_ID = int(os.environ.get("APP_ID", 28703383))

    API_HASH = os.environ.get("API_HASH", "2fe9241b329da8109e9a0bef30b74c3d")
