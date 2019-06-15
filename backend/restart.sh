#!/bin/bash
killall -9 uwsgi
sleep 1
uwsgi --ini uwsgi.ini
