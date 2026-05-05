from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Eccomi Display TV")

SCREENS = {
    "maximo": {
        "title": "Maximo TV",
        "video": "https://api.onedrive.com/v1.0/shares/u!aHR0cHM6Ly8xZHJ2Lm1zL3YvYy9lZDM2Y2UxMjA4NDkzNzUwL0lRRDN1UjNEVTlZOVFKc3lKOUIkaiV0NlF3QWUwdkRET1FqakhHckp5ZkdQU203TWFrP2U9Y1pmdm5k/root/content",
    },
    "civitavecchia": {
        "title": "Civitavecchia TV",
        "video": "https://api.onedrive.com/v1.0/shares/u!aHR0cHM6Ly8xZHJ2Lm1zL3YvYy9lZDM2Y2UxMjA4NDkzNzUwL0lRQ0pOZTNJT1VtaVFKS1B2cTdnUjFTR0FUNkswZ2c1VTZiWjZIcWVVUWhCUF4wP2U9dDMwOVFH/root/content",
    },
    "grosseto": {
        "title": "Grosseto TV",
        "video": "https://api.onedrive.com/v1.0/shares/u!aHR0cHM6Ly8xZHJ2Lm1zL3YvYy9lZDM2Y2UxMjA4NDkzNzUwL0lRRDN1UjNEVTlZOVFKc3lKOUIkaiV0NlF3QWUwdkRET1FqakhHckp5ZkdQU203TWFrP2U9Y1pmdm5k/root/content",
    },
    "laquila": {
        "title": "L'Aquila TV",
        "video": "https://api.onedrive.com/v1.0/shares/u!aHR0cHM6Ly8xZHJ2Lm1zL3YvYy9lZDM2Y2UxMjA4NDkzNzUwL0lRRDN1UjNEVTlZOVFKc3lKOUIkaiV0NlF3QWUwdkRET1FqakhHckp5ZkdQU203TWFrP2U9Y1pmdm5k/root/content",
    },
}

def render_page(title, video_url):
    return f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta http-equiv="refresh" content="600">
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

@app.get("/{screen}", response_class=HTMLResponse)
def screen(screen: str):
    data = SCREENS.get(screen)
    if not data:
        return "<h1>Schermo non trovato</h1>"
    return render_page(data["title"], data["video"])
