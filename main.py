from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Eccomi Display TV")

ORIZZONTALE = "https://drive.google.com/uc?export=download&id=1CSSua0TF2AL-hWpC07fjNTxUzZMN9rKR"
VERTICALE = "https://drive.google.com/uc?export=download&id=1rEeVmQ1-q4TXTVVP-6opjmAA4nFquqcV"

SCREENS = {
    "maximo": {"title": "Maximo TV", "video": ORIZZONTALE},
    "civitavecchia": {"title": "Civitavecchia TV", "video": VERTICALE},
    "grosseto": {"title": "Grosseto TV", "video": ORIZZONTALE},
    "laquila": {"title": "L'Aquila TV", "video": ORIZZONTALE},
}

def render_page(title, video_url):
    return f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta http-equiv="refresh" content="600">
<title>{title}</title>
<style>
html, body {{
  margin: 0;
  background: black;
  overflow: hidden;
}}
video {{
  width: 100vw;
  height: 100vh;
  object-fit: cover;
}}
</style>
</head>
<body>
<video autoplay muted loop playsinline>
  <source src="{video_url}" type="video/mp4">
</video>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
def home():
    return """
<h1>Eccomi Display TV attivo</h1>
<ul>
<li><a href="/maximo">Maximo</a></li>
<li><a href="/civitavecchia">Civitavecchia</a></li>
<li><a href="/grosseto">Grosseto</a></li>
<li><a href="/laquila">L'Aquila</a></li>
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
