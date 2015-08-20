#!/usr/bin/env python
import sys
import os
import argparse
import shelve
from appdirs import AppDirs

DIRS = AppDirs('spotify-alarm', 'vikram')
if not os.path.exists(DIRS.user_data_dir):
    os.makedirs(DIRS.user_data_dir)

DB_FILENAME = "alarm_data"
SHELVE_PATH = os.path.join(DIRS.user_data_dir,DB_FILENAME)

URI_KEY = 'default_uri'

def validate_time(time):
    if time:
        parsedTime = time.split(':')
        if len(parsedTime) != 2:
            return False
        else:
            try:
                hour = int(parsedTime[0])
                minute = int(parsedTime[1])
                if hour < 0 or hour >= 24 or minute < 0 or minute >= 60:
                    return False
            except ValueError:
                return False
    return True

def set_alarm(time):
    #add to list.
    #grab default and call helper.
    return

def set_alarm(time, uri):
    #add to list.
    #call helper directly.
    return

def set_alarm_helper(time, uri):
    #schedules alarm with the system.
    return

def set_default(uri):
    #sets default playlist/track.
    db = shelve.open(SHELVE_PATH)
    db[URI_KEY] = uri
    db.close()
    return

def delete_alarm(time):
    #remove from list and unschedule.
    return

def print_alarm():
    #print list
    db = shelve.open(SHELVE_PATH)
    try:
        print db[URI_KEY]
    except KeyError:
        print 'No default alarm set.'

    return

def main():
    parser = argparse.ArgumentParser(description='Set alarms to launch and play Spotify playlist/track.')

    parser.add_argument('time', help='Set alarm for this time. (ie. 13:52)', nargs='?')
    parser.add_argument('-uri', help='Spotify track/playlist uri.')
    parser.add_argument('-l', '--list', help='List currently set alarms.', action='store_true')
    parser.add_argument('-d', '--delete', help='Delete alarm at time (ie. 13:52)', metavar='time')

    args = parser.parse_args()

    if validate_time(args.time) and validate_time(args.delete) :
        if args.uri and args.time:
            print 'set alarm at time with uri'
        elif args.time:
            print 'set alarm at time'
        elif args.uri:
            set_default(args.uri)

        if args.list or not len(sys.argv) > 1:
            print_alarm()

        if args.delete:
            print 'delete alarm at time'
    else:
        print 'Please double check the format of the time you would like the alarm to be set/deleted.'

if __name__ == '__main__':
    main()