def torprocessor(self):
    """Main logic to sort through both self.tracker_nonprotected_list and self.tracker_protected_list
    If torrent meets criteria for deletion, its infohash_v1 will be appended to self.torrent_hash_delete_list
    """
    for canidate in self.tracker_list:
        # if canidate['state'] == 'downloading':
        if isdownloading(canidate['state']):
            if self.use_log:
                self.tl.info(f'["{canidate["name"][0:20]}..."] is still downloading and will be skipped.')
            continue
        # elif canidate['ratio'] < float(1.05) and self.tracker_protected_tag in canidate["tags"]:
        elif isprotectedunderratio(canidate['ratio'], 1.05, self.tracker_protected_tag, canidate["tags"]):
            if self.use_log:
                self.tl.debug(f'["{canidate["name"][0:20]}..."] is below a 1.05 ratio({canidate["ratio"]})')
            # if canidate['added_on'] + self.age <= self.t.time():
            if isoldtor(canidate['added_on'], self.age, self.t.time()):
                if self.use_log:
                    self.tl.debug(f'["{canidate["name"][0:20]}..."] Seconds old: {self.t.time() - self.age - canidate["added_on"]}')
                self.torrent_hash_delete_list.append(canidate['infohash_v1'])
                if self.use_log:
                    self.tl.info(f'Submitted ["{canidate["name"][0:20]}..."] for deletion from the protected list.') 
        # elif canidate['ratio'] >= float(1.05) and self.tracker_protected_tag in canidate["tags"]:
        elif isprotectedoverratio(canidate['ratio'], 1.05, self.tracker_protected_tag, canidate["tags"]):
            if self.use_log:
                self.tl.debug(f'["{canidate["name"][0:20]}..."] is above a 1.05 ratio({canidate["ratio"]}).')  
            self.torrent_hash_delete_list.append(canidate['infohash_v1'])
            if self.use_log:
                self.tl.info(f'Submitted ["{canidate["name"][0:20]}..."] for deletion from the protected list.')
        # elif self.tracker_non_protected_tag in canidate["tags"]:
        elif isnonprotectedtor(self.tracker_non_protected_tag, canidate["tags"]):
            self.torrent_hash_delete_list.append(canidate['infohash_v1'])
            if self.use_log:   
                self.tl.info(f'Submitted ["{canidate["name"][0:20]}..."] for deletion.')
        else:
            dragnet(self,canidate['state'],canidate['ratio'],canidate["tags"],canidate['added_on'],self.age,self.t.time(),canidate['infohash_v1'],canidate["name"][0:20])
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

def isdownloading(state):
    if state == 'downloading':
        return True

def isprotectedunderratio(torratio, setratio, settag, tortag):
    if torratio < float(setratio) and settag in tortag:
        return True

def isoldtor(toradd, setage, currenttime):
    if toradd + setage <= currenttime:
        return True

def isprotectedoverratio(torratio, setratio, settag, tortag):
    if torratio >= float(setratio) and settag in tortag:
        return True

def isnonprotectedtor(setnonprotectedtag, tortags):
    if setnonprotectedtag in tortags:
        return True

def dragnet(self,state,ratio,tags,added,age,time,thash,tname):
    header = ['state','ratio','tags','added','age','time','thash','tname']
    row = [state,ratio,tags,added,age,time,thash,tname]
    with open('./orphanedtorrents.csv', 'w', encoding='UTF8', newline='') as f:
        writer = self.cv.writer(f)
        if f.tell() == 0:
            writer.writerow(header)
        writer.writerow(row)