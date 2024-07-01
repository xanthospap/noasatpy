#! /usr/bin/python
#-*- coding: utf-8 -*-

from satellite import cfgio      as scf
from satellite import fitsutils  as cft
from satellite import atroflux   as caf
import os
import argparse

class myFormatter(
        argparse.ArgumentDefaultsHelpFormatter,
        argparse.RawTextHelpFormatter):
    pass

parser = argparse.ArgumentParser(
    formatter_class=myFormatter,
    description='Satellite',
    epilog=('''National Technical University of Athens,
    Dionysos Satellite Observatory\n
Send bug reports to:
  Xanthos Papanikolaou, xanthos@mail.ntua.gr
  Dimitris Anastasiou,dganastasiou@gmail.com
September, 2021'''))

parser.add_argument('-i', '--input-file',
    default=argparse.SUPPRESS,
    metavar='CONFIG_FILE',
    dest='config',
    required=True,
    help='The input configuration file.'
    )
parser.add_argument('--verbose',
    dest='verbose_mode',
    help='Run in verbose mode (show debugging messages)',
    action='store_true'
    )

if __name__ == '__main__':
    #  Parse command line arguments 
    args  = parser.parse_args()

    # Verbose print (function only exists in verbose mode)
    vprint = print if args.verbose_mode else lambda *a, **k: None

    # Read in the config file and store it in a dictionary
    if not os.path.isfile(args.config):
        print('ERROR. Failed locating config file: {:}'.format(args.config), file=sys.stderr)
        os.exit(1)
    cfg = scf.parseConfigInout(args.config)

    # Specific Slit analysis

