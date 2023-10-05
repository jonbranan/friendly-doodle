def tor_log(self):
    """Setting up the log file, if self.use_log is set to true and self.loglevel is DEBUG OR INFO"""
    if self.use_log:
        if self.log_level.lower() == 'debug':
            self.tl.basicConfig(filename=self.log_path, format='%(asctime)s:%(levelname)s:%(message)s', encoding='utf-8', datefmt='%m/%d/%Y %I:%M:%S %p',level=self.tl.DEBUG)
        elif self.log_level.lower() == 'info':
            self.tl.basicConfig(filename=self.log_path, format='%(asctime)s:%(levelname)s:%(message)s', encoding='utf-8', datefmt='%m/%d/%Y %I:%M:%S %p',level=self.tl.INFO)
        elif self.log_level.lower() == 'warn':
            self.tl.basicConfig(filename=self.log_path, format='%(asctime)s:%(levelname)s:%(message)s', encoding='utf-8', datefmt='%m/%d/%Y %I:%M:%S %p',level=self.tl.WARN)
        elif self.log_level.lower() == 'error':
            self.tl.basicConfig(filename=self.log_path, format='%(asctime)s:%(levelname)s:%(message)s', encoding='utf-8', datefmt='%m/%d/%Y %I:%M:%S %p',level=self.tl.ERROR)

def tor_notify(self):
    """Seting up to use pushover, if self.use_pushover is set to true and 
    if valid self.po_key and self.po_token is provided in the config file"""
    if self.use_pushover:
        self.poc = self.po.Pushover(self.po_token)

def tor_notify_apprise(self, req_obj, app_obj):
    """Use apprise"""
    body = f"   Total: {self.total_torrents}\n\
    Premature: {self.preme_tor_counter}\n\
    Ignored: {self.ignored_counter}\n\
    Protected: {self.c[self.tracker_protected_tag]}\n\
    Non-protected: {self.c[self.tracker_non_protected_tag]}\n\
    Orphaned: {self.up_tor_counter}\n\
    Marked for deletion: {len(self.torrent_hash_delete_list)}\n\
    {self.extm}"
    title = "--- qbit-maid summary ---"
    app_obj(req_obj, self.apprise_host, self.apprise_port, self.apprise_aurls, title, body)

def tornotifytest(self):
    """Used to make sure tornotify is working and messages are getting to the client"""
    self.poc.message(self.po_key, "Test Message", title="qbit-maid")

def process_counts(self):
    self.c = self.ct()
    for item in self.tracker_list:
        self.c[item["tags"]] += 1
        
def print_processor(self):
    """Print summary of torrents"""
    self.tl.info(f'Total: {self.total_torrents}')
    self.tl.info(f'Premature: {self.preme_tor_counter}')
    self.tl.info(f'Ignored: {self.ignored_counter}')
    self.tl.info(f'Protected: {self.c[self.tracker_protected_tag]}')
    self.tl.info(f'Non-protected: {self.c[self.tracker_non_protected_tag]}')
    self.tl.info(f'Orphaned: {self.up_tor_counter}')
    self.tl.info(f'Marked for deletion: {len(self.torrent_hash_delete_list)}')

def tor_notify_summary(self):
    """Main notification method when the app is used in an automated fashion"""
    self.poc.message(self.po_key, f"   Total: {self.total_torrents}\n\
    Premature: {self.preme_tor_counter}\n\
    Ignored: {self.ignored_counter}\n\
    Protected: {self.c[self.tracker_protected_tag]}\n\
    Non-protected: {self.c[self.tracker_non_protected_tag]}\n\
    Orphaned: {self.up_tor_counter}\n\
    Marked for deletion: {len(self.torrent_hash_delete_list)}\n\
    {self.extm}", title="--- qbit-maid summary ---")

def list_first_tor(self, index=0):
    """Only lists the first torrent"""
    self.tl.debug('First torrent in the list:')
    torrent = self.torrent_list[index]
    for k,v in torrent.items():
         self.tl.debug(f'{k}:  {v}')
    self.tl.debug('\n')

def list_qbit_api_info(self):
        """Writes torrent info to log file"""
        self.tl.debug(f'qBittorrent: {self.qbt_client.app.version}')
        self.tl.debug(f'qBittorrent Web API: {self.qbt_client.app.web_api_version}')

def torrent_count(self):
    """write torrent counts to log file"""
    self.tl.debug(f'*** Torrents with tag["{self.tracker_protected_tag}"] {self.c[self.tracker_protected_tag]} ***')
    self.tl.debug(f'*** Torrents with tag["{self.tracker_non_protected_tag}"] {self.c[self.tracker_non_protected_tag]} ***')

def get_script_runtime(self):
    elapsed_time = self.et - self.st
    if self.use_log:
        self.tl.info(f'Execution time: [{elapsed_time}]')
    if self.use_pushover:
        self.extm = f"Execution time: [{elapsed_time}]"
    if self.use_apprise:
        self.extm = f"Execution time: [{elapsed_time}]"

def send_ping(self, req_obj, healthcheck_url):
    try:
        req_obj.get(healthcheck_url, timeout=10)
    except req_obj.RequestException as e:
        self.tl.info(f"Ping failed: {e}")

def debug_torrent_list(self):
    self.tl.debug(self.torrent_list)