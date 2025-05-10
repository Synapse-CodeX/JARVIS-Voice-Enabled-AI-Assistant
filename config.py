class VoiceConfig:
    def __init__(self):
        self.mic_index = 0  
        self.energy_threshold = 3000  
        self.dynamic_energy_threshold = True
        self.pause_threshold = 0.8

        self.activation_timeout = 3  
        self.command_timeout = 5  
        self.phrase_limit = 6 

        self.speech_rate = 170
        self.speech_volume = 0.9
        self.voice_id = None  


class AppConfig:
    def __init__(self):
        self.user = "Sir"
        self.weather_api_key = ""  
