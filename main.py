#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys
import argparse
from deploy import *

try:
    parser = argparse.ArgumentParser(description='Install an OpenEPR application')

    parser.add_argument('folder', type = str, help = 'The base folder of the application')
    parser.add_argument('-f', '--filename', type = str, help = 'The filename path where the app definition is store', default = './app.json')
    parser.add_argument('-l', '--log', type = str, help = 'The filename path where store the logs', default = None)
    parser.add_argument('-o', '--without-openerp', help = 'Dont\'t install the OpenERP section', action="store_true", default = False, dest = 'without_openerp')
    parser.add_argument('-s', '--show-config', help = 'Show the OpenEPR\'s configuration file', action="store_true", default = False, dest = 'show_config')
    parser.add_argument('-c', '--create-config', help = 'Create the OpenEPR\'s configuration file', default = None, dest = 'create_config')

    args = parser.parse_args()

    deploy = deploy.Deploy(args.filename, args.log)

    deploy.setBasePath(args.folder)
    deploy.setWithoutOpenerp(args.without_openerp)

    deploy.process()

    if args.show_config:
        print deploy.showOpenerpConfig()

    if args.create_config:
        pass

except Exception as e:
    sys.exit(str(e))