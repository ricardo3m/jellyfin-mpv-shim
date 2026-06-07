import os.path
import os
import getpass

from .args import get_args

username = getpass.getuser()


def win32(app: str):
    if os.environ.get("APPDATA"):
        return os.path.join(os.environ["APPDATA"], app)
    else:
        return os.path.join(r"C:\Users", username, r"AppData\Roaming", app)

def confdir(app: str):
    custom_config = get_args().config
    if custom_config is not None:
        return custom_config
    return win32(app)


def get(app: str, conf_file: str, create: bool = False):
    conf_folder = confdir(app)
    if not os.path.isdir(conf_folder):
        os.makedirs(conf_folder)
    conf_file = os.path.join(conf_folder, conf_file)
    if create and not os.path.isfile(conf_file):
        open(conf_file, "w").close()
    return conf_file


def get_dir(app: str, subfolder: str):
    conf_folder = os.path.join(confdir(app), subfolder)
    if not os.path.isdir(conf_folder):
        os.makedirs(conf_folder)
    return conf_folder
