#The first file shall contain an client to the qbit api and the processing of the torrents.
import qbittorrentapi
import pushover
from json import load
from json import dump
from qlist import *
from qlogging import *
from qprocess import *
import time
import datetime
import logging
from collections import Counter

class Qbt:
    def __init__(self):
        """Main object, should be calling functions from qlist.py, qlogging.py and qprocess.py"""
        # Open the config. Needs a json file with the data in config.json.example
        self.st = datetime.datetime.now()
        c = open('./config.json')
        self.config = load(c)
        w = open('./category-whitelist.json')
        self.cat_whitelist = load(w)
        # Create the api object
        self.qbt_client = qbittorrentapi.Client(
            host=self.config["host"],
            port=self.config["port"],
            username=self.config["username"],
            password=self.config["password"],
        )
        # Create the logging and pushover objects
        self.tl = logging
        self.po = pushover
        self.ct = Counter
        # Variables torlog uses from config.json
        self.use_pushover = self.config["use_pushover"]
        self.use_log = self.config["use_log"]
        self.po_key = self.config["po_key"]
        self.po_token = self.config["po_token"]
        self.logpath = self.config["logpath"]
        self.loglevel = self.config["loglevel"]
        self.tracker_protected_tag = self.config["protected_tag"]
        self.tracker_non_protected_tag = self.config["non_protected_tag"]
        self.minimum_age = self.config["minimum_age"]
        self.age = self.config["age"]
        # Calling log and notify functions
        torlog(self)
        tornotify(self)
        self.t = time
        # Pulling domain names to treat carefully
        f = open('./tracker-whitelist.json')
        self.tracker_whitelist = load(f)
        self.tracker_list = []
        self.up_tor_counter = 0
        self.preme_tor_counter = 0
        self.ignored_counter = 0
        self.torrent_hash_delete_list = []
        if self.use_log:
            self.tl.debug(self.tracker_whitelist)
        #logging in
        try:
            self.tl.info('Connecting to host.')
            self.qbt_client.auth_log_in()
            self.tl.info('Connected.')
        except qbittorrentapi.APIError as e:
            self.tl.exception(e)
            self.poc.send_message(e, title="qbit-maid API ERROR")
        self.torrentlist = {}
        # Pulling all torrent data
        self.torrentlist = self.qbt_client.torrents_info()
        self.d = dump
        self.l = load
        writetor(self)
        #Main process block
        #debugpremecal(self)
        if self.use_log:
            listqbitapiinfo(self)
            listfirsttor(self)
        buildtorlist(self)
        processcounts(self)
        #tordeletetags(self)
        if self.use_log:
            torrentcount(self)
        torprocessor(self)
        if self.use_log:
            printprocessor(self)
        if self.config["delete_torrents"]:
            tordelete(self)
        self.et = datetime.datetime.now()
        getscriptruntime(self)
        if self.use_pushover:
            tornotifysummary(self)
# Run
if  __name__== "__main__":
    Qbt()