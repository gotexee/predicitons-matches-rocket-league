import requests
import playwright
from playwright.sync_api import sync_playwright, Playwright

def run(playwright: Playwright):
    chromium = playwright.chromium # or "firefox" or "webkit".
    browser = chromium.launch(headless=False) # on désactive car cfl détecte le caché
    page = browser.new_page()
    resposne = page.goto("https://rocketleague.tracker.network/rocket-league/profile/epic/mawkzy/overview")
    print(resposne)
    
with sync_playwright() as playwright:
    run(playwright)



"""
output = 403
Si on trace le chemin :
pc envoie la requete ca sort de mon routeur contenant ma requete et mon ip publique
ca contacte l'fai de mon wifi, et les serveurs du fai redirige ma requete vers les serveur de l'url demandé
Problème =  reverse oxy mondial CLOUFARE bloque ma requète
Cloudflare utilise le DEFI JAVASCRIPT pour vérifier si bot ou vrai utilsiateur

DEFI JAVSCRIPT :
    - il recoit notre requete et envoie une petite page html avec du code javascript
    - code qui demande au navigateur de résoudre un calcul mathématique, ou bien qui chercher des indications d'un navigatuer
    - nous on n'a pas de navigateur donc pas de réponse de calcul et donc cloudflare refuse l'accés.
    
    
SOLUTION :
j'installe playwright ainsi que chromium"""

