#! coding: utf-8

from flask_script import Manager, Server
from flask_script import Command
from app import app

manager = Manager(app)


# customize define command：
class Hello(Command):
    'hello world'

    def run(self):
        print 'hello world'


manager.add_command('hello', Hello())

manager.add_command("runserver", Server())  # add runserver

if __name__ == '__main__':
    manager.run()
