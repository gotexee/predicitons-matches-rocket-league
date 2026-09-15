import json
import get_statistics

from playwright.sync_api import sync_playwright, Playwright


def run(playwright: Playwright):
    chromium = playwright.chromium  # or "firefox" or "webkit".
    browser = chromium.launch(headless=False)  # on désactive car cf détecte le headless
    page = browser.new_page()
    page.goto("https://rocketleague.tracker.network/rocket-league/")
    cookies = page.context.cookies() # récupérer les cookies en format json

    with open("cookies.json", "w") as f: # w permet d'ecraser le fichier à la fermeture, si a par exemple alors a cahque ouverture du fichier les cookies d'ajouteraient ouverture apres ouverture
        json.dump(cookies, f, indent=2) # on ouvre fichier cookies.json qui est vide et on met dedans le contenu de cookies avec une certaine indentation
    print(f"{len(cookies)} cookies sauvegardés dans cookies.json") # regarde le dictionnaire et le nombre de cookies
    
    get_statistics.statistics()
    browser.close()

with sync_playwright() as playwright: # démarre le moteur playwright en tant que playwright qui représente que playwright tourne
    run(playwright) # on lance la focntion avec comme parametre notre objet playwright
    # with sert a ce que le fichier se ferme et que le lancement s'arrete quand plus d'instructions
