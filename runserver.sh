#!/bin/sh
nohup python manage.py runserver 0.0.0.0:8888 1>nohup_stdout.out 2>nohup_stderr.out  &

