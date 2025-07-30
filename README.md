# DarkWeb_Monitering
A Python-based system to monitor .onion sites and Telegram channels for potential data breaches.

## Features
- Connects to Tor network
- Scans .onion sites for breach keywords
- Filters dead/active links
- Saves output in CSV format

## Technologies Used
- Python, BeautifulSoup, Requests
- Tor proxy (9050)
- Telethon (Telegram crawler)

## Usage
1. Add `.onion` links to `sources.list`
2. Run `main.py`
3. Check `results.csv` for output
