#The fourth file shall be logic to process torrents.
def torprocessor(self):
    for canidate in self.tracker_nonprotected_list:
        if 'ipt' in canidate['tags']:
            self.tl.warning(f'{canidate["name"]} was in non-protected list.')
            break
        if canidate['state'] == 'downloading':
            self.tl.info(f'{canidate["name"]} is still downloading and will be skipped.')
            break
        else:
            self.torrent_hash_delete_list.append(canidate['infohash_v1'])
            self.tl.info(f'Submitted {canidate["name"]} for deletion.') 
    for canidate in self.tracker_protected_list:
        if canidate['state'] == 'downloading':
            self.tl.warning(f'{canidate["name"]} is still downloading and will be skipped.')
            break
        if canidate['ratio'] < float(1.05):
            self.tl.debug(f'{canidate["name"]} is below a 1.05 ratio({canidate["ratio"]})')
            if canidate['added_on'] + self.config["age"] <= self.t.time():
                self.tl.debug(f'Calculation: {canidate["added_on"] + self.config["age"]}')
                self.tl.debug(f'Comparison: {self.t.time()}')
                self.torrent_hash_delete_list.append(canidate['infohash_v1'])
                self.tl.info(f'Submitted {canidate["name"]} for deletion from the protected list.') 
        if canidate['ratio'] >= float(1.05):
            self.tl.debug(f'{canidate["name"]} is above a 1.05 ratio({canidate["ratio"]}).')  
            self.torrent_hash_delete_list.append(canidate['infohash_v1'])
            self.tl.info(f'Submitted {canidate["name"]} for deletion from the protected list.')
        else:
            pass

def printprocessor(self):
    self.tl.info(f'Protected torrents: {len(self.tracker_protected_list)}')
    self.tl.info(f'Non-protected torrents: {len(self.tracker_nonprotected_list)}')
    self.tl.info(f'Total torrents set for deletion: {len(self.torrent_hash_delete_list)}')

def tordelete(self):
    self.tl.debug(self.torrent_hash_delete_list)
    self.qbt_client.torrents_delete(True, self.torrent_hash_delete_list)