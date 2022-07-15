#The first file shall contain an client to the qbit api and the processing of the torrents.
import qbittorrentapi
from json import load
from qlist import *
from qlogging import *
from qprocess import *
import time
import logging

class Qbt:
    def __init__(self):
        """Main object, should be calling functions from qlist.py, qlogging.py and qprocess.py"""
        # Open the config. Needs a json file with the data in config.json.example
        c = open('./config.json')
        self.config = load(c)
        # Create the api object
        self.qbt_client = qbittorrentapi.Client(
            host=self.config["host"],
            port=self.config["port"],
            username=self.config["username"],
            password=self.config["password"],
        )
        # Create the logging object
        self.tl = logging
        # Variables torlog uses from config.json
        self.logpath=self.config["logpath"]
        self.loglevel=self.config["loglevel"]
        torlog(self)
        self.t = time
        f = open('./tracker-whitelist.json')
        self.tracker_whitelist = load(f)
        self.tracker_protected_list = []
        self.tracker_nonprotected_list = []
        self.tracker_protected_tag = 'ipt'
        self.tracker_non_protected_tag = 'public'
        self.torrent_hash_delete_list = []
        self.tl.debug(self.tracker_whitelist)
        try:
            self.tl.info('Connecting to host.')
            self.qbt_client.auth_log_in()
            self.tl.info('Connected.')
        except qbittorrentapi.LoginFailed as e:
            self.tl.exception(e)
        self.torrentlist = {}
        self.torrentlist = self.qbt_client.torrents_info()
        buildtorlist(self)
        torprocessor(self)
        printprocessor(self)
        tordelete(self)

if  __name__== "__main__":
    Qbt()