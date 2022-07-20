# qbit-maid

Warning: This application removes torrents that aren't downloading and that aren't from iptorrents. Age in the config.json only controls the age for torrents from iptorrents.

The objective is to filter torrents based on the following criteria:
- tracker domain name
- age
- ratio
- state

Client to the qbit api and the processing of the torrents.
qbit-clean.py

Functions to build out a list of torrents.
qlist.py

Logging and push notification communication.
qlogging.py

Logic to process torrents.
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
    "age": 2419200,
    "use_pushover": true,
    "po_key": "",
    "po_token": ""
}

loglevel - is what log messages are written to the log file. It only accepts INFO or DEBUG.

age - is a number in seconds for how long we keep torrents from IPTORRENTS.