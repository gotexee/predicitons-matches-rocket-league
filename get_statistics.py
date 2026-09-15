import json
from playwright.sync_api import sync_playwright, Playwright


def stats(playwright: Playwright):
    url = "https://api.tracker.gg/api/v2/rocket-league/standard/profile/epic/zenrll?"
    chromium = playwright.chromium  # or "firefox" or "webkit".
    browser = chromium.launch(headless=False)  # on désactive car cf détecte le headless
    page = browser.new_page()
    with open("cookies.json", "r", encoding="utf-8") as fichier:
            # mode "r" = lecture seule (pas d'écrasement comme "w"). fichier = objet qui représente le fichier ouvert.
            cookies = fichier.read()
            # .read() prend TOUT le fichier et en fait une seule grosse chaîne de texte brute -> pas encore exploitable comme des vraies données Python
    b = json.loads(cookies)
        # cookies.json commence par un "[" donc b est une LISTE, pas un dict.
        # chaque élément de cette liste est lui un dict (un cookie : {"name": ..., "value": ..., "domain": ...})
    cookie_dict = {}          # on part d'un dictionnaire vide
    for c in b:                # on parcourt chaque élément de la liste b
        cookie_dict[c["name"]] = c["value"]   # on ajoute une paire clé/valeur à chaque tour
    headers = {
        "Origin": "https://rocketleague.tracker.network",
        "Referer": "https://rocketleague.tracker.network/",
        "Accept": "application/json, text/plain, */*",
        }
    page.goto(url, cookies=cookie_dict, headers=headers)

with sync_playwright() as playwright: # démarre le moteur playwright en tant que playwright qui représente que playwright tourne
    stats(playwright) # on lance la focntion avec comme parametre notre objet playwright
    # with sert a ce que le fichier se ferme et que le lancement s'arrete quand plus d'instructions
