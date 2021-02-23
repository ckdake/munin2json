Connects to a locally running munin-node and dumps all output to JSON.

Needs a lot of work including extracting config to file, error handling, etc.

Run this with cron every 5 min to pipe to a log file for https://docs.honeycomb.io/getting-data-in/integrations/honeytail/ . If you want

run like `python3 munin2json.py >> /var/log/muninjson.log`

in a cron.d file: 

MAILTO=root

*/5 * * * * 	python3 /root/munin2json/munin2json.py >> /var/log/munin-json.log


in a logrotate.d file:

/var/log/munin/munin-json.log {
        daily
        missingok
        rotate 7
        compress
        delaycompress
        notifempty
        copytruncate
}

in a honeytail something or other:

honeytail \
    --writekey=YOUR_KEY \
    --parser=json \
    --dataset="System Metrics" \
    --file /var/log/munin-json.log

