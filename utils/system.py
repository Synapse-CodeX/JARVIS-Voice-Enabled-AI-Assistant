import os
import platform
import subprocess
from voice_control import speak


def handle_system_command(command):
    """Safer system operations with confirmation"""
    if "shutdown" in command:
        speak("Are you sure you want to shutdown? Say 'confirm' to proceed.")
        if listen().lower() == "confirm":
            if platform.system() == "Windows":
                os.system("shutdown /s /t 1")
            else:
                subprocess.run(["shutdown", "-h", "now"])

    elif "restart" in command:
        speak("Confirm system restart? Say 'confirm' to proceed.")
        if listen().lower() == "confirm":
            if platform.system() == "Windows":
                os.system("shutdown /r /t 1")
            else:
                subprocess.run(["reboot"])
