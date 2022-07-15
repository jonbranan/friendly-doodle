#The third file shall contain logging and email communication.

def torlog(self):
    
    if self.loglevel == 'DEBUG':
        self.tl.basicConfig(filename=self.logpath, format='%(asctime)s:%(levelname)s:%(message)s', encoding='utf-8', datefmt='%m/%d/%Y %I:%M:%S %p',level=self.tl.DEBUG)
    if self.loglevel == 'INFO':
        self.tl.basicConfig(filename=self.logpath, format='%(asctime)s:%(levelname)s:%(message)s', encoding='utf-8', datefmt='%m/%d/%Y %I:%M:%S %p',level=self.tl.INFO)

def toremail(self):
    pass

def getunixtimestamp(self):
    self.uts = self.t.time()
    self.tl.info(self.uts)