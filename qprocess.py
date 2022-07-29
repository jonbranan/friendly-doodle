def torprocessor(self):
    """Main logic to sort through both self.tracker_nonprotected_list and self.tracker_protected_list
    If torrent meets criteria for deletion, its infohash_v1 will be appended to self.torrent_hash_delete_list
    """
    for canidate in self.tracker_list:
        if canidate['state'] == 'downloading':
            if self.use_log:
                self.tl.info(f'["{canidate["name"][0:20]}..."] is still downloading and will be skipped.')
            continue
        elif canidate['ratio'] < float(1.05) and self.tracker_protected_tag in canidate["tags"]:
            if self.use_log:
                self.tl.debug(f'["{canidate["name"][0:20]}..."] is below a 1.05 ratio({canidate["ratio"]})')
            if canidate['added_on'] + self.age <= self.t.time():
                if self.use_log:
                    self.tl.debug(f'["{canidate["name"][0:20]}..."] Seconds old: {self.t.time() - self.age - canidate["added_on"]}')
                self.torrent_hash_delete_list.append(canidate['infohash_v1'])
                if self.use_log:
                    self.tl.info(f'Submitted ["{canidate["name"][0:20]}..."] for deletion from the protected list.') 
        elif canidate['ratio'] >= float(1.05) and self.tracker_protected_tag in canidate["tags"]:
            if self.use_log:
                self.tl.debug(f'["{canidate["name"][0:20]}..."] is above a 1.05 ratio({canidate["ratio"]}).')  
            self.torrent_hash_delete_list.append(canidate['infohash_v1'])
            if self.use_log:
                self.tl.info(f'Submitted ["{canidate["name"][0:20]}..."] for deletion from the protected list.')
        elif self.tracker_non_protected_tag in canidate["tags"]:
            self.torrent_hash_delete_list.append(canidate['infohash_v1'])
            if self.use_log:   
                self.tl.info(f'Submitted ["{canidate["name"][0:20]}..."] for deletion.')
        else:
            self.tl.info(f'["{canidate["name"][0:20]}..."] is orphaned.')
            self.up_tor_counter += 1
            continue

def tordeletetags(self):
    tag_list = [self.tracker_protected_tag, self.tracker_non_protected_tag]
    self.qbt_client.torrents_delete_tags(tag_list)

def tordelete(self):
    """Remove torrents, will also delete files, this keeps the filesystem clean. 
    Only pass self.torrent_hash_delete_list if you would like to keep the files."""
    if self.use_log:
        self.tl.debug('Hash list submitted for deletion:')
        self.tl.debug(self.torrent_hash_delete_list)
    self.qbt_client.torrents_delete(True, self.torrent_hash_delete_list)