#!/usr/local/bin/bash

ansible -m raw -a "sudo env ASSUME_ALWAYS_YES=YES pkg install python" -vvv -i hosts redpaw
