# qbit-maid

Warning: This application removes torrents that aren't downloading and that aren't from iptorrents. Age in the config.json only controls the age for torrents from iptorrents.

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

You will need a config.json in the root directory.

It should look something like this:
{
    "host": "192.168.1.1",
    "port": 8080,
    "username": "admin",
    "password": "admin",
    "loglevel": "INFO",
    "logpath": "./qc.log",
    "age": 2419200
}

loglevel is what log messages are written to the log file. It only accepts INFO or DEBUG.

Age is a number in seconds for how long we keep torrents from IPTORRENTS.