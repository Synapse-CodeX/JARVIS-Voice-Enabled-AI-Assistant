from voice_control import VoiceControl
from commands import CommandHandler
import time


class JARVIS:
    def __init__(self):
        self.voice = VoiceControl()
        self.commands = CommandHandler(self.voice)

    def run(self):
        print("""
        ╔══════════════════════════════╗
        ║       JARVIS v3.0 ACTIVE     ║
        ╚══════════════════════════════╝
        """)
        self.voice.speak("Systems online and ready")

        while True:
            try:
                if self.voice.detect_activation():
                    command = self.voice.listen_command()
                    if command:
                        self.commands.handle(command)

            except KeyboardInterrupt:
                self.voice.speak("Shutting down all systems")
                break
            except Exception as e:
                print(f"System Error: {e}")
                time.sleep(1)


if __name__ == "__main__":
    ai = JARVIS()
    ai.run()
