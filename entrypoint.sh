#!/bin/sh

CRON_CONFIG_FILE="/opt/crontab"

echo "${CRON} python /opt/qbit-maid.py" > $CRON_CONFIG_FILE

exec supercronic -passthrough-logs -quiet $CRON_CONFIG_FILE