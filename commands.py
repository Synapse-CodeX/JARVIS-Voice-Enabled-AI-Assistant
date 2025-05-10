import webbrowser
import os
import datetime
from config import AppConfig


class CommandHandler:
    def __init__(self, voice_control):
        self.voice = voice_control
        self.config = AppConfig()

    def handle(self, command):
        """Main command processing hub"""
        if self._handle_websites(command):
            return True

        if self._handle_system(command):
            return True

        if self._handle_time(command):
            return True

        self.voice.speak("Command not recognized")
        return False

    def _handle_websites(self, command):
        """All website-related commands"""
        sites = {
            'youtube': 'https://youtube.com',
            'google': 'https://google.com',
            'github': 'https://github.com'
        }

        for site, url in sites.items():
            if site in command and ('open' in command or 'launch' in command):
                webbrowser.open(url)
                self.voice.speak(f"Opening {site}")
                return True
        return False

    def _handle_system(self, command):
        """System control commands"""
        if 'time' in command:
            current = datetime.datetime.now().strftime("%I:%M %p")
            self.voice.speak(f"The time is {current}")
            return True

        if 'date' in command:
            current = datetime.datetime.now().strftime("%A, %B %d")
            self.voice.speak(f"Today is {current}")
            return True

        return False

    def _handle_time(self, command):
        """Time-related commands"""
        if 'shutdown' in command:
            self.voice.speak("Confirm system shutdown?")
            return True

        if 'exit' in command or 'quit' in command:
            self.voice.speak("Goodbye sir")
            exit()

        return False
