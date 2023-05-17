import qbittorrentapi
import pushover
from tomllib import load
from qlist import *
from qlogging import *
from qprocess import *
from AppriseClient import apprise_notify
import time
import datetime
import logging
from collections import Counter
import csv
import requests as r

class Qbt:
    def __init__(self):
        """Main object, should be calling functions from qlist.py, qlogging.py and qprocess.py"""
        # Open the config. Needs a json file with the data in config.json.example
        self.st = datetime.datetime.now()
        c = open('./config.toml', 'rb')
        self.config = load(c)

        # # Create the api object
        self.qbt_client = qbittorrentapi.Client(
            # qbittorrent
            host=self.config["qbittorrent"]["host"],
            port=self.config["qbittorrent"]["port"],
            username=self.config["qbittorrent"]["username"],
            password=self.config["qbittorrent"]["password"],
        )
        # Create the logging and pushover objects
        self.tl = logging
        self.po = pushover
        self.ct = Counter
        self.cv = csv
        # Init config.toml

        # logging
        self.use_log = self.config["logging"]["use_log"]
        self.log_path = self.config["logging"]["log_path"]
        self.log_level = self.config["logging"]["log_level"]

        #app_tags
        self.tracker_protected_tag = self.config["app_tags"]["protected_tag"]
        self.tracker_non_protected_tag = self.config["app_tags"]["non_protected_tag"]

        #torrent
        self.delete_torrents = self.config["torrent"]["delete_torrents"]
        self.minimum_age = self.config["torrent"]["minimum_age"]
        self.age = self.config["torrent"]["age"]

        #pushover
        self.use_pushover = self.config["pushover"]["use_pushover"]
        self.po_key = self.config["pushover"]["po_key"]
        self.po_token = self.config["pushover"]["po_token"]

        #apprise
        self.use_apprise = self.config["apprise"]["use_apprise"]
        self.apprise_host = self.config["apprise"]["host"]
        self.apprise_port = self.config["apprise"]["port"]
        self.apprise_aurls = self.config["apprise"]["aurls"]

        #dragnet
        self.enable_dragnet = self.config["dragnet"]["enable_dragnet"]
        self.dragnet_outfile = self.config["dragnet"]["dragnet_outfile"]

        #ignored_categories
        self.cat_whitelist = self.config["ignored_categories"]

        #ignored_domains
        self.tracker_whitelist = self.config["ignored_domains"]

        #ignored_tags
        self.ignored_tags = self.config["ignored_domains"]

        # Calling log and notify functions
        tor_log(self)
        tor_notify(self)
        self.t = time
        # Pulling domain names to treat carefully
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
        if self.use_log:
            torrent_count(self)
        tor_processor(self)
        if self.use_log:
            print_processor(self)
        if self.delete_torrents:
            tor_delete(self)
        self.et = datetime.datetime.now()
        get_script_runtime(self)
        if self.use_pushover:
            tor_notify_summary(self)
        if self.use_apprise:
            tor_notify_apprise(self, r, apprise_notify)
# Run
if  __name__== "__main__":
    Qbt()