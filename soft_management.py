
import os


def start(command):
    os.system('sh start.sh '+command)


def stop(command):
    os.system('sh stop.sh')


def restart(command):
    pass


def install():
    os.system('sh install.sh')


def uninstall():
    pass


def usage():
    pass


def menu():
    print('''
    1.install
    2.uninstall
    3.start
    4.stop
    5.restart
''')


menu()
command = input('Enter a command & arguments:')
args = command.split(' ')
if args[0] == 'install':
    install()
elif args[0] == 'uninstall':
    uninstall()
elif args[0] == 'start':
    start(args[1])
elif args[0] == 'stop':
    stop()
elif args[0] == 'restart':
    restart()
else:
    usage()
