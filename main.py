from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Eccomi Display TV")

# I tuoi link Dropbox (da aggiornare ogni 10gg)
ORIZZONTALE = "https://www.dropbox.com/scl/fi/n2lbb2ky42dist5ojqhbl/orizzontale.MP4?rlkey=ft0dtz52235og6vonwrh3k1i7&st=o0qln1cq&raw=1"

VERTICALE = "https://www.dropbox.com/scl/fi/rdsv86zlt740xebafj8w7/verticale.MP4?rlkey=e2lo5jqiksvrp2t24oye8sezn&st=guipalz1&raw=1"

# --- AGGIUNGI O RIMUOVI LE TV QUI ---
SCREENS = {
    "maximo": {"title": "Maximo TV", "video": ORIZZONTALE},
    "civitavecchia": {"title": "Civitavecchia TV", "video": VERTICALE},
    "grosseto": {"title": "Grosseto TV", "video": ORIZZONTALE},
    "laquila": {"title": "L'Aquila TV", "video": ORIZZONTALE},
    "roma": {"title": "Roma TV", "video": ORIZZONTALE},      # Esempio nuova TV
    "milano": {"title": "Milano TV", "video": VERTICALE},     # Esempio nuova TV
}

def render_page(title, video_url):
    return f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta http-equiv="refresh" content="86400">
<title>{title}</title>
<style>
html, body {{
  margin: 0;
  background: black;
  overflow: hidden;
  width: 100%;
  height: 100%;
}}
video {{
  width: 100vw;
  height: 100vh;
  object-fit: cover;
  background: black;
}}
</style>
</head>
<body>
<video autoplay muted loop playsinline preload="auto">
  <source src="{video_url}" type="video/mp4">
</video>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
def home():
    # Questa riga genera la lista HTML automaticamente leggendo da SCREENS
    lista_link = "".join([f'<li><a href="/{chiave}">{dati["title"]}</a></li>' for chiave, dati in SCREENS.items()])
    
    return f"""
    <h1>Eccomi Display TV attivo</h1>
    <ul>
        {lista_link}
    </ul>
    """

@app.get("/health")
def health():
    return {"ok": True}

@app.get("/{screen}", response_class=HTMLResponse)
def screen(screen: str):
    data = SCREENS.get(screen)
    if not data:
        return "<h1>Schermo non trovato</h1>"
    return render_page(data["title"], data["video"])
