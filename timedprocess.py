
#!/usr/bin/python

# Created by Aaron Delaney - devoxel.net
# GNU General Public License (see LICENSE)

import subprocess
import click
import re
import sys

from time import sleep

class StringTimeType(click.ParamType):
    name = 'time'

    def convert_times_to_seconds(self, times):
        units = {'s': 1, 'm': 60, 'h':60*60}
        seconds = 0
        for time in times:
            time_value = int(time[:len(time)-1])
            time_unit = time[-1]
            seconds += units[time_unit] * time_value
        return seconds

    def convert(self, value, param, ctx):
        pattern = '([0-9]+[smh])'
        results = re.findall(pattern, value)
        try:
            if len(results) <= 0:
                raise ValueError
            return self.convert_times_to_seconds(results)
        except ValueError:
            self.fail("%s is not a valid duration" % value, param, ctx)


# Start Click Definitions #####################
stringtime = StringTimeType()
CONTEXT_SETTINGS = dict(help_option_names=['-h', '-help', '--help'])

@click.command(context_settings=CONTEXT_SETTINGS, options_metavar='<options>')

@click.option("--show-time-remaining", help="flag to show the time remaining", is_flag=True)

@click.argument("duration", type=stringtime, metavar="<duration>")

@click.argument("path", type=click.Path(exists=True, dir_okay=False), metavar="<path>")
###############################################

def cli(show_time_remaining, duration, path):
    """
    A simple command line tool to run a program for a specified duration

    <duration> = how long you wish your program to run

    <path> = path to file you wish to run
    """
    try:
        popen_process = subprocess.Popen(path)
        sleep_iterator = [1] * duration
        time_left = duration
        seperator = '='*5
        output = (seperator + 'running the program - PID: ' + popen_process.pid + seperator)
        for time_to_sleep in sleep_iterator:
            if show_time_remaining:
                click.echo("Time Remaining: %s seconds" % time_left)
            time_left = time_left - time_to_sleep
            sleep(time_to_sleep)
        popen_process.terminate()

        if duration % time_left == 0:
            returncode = popen_process.poll()
            if returncode != None:
                click.echo("Process has terminated. Termination code: %s" % returncode)
                sys.exit(0)

    except OSError:
        click.echo("Error running file. Do you have permission and is the path correct?")
        sys.exit(-1)

    except WindowsError:
        click.echo("Error running file. Do you have permission and is the path correct?")
        sys.exit(-1)

    sys.exit(0)

if __name__ == "__main__":
    cli()
