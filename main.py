from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Eccomi Display TV")

ORIZZONTALE = "https://1drv.ms/v/c/ed36ce1208493750/IQD3uR3DU9Y9QJsyJ9BDjyQwAe0VDOQjjXGrJyfGPPm7Mak?e=ruE47B"
VERTICALE = "https://1drv.ms/v/c/ed36ce1208493750/IQCJNe3IOUmiQJKPvq7gR1SGAT6K0gg5U6bZ6HqeUQrBPN0?e=t309QG"

SCREENS = {
    "maximo": {
        "title": "Maximo TV Orizzontale",
        "video": ORIZZONTALE,
    },
    "civitavecchia": {
        "title": "Civitavecchia TV Verticale",
        "video": VERTICALE,
    },
    "grosseto": {
        "title": "Grosseto TV Orizzontale",
        "video": ORIZZONTALE,
    },
    "laquila": {
        "title": "L'Aquila TV Orizzontale",
        "video": ORIZZONTALE,
    },
}


def render_page(title: str, video_url: str):
    return f"""
<!DOCTYPE html>
<html lang="it">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="refresh" content="3600">
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

    iframe {{
      width: 100vw;
      height: 100vh;
      border: 0;
      background: #000;
    }}
  </style>
</head>

<body>
  <iframe src="{video_url}" allow="autoplay; fullscreen"></iframe>
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
