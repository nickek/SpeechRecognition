import subprocess
import sys

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
    