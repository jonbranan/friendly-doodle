import qbittorrentapi
import pushover
from json import load
from qlist import *
from qlogging import *
from qprocess import *
import time
import datetime
import logging
from collections import Counter
import csv

class Qbt:
    def __init__(self):
        """Main object, should be calling functions from qlist.py, qlogging.py and qprocess.py"""
        # Open the config. Needs a json file with the data in config.json.example
        self.st = datetime.datetime.now()
        c = open('./config.json')
        self.config = load(c)
        w = open('./ignored_categories.json')
        self.cat_whitelist = load(w)
        tg = open('./ignored_tags.json')
        self.ignored_tags = load(tg)
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
        self.cv = csv
        # Init config.json
        self.use_pushover = self.config["use_pushover"]
        self.use_log = self.config["use_log"]
        self.po_key = self.config["po_key"]
        self.po_token = self.config["po_token"]
        self.log_path = self.config["log_path"]
        self.log_level = self.config["log_level"]
        self.tracker_protected_tag = self.config["protected_tag"]
        self.tracker_non_protected_tag = self.config["non_protected_tag"]
        self.minimum_age = self.config["minimum_age"]
        self.age = self.config["age"]
        self.enable_dragnet = self.config["enable_dragnet"]
        self.dragnet_outfile = self.config["dragnet_outfile"]
        # Calling log and notify functions
        tor_log(self)
        tor_notify(self)
        self.t = time
        # Pulling domain names to treat carefully
        f = open('./ignored_domains.json')
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
            self.po.send_message(e, title="qbit-maid API ERROR")
        # Pulling all torrent data
        self.torrent_list = self.qbt_client.torrents_info()
        #Main process block
        if self.use_log:
            list_qbit_api_info(self)
            list_first_tor(self)
        build_tor_list(self)
        process_counts(self)
        # if self.use_log:
        #     torrent_count(self)
        tor_processor(self)
        if self.use_log:
            print_processor(self)
        if self.config["delete_torrents"]:
            tor_delete(self)
        self.et = datetime.datetime.now()
        get_script_runtime(self)
        if self.use_pushover:
            tor_notify_summary(self)
# Run
if  __name__== "__main__":
    Qbt()