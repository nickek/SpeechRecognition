import datetime


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
    else:
        engine.say(f'I cant find the command: {command}.')
        engine.runAndWait()
        return


def time(command, engine):
    if 'time' or 'time?' in command:
        Time = datetime.datetime.now().strftime("%H:%M:%S")
        engine.say('The current time is')
        engine.say(Time)
        engine.runAndWait()
        return
