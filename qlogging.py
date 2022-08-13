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

def processcounts(self):
    self.c = self.ct()
    for item in self.tracker_list:
        self.c[item["tags"]] += 1
        
def printprocessor(self):
    """Print summary of torrents"""
    self.tl.info(f'Total: {self.total_torrents}')
    self.tl.info(f'Premature: {self.preme_tor_counter}')
    self.tl.info(f'Ignored: {self.ignored_counter}')
    self.tl.info(f'Protected: {self.c[self.tracker_protected_tag]}')
    self.tl.info(f'Non-protected: {self.c[self.tracker_non_protected_tag]}')
    self.tl.info(f'Orphaned: {self.up_tor_counter}')
    self.tl.info(f'Marked for deletion: {len(self.torrent_hash_delete_list)}')

def tornotifysummary(self):
    """Main notification method when the app is used in an automated fashion"""
    self.poc.send_message(f"   Total: {self.total_torrents}\n\
    Premature: {self.preme_tor_counter}\n\
    Ignored: {self.ignored_counter}\n\
    Protected: {self.c[self.tracker_protected_tag]}\n\
    Non-protected: {self.c[self.tracker_non_protected_tag]}\n\
    Orphaned: {self.up_tor_counter}\n\
    Marked for deletion: {len(self.torrent_hash_delete_list)}\n\
    {self.extm}", title="--- qbit-maid summary ---")

def getunixtimestamp(self):
    """Used for debuging and development related to unixtimestamps, not used in main script but useful"""
    self.uts = self.t.time()
    self.tl.info(self.uts)

def writetor(self, filepath='./torrentinfo.json'):
    """Write all torrent data to a file.
    Useful for development of new features.
    """
    pass

def listfirsttor(self, index=0):
    """Only lists the first torrent"""
    self.tl.debug('First torrent in the list:')
    torrent = self.torrentlist[index]
    for k,v in torrent.items():
         self.tl.debug(f'{k}:  {v}')
    self.tl.debug('\n')

def listqbitapiinfo(self):
        """Writes torrent info to log file"""
        self.tl.debug(f'qBittorrent: {self.qbt_client.app.version}')
        self.tl.debug(f'qBittorrent Web API: {self.qbt_client.app.web_api_version}')

def torrentcount(self):
    """write torrent counts to log file"""
    self.tl.debug(f'torrents that are protected {self.tracker_list.count("ipt")}')
    self.tl.debug(f'torrents that aren\'t protected {self.tracker_list.count("public")}')

def torlisttags(self):
    pass

def debugpremecal(self):
    for torrent in self.torrentlist:
        if torrent['infohash_v1'] == 'a89b484ea375094af53ce89ecbea14bf086d6284':
            print(torrent["name"][0:20])
            print(torrent['added_on'] + self.minimum_age >= self.t.time())

def getscriptruntime(self):
    elapsed_time = self.et - self.st
    if self.use_log:
        self.tl.info(f'Execution time: [{elapsed_time}]')
    if self.use_pushover:
        self.extm = f"Execution time: [{elapsed_time}]"

def getobjecttype(object):
    print(type(object))