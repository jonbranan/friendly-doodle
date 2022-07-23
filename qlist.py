def buildtorlist(self):
        """Builds multiple lists of torrents to be sorted. Also adds tags to the torents.
        There are more effecient ways of doing things but I did this rather quickly.
        V2 will certainly be more performant. The reason two lists were used was so that torrents 
        that are in public trackers woudln't be around as long as torrents from a private tracker.
        """
        while self.torrentlist:
            torrent = self.torrentlist.pop()
            if self.use_log:
                self.tl.debug(f'["{torrent["name"][0:20]}..."] {torrent["infohash_v1"]}')
            if torrent['category'] in self.cat_whitelist.values():
                self.tl.info(f'Ignored torrent:["{torrent["name"][0:20]}..."]')
                continue
            if torrent['tracker'] == '':
                if self.use_log:
                    self.tl.warning(f'Torrent doesn\'t have a tracker ["{torrent["name"][0:20]}..."] [{torrent["tracker"]}]hash: {torrent["hash"]}')
                continue
            if torrent['tracker'].split('/')[2] in self.tracker_whitelist.values():
                if self.use_log:
                    self.tl.debug(f'Protected torrent: {torrent["tracker"]}hash: {torrent["hash"]}')
                self.qbt_client.torrents_add_tags(self.tracker_protected_tag,torrent['hash'])
                self.tracker_protected_list.append(torrent)
            if torrent['tracker'].split('/')[2] not in self.tracker_whitelist.values():
                if self.use_log:
                    self.tl.debug(f'Non-protected torrent: {torrent["tracker"]}hash: {torrent["hash"]}')
                self.qbt_client.torrents_add_tags(self.tracker_non_protected_tag,torrent['hash'])
                self.tracker_nonprotected_list.append(torrent)

def writetor(self, filepath='./torrentinfo.txt'):
    """Write all torrent data to a file.
    Useful for development of new features.
    """
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
    """write torrent counts to log file"""
    self.tl.debug(f'torrents that are protected {self.protected_count}')
    self.tl.debug(f"torrents that aren't protected {self.nonprotected_count}")

def tordeletetags(self):
    tag_list = ['ipt','public','iptorrents']
    self.qbt_client.torrents_delete_tags(tag_list)

def torlisttags(self):
    pass