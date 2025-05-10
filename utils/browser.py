import webbrowser
from voice_control import speak

WEBSITES = {
    "youtube": "https://youtube.com",
    "google": "https://google.com",
    "github": "https://github.com",
    "wikipedia": "https://wikipedia.org"
}


def search_web(command):
    """Smart search with URL encoding"""
    from urllib.parse import quote
    query = command.split("search")[-1].strip()
    if not query:
        query = command.split("google")[-1].strip()

    if query:
        url = f"https://www.google.com/search?q={quote(query)}"
        webbrowser.open(url)
        speak(f"Searching for {query}")


def open_website(command):
    """Enhanced website opening with suggestions"""
    target = next(
        (site for site in WEBSITES
         if site in command.lower()),
        None
    )

    if target:
        webbrowser.open(WEBSITES[target])
        speak(f"Opening {target}")
    else:
        speak(f"I know these websites: {', '.join(WEBSITES.keys())}")
