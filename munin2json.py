#!/usr/bin/python

from telnetlib import Telnet
import datetime
import json
import platform

data = {}
data['hostname'] = platform.node()
data['timestamp'] = datetime.datetime.utcnow().isoformat("T") + "Z"

with Telnet('localhost', 4949) as tn:
    tn.read_until(b'\n')
    tn.write("list".encode('ascii') + b"\n")
    fields = tn.read_until(b'\n').decode('ascii').split()

    for group in fields:
        if not group in ["pending", "fail2ban"]:
            tn.write(("fetch " + group).encode('ascii') + b"\n")
            fields = tn.read_until(b'.\n').decode('ascii').split("\n")[:-2]
            for field in fields:
                (k,value) = field.split(' ', 1)
                key = (group + "." + k.split('.')[0])
                data[key] = value

print(json.dumps(data))
