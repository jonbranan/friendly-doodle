#The third file shall contain logging and email communication.

def torlog(self):
    if self.use_log:
        if self.loglevel == 'DEBUG':
            self.tl.basicConfig(filename=self.logpath, format='%(asctime)s:%(levelname)s:%(message)s', encoding='utf-8', datefmt='%m/%d/%Y %I:%M:%S %p',level=self.tl.DEBUG)
        elif self.loglevel == 'INFO':
            self.tl.basicConfig(filename=self.logpath, format='%(asctime)s:%(levelname)s:%(message)s', encoding='utf-8', datefmt='%m/%d/%Y %I:%M:%S %p',level=self.tl.INFO)

def tornotify(self):
    if self.use_pushover:
        self.poc = self.po.Client(self.po_key, api_token=self.po_token)

def tornotifytest(self):
    self.poc.send_message("Test Message", title="qbit-maid")

def tornotifysummary(self):
    self.poc.send_message(f'    Protected torrents: {len(self.tracker_protected_list)}\n\
    Non-protected torrents: {len(self.tracker_nonprotected_list)}\n\
    Total torrents set for deletion: {len(self.torrent_hash_delete_list)}', title="qbit-maid summary")


def getunixtimestamp(self):
    self.uts = self.t.time()
    self.tl.info(self.uts)