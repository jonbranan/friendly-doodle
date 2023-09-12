def tor_processor(self):
    """Main logic to sort through both self.tracker_nonprotected_list and self.tracker_protected_list
    If torrent meets criteria for deletion, its infohash_v1 will be appended to self.torrent_hash_delete_list
    """
    for canidate in self.tracker_list:
        if self.use_log:
            self.tl.debug(f'---Reviewing canidate: ["{canidate["name"][0:20]}..."] {canidate["infohash_v1"]}---')
        if is_downloading(canidate['state']):
            if self.use_log:
                self.tl.info(f'["{canidate["name"][0:20]}..."] is still downloading and will be skipped.')
            continue
        elif is_protected_under_ratio(canidate['ratio'], 1.05, self.tracker_protected_tag, canidate["tags"]):
            if self.use_log:
                self.tl.debug(f'["{canidate["name"][0:20]}..."] is below a 1.05 ratio({canidate["ratio"]})')
            if is_old_tor(canidate['time_active'], self.max_age):
                if self.use_log:
                    self.tl.debug(f'["{canidate["name"][0:20]}..."] Seconds old: {canidate["time_active"]} Delta: {canidate["time_active"] - self.max_age}')
                self.torrent_hash_delete_list.append(canidate['infohash_v1'])
                if self.use_log:
                    self.tl.info(f'Submitted ["{canidate["name"][0:20]}..."] for deletion from the protected list.') 
        elif is_protected_over_ratio(canidate['ratio'], 1.05, self.tracker_protected_tag, canidate["tags"]):
            if self.use_log:
                self.tl.debug(f'["{canidate["name"][0:20]}..."] is above a 1.05 ratio({canidate["ratio"]}).')  
            self.torrent_hash_delete_list.append(canidate['infohash_v1'])
            if self.use_log:
                self.tl.info(f'Submitted ["{canidate["name"][0:20]}..."] for deletion from the protected list.')
        elif is_not_protected_tor(self.tracker_non_protected_tag, canidate["tags"]):
            self.torrent_hash_delete_list.append(canidate['infohash_v1'])
            if self.use_log:   
                self.tl.info(f'Submitted ["{canidate["name"][0:20]}..."] for deletion.')
        else:
            if self.enable_dragnet:
                dragnet(self.cv,self.dragnet_outfile,canidate['state'],canidate['ratio'],canidate["tags"],canidate['added_on'],self.age,self.t.time(),canidate['infohash_v1'],canidate["name"][0:20],canidate['tracker'])
            self.tl.info(f'["{canidate["name"][0:20]}..."] is orphaned.')
            self.up_tor_counter += 1
            continue

def tor_delete_tags(self):
    tag_list = [self.tracker_protected_tag, self.tracker_non_protected_tag]
    self.qbt_client.torrents_delete_tags(tag_list)

def tor_delete(self):
    """Remove torrents, will also delete files, this keeps the filesystem clean. 
    Only pass self.torrent_hash_delete_list if you would like to keep the files."""
    if self.use_log:
        self.tl.debug('Hash list submitted for deletion:')
        self.tl.debug(self.torrent_hash_delete_list)
    if self.torrent_hash_delete_list:
        self.qbt_client.torrents_delete(True, self.torrent_hash_delete_list)

def is_downloading(state):
    if state == 'downloading':
        return True

def is_protected_under_ratio(torratio, setratio, settag, tortag):
    if torratio < float(setratio) and settag in tortag:
        return True

def is_old_tor(realage, maxage):
    if realage >= maxage:
        return True

def is_protected_over_ratio(torratio, setratio, settag, tortag):
    if torratio >= float(setratio) and settag in tortag:
        return True

def is_not_protected_tor(setnonprotectedtag, tortags):
    if setnonprotectedtag in tortags:
        return True

def dragnet(csv_obj,outfile,state,ratio,tags,added,age,time,thash,tname,trname):
    header = ['state','ratio','tags','added','age','time','thash','tname','trname']
    row = [state,ratio,tags,added,age,time,thash,tname,trname]
    with open(outfile, 'a+', encoding='UTF8', newline='') as f:
        writer = csv_obj.writer(f)
        if f.tell() == 0:
            writer.writerow(header)
        writer.writerow(row)