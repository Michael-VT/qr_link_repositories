# QR Link Repositories

A Python script that generates a self-contained HTML gallery of your GitHub repositories with QR codes and OpenGraph preview cards.

[Русский](README.ru.md) | [Українська](README.uk.md) | [Português](README.pt.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

## What It Does

1. Fetches public repositories for a given GitHub user via the GitHub REST API (paginated, sorted by last updated).
2. Generates a QR code for each repository URL and embeds it as a base64 PNG.
3. Fetches an OpenGraph social preview image for each repository (via `opengraph.githubassets.com`).
4. Renders a dark-themed responsive card grid HTML page with all data inlined — **no external assets, no server required**.
5. Writes the result to `repos_gallery.html`.

Archived and disabled repositories are excluded automatically.

## Requirements

- Python 3.7+
- `requests`
- `qrcode`
- `Pillow` (PIL)

Install dependencies:

```bash
pip install requests qrcode Pillow
```

## Configuration

Edit the constants at the top of `scriptn1.py`:

| Constant | Default | Description |
|---|---|---|
| `USERNAME` | `"Michael-VT"` | GitHub username to fetch repos for |
| `OUTPUT_HTML` | `"repos_gallery.html"` | Output file name |
| `MAX_REPOS` | `50` | Maximum number of repositories to process |
| `QR_SIZE` | `160` | QR code image size in pixels |
| `IMG_SIZE` | `110` | Preview thumbnail size in pixels |

## Usage

```bash
python scriptn1.py
```

The script will:
1. Fetch repositories from GitHub.
2. Generate QR codes and fetch previews.
3. Write `repos_gallery.html` to the current directory.

Open `repos_gallery.html` in any browser to view the gallery.

## Linking from Other Projects

To add a link to the gallery from your other repository README files:

### Markdown

```markdown
[My Repositories Gallery](https://htmlpreview.github.io/?https://github.com/Michael-VT/qr_link_repositories/main/repos_gallery.html)
```

Or, if you use GitHub Pages for this repository:

```markdown
[My Repositories Gallery](https://michael-vt.github.io/qr_link_repositories/repos_gallery.html)
```

### HTML

```html
<a href="https://htmlpreview.github.io/?https://github.com/Michael-VT/qr_link_repositories/main/repos_gallery.html">
    My Repositories Gallery
</a>
```

### QR Code Tip

You can also generate a QR code pointing to the hosted `repos_gallery.html` URL and embed it in other projects, physical documents, or presentations.

## Output Preview

The generated page is a responsive dark-themed grid. Each card contains:
- A QR code linking to the repository
- Repository name (clickable link)
- Description
- OpenGraph preview image (when available)
- Star count and primary language

## License

This project is provided as-is for personal use.
