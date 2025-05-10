import speech_recognition as sr
import pyttsx3
import time
from config import VoiceConfig


class VoiceControl:
    def __init__(self):
        self.config = VoiceConfig()
        self.engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()
        self._setup_voice_engine()
        self._setup_recognizer()

    def _setup_voice_engine(self):
        """Configure text-to-speech settings"""
        self.engine.setProperty('rate', self.config.speech_rate)
        self.engine.setProperty('volume', self.config.speech_volume)
        if self.config.voice_id:
            self.engine.setProperty('voice', self.config.voice_id)

    def _setup_recognizer(self):
        """Configure speech recognition settings"""
        self.recognizer.energy_threshold = self.config.energy_threshold
        self.recognizer.pause_threshold = self.config.pause_threshold
        self.recognizer.dynamic_energy_threshold = True
        self.recognizer.non_speaking_duration = 0.3

    def speak(self, text):
        """Convert text to speech with visual feedback"""
        print(f"\nJARVIS: {text}")
        self.engine.say(text)
        self.engine.runAndWait()

    def detect_activation(self):
        """Listen specifically for 'JARVIS' wake word"""
        with sr.Microphone(device_index=self.config.mic_index) as source:
            print("\n🔈 Waiting for 'JARVIS'...")
            try:
                audio = self.recognizer.listen(
                    source,
                    timeout=self.config.activation_timeout,
                    phrase_time_limit=2
                )
                heard = self.recognizer.recognize_google(audio).lower()
                return "jarvis" in heard
            except:
                return False

    def listen_command(self):
        """Listen for actual command after activation"""
        with sr.Microphone(device_index=self.config.mic_index) as source:
            self.speak("How can I help?")
            print("\n🎤 Listening for command...")
            try:
                audio = self.recognizer.listen(
                    source,
                    timeout=self.config.command_timeout,
                    phrase_time_limit=self.config.phrase_limit
                )
                command = self.recognizer.recognize_google(audio).lower()
                print(f"You: {command}")
                return command
            except sr.UnknownValueError:
                self.speak("I didn't catch that")
                return None
            except Exception as e:
                print(f"Audio Error: {e}")
                return None
