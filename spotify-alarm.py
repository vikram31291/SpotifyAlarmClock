#!/usr/bin/env python
import sys
import argparse
import shelve

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
    return

def delete_alarm(time):
    #remove from list and unschedule.
    return

def print_alarm():
    #print list
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
            print 'set default uri'

        if args.list or not len(sys.argv) > 1:
            print 'list of alarms'

        if args.delete:
            print 'delete alarm at time'
    else:
        print 'Please double check the format of the time you would like the alarm to be set/deleted.'

if __name__ == '__main__':
    main()