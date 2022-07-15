# qbit-maid

The objective is to filter torrents based on the following criteria:
- tracker domain name
- age
- ratio
- state

The first file shall contain an client to the qbit api and the processing of the torrents.
qbit-clean.py

The second file shall contain functions to build out a list of torrents.
qlist.py

The third file shall contain logging and email communication.
qlogging.py

The fourth file shall be logic to process torrents.
qprocess.py