import os

folders = [
    "lyrics_app/templates",
    "lyrics_app/static",
    "lyrics_app/auth",
    "lyrics_app/routes"
]

files = {
    "lyrics_app/app.py": "",
    "lyrics_app/config.py": "",
    "lyrics_app/models.py": "",
    "lyrics_app/templates/base.html": "",
    "lyrics_app/templates/home.html": "",
    "lyrics_app/templates/login.html": "",
    "lyrics_app/templates/register.html": "",
    "lyrics_app/templates/song.html": "",
    "lyrics_app/templates/favourites.html": "",
    "lyrics_app/auth/__init__.py": "",
    "lyrics_app/auth/routes.py": "",
    "lyrics_app/routes/__init__.py": "",
    "lyrics_app/routes/main.py": "",
}

for folder in folders:
    os.makedirs(folder, exist_ok=True)

for path, content in files.items():
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print("✅ Project structure created successfully!")
