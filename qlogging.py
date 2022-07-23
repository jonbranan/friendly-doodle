def torlog(self):
    """Setting up the log file, if self.use_log is set to true and self.loglevel is DEBUG OR INFO"""
    if self.use_log:
        if self.loglevel == 'DEBUG':
            self.tl.basicConfig(filename=self.logpath, format='%(asctime)s:%(levelname)s:%(message)s', encoding='utf-8', datefmt='%m/%d/%Y %I:%M:%S %p',level=self.tl.DEBUG)
        elif self.loglevel == 'INFO':
            self.tl.basicConfig(filename=self.logpath, format='%(asctime)s:%(levelname)s:%(message)s', encoding='utf-8', datefmt='%m/%d/%Y %I:%M:%S %p',level=self.tl.INFO)

def tornotify(self):
    """Seting up to use pushover, if self.use_pushover is set to true and 
    if valid self.po_key and self.po_token is provided in the config file"""
    if self.use_pushover:
        self.poc = self.po.Client(self.po_key, api_token=self.po_token)

def tornotifytest(self):
    """Used to make sure tornotify is working and messages are getting to the client"""
    self.poc.send_message("Test Message", title="qbit-maid")

def tornotifysummary(self):
    """Main notification method when the app is used in an automated fashion"""
    self.poc.send_message(f"   Total: {self.total_torrents}\n\
    Protected: {self.c[self.tracker_protected_tag]}\n\
    Non-protected: {self.c[self.tracker_non_protected_tag]}\n\
    Marked for deletion: {len(self.torrent_hash_delete_list)}\n\
    Orphaned: {self.up_tor_counter}", title="--- qbit-maid summary ---")

def getunixtimestamp(self):
    """Used for debuging and development related to unixtimestamps, not used in main script but useful"""
    self.uts = self.t.time()
    self.tl.info(self.uts)