from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Eccomi Display TV")

app.mount("/static", StaticFiles(directory="static"), name="static")

SCREENS = {
    "maximo": "/static/videos/orizzontale.mp4",
    "civitavecchia": "/static/videos/verticale.mp4",
    "grosseto": "/static/videos/orizzontale.mp4",
    "laquila": "/static/videos/orizzontale.mp4",
}

def page(video_url):
    return f"""
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta http-equiv="refresh" content="600">
  <style>
    html, body {{
      margin: 0;
      background: #000;
      overflow: hidden;
      width: 100%;
      height: 100%;
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
    <source src="{video_url}?v=1" type="video/mp4">
  </video>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <h1>Eccomi Display TV</h1>
    <p><a href="/maximo">Maximo</a></p>
    <p><a href="/civitavecchia">Civitavecchia</a></p>
    <p><a href="/grosseto">Grosseto</a></p>
    <p><a href="/laquila">L'Aquila</a></p>
    """

@app.get("/{screen}", response_class=HTMLResponse)
def display(screen: str):
    video = SCREENS.get(screen)
    if not video:
        return "<h1>Schermo non trovato</h1>"
    return page(video)

@app.get("/health")
def health():
    return {"ok": True}
