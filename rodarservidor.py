#!/usr/bin/env python

from os import environ
from sys import argv

if len(argv) == 3 and argv[1] == '--env':
    environ['CONTASDOAPE_ENV'] = argv[2].upper() 

from contasdoape.web import app
app.run()
