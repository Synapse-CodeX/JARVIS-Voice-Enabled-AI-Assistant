import speech_recognition as sr

def test_microphone():
    r = sr.Recognizer()
    print("Available microphones:")
    print(sr.Microphone.list_microphone_names())

    with sr.Microphone() as source:
        print("\nSpeak 'JARVIS' clearly into your microphone...")
        r.adjust_for_ambient_noise(source, duration=2)
        audio = r.listen(source, timeout=5)

    try:
        text = r.recognize_google(audio).lower()
        print(f"System heard: {text}")
        return "jarvis" in text
    except Exception as e:
        print(f"Error: {e}")
        return False


if test_microphone():
    print("Microphone working! JARVIS heard you.")
else:
    print("Microphone not detecting speech properly.")
