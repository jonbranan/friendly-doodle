#The second file shall contain functions to build out a list of torrents.
def buildtorlist(self):
        """builds multiple lists of torrents to be sorted."""
        self.protected_count = 0
        self.nonprotected_count = 0
        while self.torrentlist:
            torrent = self.torrentlist.pop()
            if self.use_log:
                self.tl.debug(f'{torrent["name"]} {torrent["infohash_v1"]}')
            if torrent['tracker'] == '':
                if self.use_log:
                    self.tl.warning(f"Torrent doesn't have a tracker{torrent['name']} [{torrent['tracker']}]hash: {torrent['hash']}")
                break
            if self.tracker_whitelist['iptorrents-empirehost'] in torrent['tracker']:
                if self.use_log:
                    self.tl.debug(f'Protected torrent: {torrent["tracker"]}hash: {torrent["hash"]}')
                self.protected_count += 1
                self.qbt_client.torrents_add_tags(self.tracker_protected_tag,torrent['hash'])
                self.tracker_protected_list.append(torrent)
            elif self.tracker_whitelist["iptorrents-stackoverflow"] in torrent['tracker']:
                if self.use_log:
                    self.tl.debug(f'Protected torrent: {torrent["tracker"]}hash: {torrent["hash"]}')
                self.protected_count += 1
                self.qbt_client.torrents_add_tags(self.tracker_protected_tag,torrent['hash'])
                self.tracker_protected_list.append(torrent)
            elif self.tracker_whitelist["iptorrents-bgp"] in torrent['tracker']:
                if self.use_log:
                    self.tl.debug(f'Protected torrent: {torrent["tracker"]}hash: {torrent["hash"]}')
                self.protected_count += 1
                self.qbt_client.torrents_add_tags(self.tracker_protected_tag,torrent['hash'])
                self.tracker_protected_list.append(torrent)
            else:
                if self.use_log:
                    self.tl.debug(f'Non-protected torrent: {torrent["tracker"]}hash: {torrent["hash"]}')
                self.nonprotected_count += 1
                self.qbt_client.torrents_add_tags(self.tracker_non_protected_tag,torrent['hash'])
                self.tracker_nonprotected_list.append(torrent)

def writetor(self, filepath='./torrentinfo.txt'):
    with open(filepath, 'w') as fp:
        fp.write(str(self.torrentlist))

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
    self.tl.debug(f'torrents that are protected {self.protected_count}')
    self.tl.debug(f"torrents that aren't protected {self.nonprotected_count}")