from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Eccomi Display TV")

app.mount("/static", StaticFiles(directory="static"), name="static")

SCREENS = {
    "maximo": {
        "title": "Maximo TV",
        "video": "/static/videos/orizzontale.MP4",
    },
    "civitavecchia": {
        "title": "Civitavecchia TV",
        "video": "/static/videos/verticale.MP4",
    },
    "grosseto": {
        "title": "Grosseto TV",
        "video": "/static/videos/orizzontale.MP4",
    },
    "laquila": {
        "title": "L'Aquila TV",
        "video": "/static/videos/orizzontale.MP4",
    },
}


def render_page(title: str, video_url: str):
    return f"""
<!DOCTYPE html>
<html lang="it">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="refresh" content="600">
  <title>{title}</title>

  <style>
    html, body {{
      margin: 0;
      padding: 0;
      width: 100%;
      height: 100%;
      background: #000;
      overflow: hidden;
    }}

    video {{
      width: 100vw;
      height: 100vh;
      object-fit: cover;
      background: #000;
    }}
  </style>
</head>

<body>
  <video autoplay muted loop playsinline preload="auto">
    <source src="{video_url}?v=1" type="video/mp4">
  </video>
</body>
</html>
"""


@app.get("/", response_class=HTMLResponse)
def home():
    return """
<!DOCTYPE html>
<html lang="it">
<head>
  <meta charset="UTF-8">
  <title>Eccomi Display TV</title>
</head>
<body>
  <h1>Eccomi Display TV attivo</h1>
  <ul>
    <li><a href="/maximo">Maximo TV Orizzontale</a></li>
    <li><a href="/civitavecchia">Civitavecchia TV Verticale</a></li>
    <li><a href="/grosseto">Grosseto TV Orizzontale</a></li>
    <li><a href="/laquila">L'Aquila TV Orizzontale</a></li>
  </ul>
</body>
</html>
"""


@app.get("/health")
def health():
    return {"ok": True, "service": "eccomi-display-tv"}


@app.get("/{screen_name}", response_class=HTMLResponse)
def display(screen_name: str):
    screen = SCREENS.get(screen_name)

    if not screen:
        return "<h1>Schermo non trovato</h1>"

    return render_page(screen["title"], screen["video"])
