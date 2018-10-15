# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.
#
# This is a simple skill based on the HelloWorld Skill that shuts down the computer when asking for it. 
# It does not require root.

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_file_handler
from mycroft.util.log import getLogger
import os

__author__ = 'syner1'

LOGGER = getLogger(__name__)



class mmSkill(MycroftSkill):

    def __init__(self):
        super(mmSkill, self).__init__(name="mmSkill")

    def initialize(self):
        self.tasks = self.translate_namedvalues('tasks')

        shutdown_intent = IntentBuilder("shutdownIntent").\
                          require("shutdownKeyword").build()
        self.register_intent(shutdown_intent, self.handle_shutdown_intent)

        restart_intent = IntentBuilder("restartIntent").\
                         require("restartKeyword").build()
        self.register_intent(restart_intent,
                             self.handle_restart_intent)

        start_intent = IntentBuilder("startIntent").\
                         require("startKeyword").build()
        self.register_intent(start_intent,
                             self.handle_start_intent)


    def getUserConfirmation(self, task):
        assert task

        data = {'task' : task}
        utter = self.ask_yesno('confirmation', data)

        if utter == 'yes':
            return True

    @intent_file_handler('powerOff.intent')
    def handle_shutdown_intent(self, message):
        if self.getUserConfirmation(self.tasks['poweroff']):
            self.speak_dialog("shuttingDown")
            os.system("pm2 delete mm")

    @intent_file_handler('reboot.intent')
    def handle_restart_intent(self, message):
        if self.getUserConfirmation(self.tasks['reboot']):
            self.speak_dialog("restart")
            os.system("pm2 restart mm")

    @intent_file_handler('boot.intent')
    def handle_start_intent(self, message):
        if self.getUserConfirmation(self.tasks['boot']):
            self.speak_dialog("start")
            os.system("pm2 start ~/mm.sh")

    def stop(self):
        pass

def create_skill():
    return mmSkill()

