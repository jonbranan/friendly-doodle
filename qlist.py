def build_tor_list(self):
        """Builds multiple lists of torrents to be sorted. Also adds tags to the torents.
        There are more effecient ways of doing things but I did this rather quickly.
        V2 will certainly be more performant. The reason two lists were used was so that torrents 
        that are in public trackers woudln't be around as long as torrents from a private tracker.
        """
        self.total_torrents = len(self.torrentlist) 
        while self.torrentlist:
            torrent = self.torrentlist.pop()
            if self.use_log:
                self.tl.debug(f'["{torrent["name"][0:20]}..."] {torrent["infohash_v1"]}')
            if is_ignored_tag(self.ignored_tags.values(),torrent['tags']):
                self.ignored_counter += 1
                continue
            # if torrent['added_on'] + self.minimum_age >= self.t.time():
            if is_preme(torrent['added_on'], self.minimum_age, self.t.time()):
                self.preme_tor_counter += 1
                continue
            # if torrent['category'] in self.cat_whitelist.values():
            if is_cat_ignored(torrent['category'], self.cat_whitelist.values()):
                self.tl.info(f'Ignored torrent:["{torrent["name"][0:20]}..."]')
                self.ignored_counter += 1
                continue
            # if torrent['tracker'] == '':
            if is_tracker_blank(torrent['tracker']):
                if self.use_log:
                    self.tl.warning(f'Torrent doesn\'t have a tracker ["{torrent["name"][0:20]}..."] [{torrent["tracker"]}]hash: {torrent["hash"]}')
                self.ignored_counter += 1
                continue
            # if torrent['tracker'].split('/')[2] in self.tracker_whitelist.values():
            if is_protected_tracker(torrent['tracker'], self.tracker_whitelist.values()):
                if self.use_log:
                    self.tl.debug(f'Protected torrent: {torrent["tracker"]}hash: {torrent["hash"]}')
                # if torrent['tags'] == '':
                if is_tag_blank(torrent['tags']):
                    self.qbt_client.torrents_add_tags(self.tracker_protected_tag,torrent['hash'])
                self.tracker_list.append(torrent)
            if is_not_protected_tracker(torrent['tracker'], self.tracker_whitelist.values()):
                if self.use_log:
                    self.tl.debug(f'Non-protected torrent: {torrent["tracker"]}hash: {torrent["hash"]}')
                # if torrent['tags'] == '':
                if is_tag_blank(torrent['tags']):
                    self.qbt_client.torrents_add_tags(self.tracker_non_protected_tag,torrent['hash'])
                self.tracker_list.append(torrent)

def is_preme(added, minage, time):
    if added + minage >= time:
        return True

def is_cat_ignored(cat, catlist):
    if cat in catlist:
        return True

def is_tracker_blank(tracker):
    if tracker == '':
        return True

def is_protected_tracker(tracker, trackerlist):
    if tracker.split('/')[2] in trackerlist:
        return True

def is_not_protected_tracker(tracker, trackerlist):
    if tracker.split('/')[2] not in trackerlist:
        return True

def is_tag_blank(tag):
    if tag == '':
        return True

def is_ignored_tag(igtags, tortags):
    for igt in igtags:
        if igt in tortags:
            return True