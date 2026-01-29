import requests
from bs4 import BeautifulSoup

def extract_text_from_url(url: str) -> str:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    paragraphs = [p.get_text() for p in soup.find_all("p")]
    text = " ".join(paragraphs)

    return text.strip()[:5000]  # safety cap
