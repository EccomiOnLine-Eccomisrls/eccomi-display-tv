from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Eccomi Display TV")

ORIZZONTALE = "https://www.dropbox.com/scl/fi/n2lbb2ky42dist5ojqhbl/orizzontale.MP4?rlkey=ft0dtz52235og6vonwrh3k1i7&st=o0qln1cq&raw=1"

VERTICALE = "https://www.dropbox.com/scl/fi/rdsv86zlt740xebafj8w7/verticale.MP4?rlkey=e2lo5jqiksvrp2t24oye8sezn&st=guipalz1&raw=1"

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
