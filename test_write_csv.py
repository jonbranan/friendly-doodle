from qprocess import write_csv
import csv
import unittest
import os
# Torrent Items needed for testing
# canidate['state'] {canidate["ratio"]} {torrent["tags"]} torrent["seeding_time"] {torrent["category"]} {torrent["name"][0:20]} {canidate["time_active"]}
class TestWriteCSV(unittest.TestCase):
    def test_write_csv_dragnet(self):
        self.cv = csv
        outfile = './test_dragnet_outfile.csv'
        state = 'downloading'
        ratio = 1.05
        tags = 'ipt'
        added = 1
        age = 240000
        time = 123456
        thash = 'asfasdf23412adfqwer'
        tname = 'thisismynamehahahah'
        trname = 'https://localhost.stackoverflow.tech/317332f1c125bc9c1b9b14fb8e054908/announce'
        header = ['state','ratio','tags','added','age','time','thash','tname','trname']
        row = [state,ratio,tags,added,age,time,thash,tname,trname]
        write_csv(self.cv,outfile,header,row)
        self.assertTrue(os.path.exists(outfile))

    def test_write_csv_telemetry(self):
        self.cv = csv
        outfile = './test_telemetry_outfile.csv'
        state = 'downloading'
        ratio = 1.05
        tags = 'ipt'
        added = 1
        thash = 'asfasdf23412adfqwer'
        tname = 'thisismynamehahahah'
        trname = 'https://localhost.stackoverflow.tech/317332f1c125bc9c1b9b14fb8e054908/announce'
        header = ['state','ratio','tags','added','hash','name','tracker']
        row = [state,ratio,tags,added,thash,tname,trname]
        write_csv(self.cv,outfile,header,row)
        self.assertTrue(os.path.exists(outfile))

if __name__ == '__main__':
    unittest.main()