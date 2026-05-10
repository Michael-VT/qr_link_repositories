# QR Link Repositories

Ein Python-Skript, das eine eigenständige HTML-Galerie Ihrer GitHub-Repositories mit QR-Codes und OpenGraph-Vorschaukarten erstellt.

[English](README.md) | [Русский](README.ru.md) | [Українська](README.uk.md) | [Português](README.pt.md) | [Français](README.fr.md)

## Was das Skript macht

1. Ruft die öffentlichen Repositories eines GitHub-Benutzers über die REST-API ab (seitenweise, sortiert nach Aktualisierungsdatum).
2. Erzeugt einen QR-Code für die URL jedes Repositories und bettet ihn als Base64-PNG ein.
3. Lädt ein OpenGraph-Vorschaubild für jedes Repository herunter (über `opengraph.githubassets.com`).
4. Erstellt eine HTML-Seite mit dunklem Theme und responsivem Kartenraster. **Alle Daten sind in die Datei eingebettet — keine externen Ressourcen oder Server erforderlich.**
5. Schreibt das Ergebnis in `repos_gallery.html`.

Archivierte und deaktivierte Repositories werden automatisch übersprungen.

## Voraussetzungen

- Python 3.7+
- `requests`
- `qrcode`
- `Pillow` (PIL)

Abhängigkeiten installieren:

```bash
pip install requests qrcode Pillow
```

## Konfiguration

Bearbeiten Sie die Konstanten am Anfang von `scriptn1.py`:

| Konstante | Standardwert | Beschreibung |
|---|---|---|
| `USERNAME` | `"Michael-VT"` | GitHub-Benutzername |
| `OUTPUT_HTML` | `"repos_gallery.html"` | Name der Ausgabedatei |
| `MAX_REPOS` | `50` | Maximale Anzahl der Repositories |
| `QR_SIZE` | `160` | QR-Code-Größe in Pixeln |
| `IMG_SIZE` | `110` | Vorschaubild-Größe in Pixeln |

## Ausführung

```bash
python scriptn1.py
```

Das Skript:
1. Ruft Repositories von GitHub ab.
2. Generiert QR-Codes und lädt Vorschaubilder herunter.
3. Schreibt `repos_gallery.html` in das aktuelle Verzeichnis.

Öffnen Sie `repos_gallery.html` in einem beliebigen Browser, um die Galerie anzuzeigen.

## Verlinkung aus anderen Projekten

So verlinken Sie die Galerie aus der README eines anderen Repositories:

### Markdown

```markdown
[Meine Repository-Galerie](https://htmlpreview.github.io/?https://github.com/Michael-VT/qr_link_repositories/main/repos_gallery.html)
```

Wenn Sie GitHub Pages für dieses Repository verwenden:

```markdown
[Meine Repository-Galerie](https://michael-vt.github.io/qr_link_repositories/repos_gallery.html)
```

### HTML

```html
<a href="https://htmlpreview.github.io/?https://github.com/Michael-VT/qr_link_repositories/main/repos_gallery.html">
    Meine Repository-Galerie
</a>
```

### QR-Code-Tipp

Sie können auch einen QR-Code generieren, der auf die URL der gehosteten `repos_gallery.html` verweist, und ihn in andere Projekte, gedruckte Dokumente oder Präsentationen einbetten.

## Vorschau des Ergebnisses

Die generierte Seite ist ein responsives Raster mit dunklem Theme. Jede Karte enthält:
- Einen QR-Code mit Link zum Repository
- Repository-Namen (klickbarer Link)
- Beschreibung
- OpenGraph-Vorschaubild (falls verfügbar)
- Sternebewertung und Hauptsprache

## Lizenz

Dieses Projekt wird wie besehen zur persönlichen Nutzung bereitgestellt.
