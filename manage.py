#!/usr/bin/env python3
from flask_script import Manager

from app import application

import sys
sys.path.append("/var/www/app/")

manager = Manager(application)

if __name__ == '__main__':
    manager.run()
