#!/usr/bin/env python
import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description='Set alarms to launch and play Spotify playlist/track.')

    parser.add_argument('time', help='Set alarm for this time. (ie. 13:52)', nargs='?')
    parser.add_argument('-uri', help='Spotify track/playlist uri.')
    parser.add_argument('-l', '--list', help='List currently set alarms.', action='store_true')
    parser.add_argument('-d', '--delete', help='Delete alarm at time (ie. 13:52)', metavar='time')

    args = parser.parse_args()

    if args.uri and args.time:
        print 'set alarm at time with uri'
    elif args.time:
        print 'set alarm at time'
    elif args.uri:
        print 'set default uri'

    if args.list or not len(sys.argv) > 1:
        print 'list of alarms'

    if args.delete:
        print 'delete alarm at time'


if __name__ == '__main__':
    main()