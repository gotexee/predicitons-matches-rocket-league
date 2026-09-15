import json
from playwright.sync_api import sync_playwright, Playwright


def stats(playwright: Playwright):
    url = "https://api.tracker.gg/api/v2/rocket-league/standard/profile/epic/zenrll?"
    chromium = playwright.chromium  # or "firefox" or "webkit".
    browser = chromium.launch(headless=False)  # on désactive car cf détecte le headless
    with open("cookies.json", "r", encoding="utf-8") as fichier: 
        b = json.load(fichier)
            # mode "r" = lecture seule (pas d'écrasement comme "w"). fichier = objet qui représente le fichier ouvert.
            # b est une lsite de dicts
    headers = {
        "Origin": "https://rocketleague.tracker.network",
        "Referer": "https://rocketleague.tracker.network/",
        "Accept": "application/json, text/plain, */*",
        }
    context = browser.new_context(extra_http_headers=headers) # creation d'un contexte de navigation, on y met les headers
    cookies = []
    for c in b: # on parcourt la liste de dicts b et on ajoute les dictionnaires de cookies dans la liste cookies
        cookies.append({
            "name": c["name"],
            "value": c["value"],
            "domain": c["domain"],
            "path": c["path"],
            })
    context.add_cookies(cookies) # on ajoute cookies dans le contxt
    page = context.new_page()
    response = page.goto(url)
    print(response.json())