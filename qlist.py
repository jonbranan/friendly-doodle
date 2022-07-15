#The second file shall contain functions to build out a list of torrents.
def buildtorlist(self):
        self.protected_count = 0
        self.nonprotected_count = 0
        while self.torrentlist:
            torrent = self.torrentlist.pop()
            self.tl.debug(torrent['tracker'])
            if self.tracker_whitelist['iptorrents-empirehost'] in torrent['tracker']:
                self.tl.debug(f'Protected torrent tracker: {torrent["tracker"]}hash: {torrent["hash"]}')
                self.protected_count += 1
                self.qbt_client.torrents_add_tags(self.tracker_protected_tag,torrent['hash'])
                self.tracker_protected_list.append(torrent)
            elif self.tracker_whitelist["iptorrents-stackoverflow"] in torrent['tracker']:
                self.tl.debug(f'Protected torrent tracker: {torrent["tracker"]}hash: {torrent["hash"]}')
                self.protected_count += 1
                self.qbt_client.torrents_add_tags(self.tracker_protected_tag,torrent['hash'])
                self.tracker_protected_list.append(torrent)
            elif self.tracker_whitelist["iptorrents-bgp"] in torrent['tracker']:
                self.tl.debug(f'Protected torrent tracker: {torrent["tracker"]}hash: {torrent["hash"]}')
                self.protected_count += 1
                self.qbt_client.torrents_add_tags(self.tracker_protected_tag,torrent['hash'])
                self.tracker_protected_list.append(torrent)
            else:
                self.tl.debug(f'Non-protected tracker: {torrent["tracker"]}hash: {torrent["hash"]}')
                self.nonprotected_count += 1
                self.qbt_client.torrents_add_tags(self.tracker_non_protected_tag,torrent['hash'])
                self.tracker_nonprotected_list.append(torrent)

def writetor(self, filepath='./torrentinfo.txt'):
    with open(filepath, 'w') as fp:
        fp.write(str(self.torrentlist))

def listfirsttor(self, index=0):
    torrent = self.torrentlist[index]
    for k,v in torrent.items():
         self.tl.debug(f'{k}:  {v}')

def listqbitapiinfo(self):
        self.tl.info(f'qBittorrent: {self.qbt_client.app.version}')
        self.tl.info(f'qBittorrent Web API: {self.qbt_client.app.web_api_version}')

def torrentcount(self):
    self.tl.debug(f'torrents that are protected {self.protected_count}')
    self.tl.debug(f"torrents that aren't protected {self.nonprotected_count}")