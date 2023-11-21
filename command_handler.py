import subprocess
import sys
import datetime


def command_handler(command, engine):
    if 'shut down' in command:
        if 'cancel' in command:
            subprocess.run('shutdown /a', shell=True)
            engine.say('Okay Cancelled shutdown.')
            engine.runAndWait()
            return
        subprocess.run('shutdown /s /t 3600', shell=True)
        engine.say('Okay Shutting down in one hour.')
        engine.runAndWait()
        return
    elif 'exit' in command:
        engine.say('Okay exitting program.')
        engine.runAndWait()
        sys.exit()
    else:
        engine.say(f'I Cant find the command: {command}.')
        engine.runAndWait()
        return


def date(command, engine):
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    year = datetime.datetime.now().year
    if 'date' or 'date?' in command:
        engine.say(month)
        engine.say(day)
        engine.say(year)
        engine.runAndWait()
        return
    # else:
    #     engine.say(f'I cant find the command: {command}.')
    #     engine.runAndWait()
    #     return


def time(command, engine):
    if 'time' or 'time?' in command:
        Time = datetime.datetime.now().strftime("%H:%M:%S")
        engine.say('The current time is')
        engine.say(Time)
        engine.runAndWait()
        return
