def torprocessor(self):
    """Main logic to sort through both self.tracker_nonprotected_list and self.tracker_protected_list
    If torrent meets criteria for deletion, its infohash_v1 will be appended to self.torrent_hash_delete_list
    """
    for canidate in self.tracker_nonprotected_list:
        if 'ipt' in canidate['tags']:
            if self.use_log:
                self.tl.warning(f'["{canidate["name"][0:20]}..."] was in non-protected list.')
            break
        if canidate['state'] == 'downloading':
            if self.use_log:
                self.tl.info(f'["{canidate["name"][0:20]}..."] is still downloading and will be skipped.')
            break
        else:
            self.torrent_hash_delete_list.append(canidate['infohash_v1'])
            if self.use_log:   
                self.tl.info(f'Submitted ["{canidate["name"][0:20]}..."] for deletion.') 
    for canidate in self.tracker_protected_list:
        if canidate['state'] == 'downloading':
            if self.use_log:
                self.tl.warning(f'["{canidate["name"][0:20]}..."] is still downloading and will be skipped.')
            break
        if canidate['ratio'] < float(1.05):
            if self.use_log:
                self.tl.debug(f'["{canidate["name"][0:20]}..."] is below a 1.05 ratio({canidate["ratio"]})')
            if canidate['added_on'] + self.config["age"] <= self.t.time():
                if self.use_log:
                    self.tl.debug(f'["{canidate["name"][0:20]}..."] Seconds old: {self.t.time() - self.config["age"] - canidate["added_on"]}')
                self.torrent_hash_delete_list.append(canidate['infohash_v1'])
                if self.use_log:
                    self.tl.info(f'Submitted ["{canidate["name"][0:20]}..."] for deletion from the protected list.') 
        if canidate['ratio'] >= float(1.05):
            if self.use_log:
                self.tl.debug(f'["{canidate["name"][0:20]}..."] is above a 1.05 ratio({canidate["ratio"]}).')  
            self.torrent_hash_delete_list.append(canidate['infohash_v1'])
            if self.use_log:
                self.tl.info(f'Submitted ["{canidate["name"][0:20]}..."] for deletion from the protected list.')
        else:
            pass

def printprocessor(self):
    """Print summary of torrents"""
    self.tl.info(f'Protected torrents: {len(self.tracker_protected_list)}')
    self.tl.info(f'Non-protected torrents: {len(self.tracker_nonprotected_list)}')
    self.tl.info(f'Total torrents set for deletion: {len(self.torrent_hash_delete_list)}')

def tordelete(self):
    """Remove torrents, will also delete files, this keeps the filesystem clean. 
    Only pass self.torrent_hash_delete_list if you would like to keep the files."""
    if self.use_log:
        self.tl.debug('Hash list submitted for deletion:')
        self.tl.debug(self.torrent_hash_delete_list)
    self.qbt_client.torrents_delete(True, self.torrent_hash_delete_list)