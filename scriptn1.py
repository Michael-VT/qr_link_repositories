import requests
import qrcode
from PIL import Image
import os
import time
import base64
from io import BytesIO

# ================= НАСТРОЙКИ =================
USERNAME = "Michael-VT"          # ← Измени, если нужно
OUTPUT_HTML = "repos_gallery.html"
MAX_REPOS = 50
QR_SIZE = 160                    # чуть уменьшил, чтобы лучше влезало
IMG_SIZE = 110
# ============================================

def get_user_repos(username):
    url = f"https://api.github.com/users/{username}/repos"
    params = {"per_page": 100, "sort": "updated", "direction": "desc"}
    headers = {"Accept": "application/vnd.github.v3+json"}
    
    repos = []
    page = 1
    while len(repos) < MAX_REPOS:
        params["page"] = page
        resp = requests.get(url, params=params, headers=headers)
        if resp.status_code != 200:
            print("Ошибка API:", resp.status_code)
            break
        data = resp.json()
        if not data:
            break
        repos.extend(data)
        page += 1
        time.sleep(0.7)
    return repos[:MAX_REPOS]


def create_qr_base64(url, size=QR_SIZE):
    """Создаём QR и сразу превращаем в base64"""
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, 
                       box_size=10, border=2)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img = img.resize((size, size))
    
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode('utf-8')


def get_repo_preview(repo):
    try:
        preview_url = f"https://opengraph.githubassets.com/1/{repo['full_name']}"
        resp = requests.get(preview_url, timeout=6)
        if resp.status_code == 200:
            img = Image.open(BytesIO(resp.content))
            img.thumbnail((IMG_SIZE, IMG_SIZE))
            buffered = BytesIO()
            img.save(buffered, format="PNG")
            return base64.b64encode(buffered.getvalue()).decode('utf-8')
    except:
        pass
    return None


def generate_html(repos):
    html = f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Репозитории {USERNAME}</title>
    <style>
        body {{ font-family: system-ui, sans-serif; background: #0d1117; color: #c9d1d9; margin: 0; padding: 20px; }}
        .gallery {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 20px; }}
        .card {{
            background: #161b22;
            border: 1px solid #30363d;
            border-radius: 12px;
            padding: 16px;
            transition: all 0.2s;
        }}
        .card:hover {{ transform: translateY(-4px); border-color: #58a6ff; }}
        .header {{ display: flex; gap: 16px; align-items: flex-start; margin-bottom: 12px; }}
        .qr {{ border: 1px solid #30363d; border-radius: 8px; }}
        .info {{ flex: 1; }}
        .title {{ margin: 0 0 6px 0; font-size: 1.1em; }}
        .title a {{ color: #58a6ff; text-decoration: none; }}
        .title a:hover {{ text-decoration: underline; }}
        .desc {{ font-size: 0.95em; line-height: 1.4; color: #8b949e; margin: 0; }}
        .footer {{ margin-top: 12px; font-size: 0.8em; color: #6e7681; }}
    </style>
</head>
<body>
    <h1>Репозитории {USERNAME}</h1>
    <div class="gallery">
"""

    count = 0
    for repo in repos:
        if repo.get('archived') or repo.get('disabled'):
            continue
            
        name = repo['name']
        url = repo['html_url']
        desc = (repo.get('description') or "Нет описания")[:170]
        if len(repo.get('description') or "") > 170:
            desc += "..."

        qr_base64 = create_qr_base64(url)
        preview_base64 = get_repo_preview(repo)

        preview_html = ""
        if preview_base64:
            preview_html = f'<img src="data:image/png;base64,{preview_base64}" style="width:{IMG_SIZE}px;height:auto;border-radius:6px;margin-top:8px;" alt="preview">'

        card = f"""
        <div class="card">
            <div class="header">
                <img src="data:image/png;base64,{qr_base64}" class="qr" width="{QR_SIZE}" height="{QR_SIZE}" alt="QR">
                <div class="info">
                    <h3 class="title"><a href="{url}" target="_blank">{name}</a></h3>
                    <p class="desc">{desc}</p>
                </div>
            </div>
            {preview_html}
            <div class="footer">
                ⭐ {repo.get('stargazers_count', 0)} • {repo.get('language') or '—'}
            </div>
        </div>
"""
        html += card
        count += 1

    html += """
    </div>
</body>
</html>
"""

    with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
        f.write(html)
    
    print(f"✅ Готово! Обработано {count} репозиториев → {OUTPUT_HTML}")


if __name__ == "__main__":
    print("Получаем список репозиториев...")
    repos = get_user_repos(USERNAME)
    print(f"Найдено репозиториев: {len(repos)}")
    generate_html(repos)
