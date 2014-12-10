#!/bin/bash
kill -9 `ps axw | grep manage.py | grep -v grep | cut -d ' ' -f 1`
