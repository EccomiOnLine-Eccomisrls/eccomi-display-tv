from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Eccomi Display TV")

# Link Dropbox RAW
ORIZZONTALE = "https://www.dropbox.com/scl/fi/o2zgr5mldx2zv2x34fosx/VIDEO-2026-07-10-15-34-11.mp4?rlkey=fnxo788iwql9a0177ajpd39n1&st=yyao12pz&raw=1"

VERTICALE = "https://www.dropbox.com/scl/fi/o2zgr5mldx2zv2x34fosx/VIDEO-2026-07-10-15-34-11.mp4?rlkey=fnxo788iwql9a0177ajpd39n1&st=yyao12pz&raw=1"


def render_auto_page():
    return f"""
<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv="refresh" content="86400">
<title>Eccomi Display TV</title>

<style>
html, body {{
  margin: 0;
  padding: 0;
  background: #000;
  overflow: hidden;
  width: 100%;
  height: 100%;
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
<video id="player" autoplay muted loop playsinline preload="auto"></video>

<script>
const ORIZZONTALE = "{ORIZZONTALE}";
const VERTICALE = "{VERTICALE}";
const player = document.getElementById("player");

function scegliVideo() {{
  const isVerticale = window.innerHeight > window.innerWidth;
  const videoScelto = isVerticale ? VERTICALE : ORIZZONTALE;

  if (player.src !== videoScelto) {{
    player.src = videoScelto;
    player.load();
    player.play().catch(() => {{}});
  }}
}}

scegliVideo();

window.addEventListener("resize", scegliVideo);
window.addEventListener("orientationchange", scegliVideo);
</script>
</body>
</html>
"""


@app.get("/", response_class=HTMLResponse)
def home():
    return """
<h1>Eccomi Display TV attivo</h1>
<p><a href="/oe">Apri Display Unico /oe</a></p>
<p><a href="/health">Health Check</a></p>
"""


@app.get("/oe", response_class=HTMLResponse)
def oe():
    return render_auto_page()


@app.get("/health")
def health():
    return {"ok": True, "service": "eccomi-display-tv"}


# Compatibilità con i vecchi link già usati sui TV
@app.get("/{screen}", response_class=HTMLResponse)
def screen(screen: str):
    return render_auto_page()
