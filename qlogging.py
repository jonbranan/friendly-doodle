#The third file shall contain logging and email communication.

def torlog(self):
    if self.loglevel == 'DEBUG':
        self.tl.basicConfig(filename=self.logpath, format='%(asctime)s:%(levelname)s:%(message)s', encoding='utf-8', datefmt='%m/%d/%Y %I:%M:%S %p',level=self.tl.DEBUG)
    if self.loglevel == 'INFO':
        self.tl.basicConfig(filename=self.logpath, format='%(asctime)s:%(levelname)s:%(message)s', encoding='utf-8', datefmt='%m/%d/%Y %I:%M:%S %p',level=self.tl.INFO)

def tornotify(self):
    if self.use_pushover:
        self.poc = self.po.Client(self.po_key, api_token=self.po_token)
        self.poc.send_message("Test Message", title="qbit-maid")

def getunixtimestamp(self):
    self.uts = self.t.time()
    self.tl.info(self.uts)