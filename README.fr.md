# QR Link Repositories

Un script Python qui génère une galerie HTML autonome de vos dépôts GitHub avec des codes QR et des cartes de prévisualisation OpenGraph.

[English](README.md) | [Русский](README.ru.md) | [Українська](README.uk.md) | [Português](README.pt.md) | [Deutsch](README.de.md)

## Ce que fait le script

1. Récupère les dépôts publics d'un utilisateur GitHub via l'API REST (paginé, trié par date de mise à jour).
2. Génère un code QR pour l'URL de chaque dépôt et l'intègre en tant que PNG base64.
3. Télécharge une image de prévisualisation OpenGraph pour chaque dépôt (via `opengraph.githubassets.com`).
4. Crée une page HTML avec un thème sombre et une grille de cartes responsive. **Toutes les données sont intégrées dans le fichier — aucune ressource externe ni serveur requis.**
5. Écrit le résultat dans `repos_gallery.html`.

Les dépôts archivés et désactivés sont automatiquement exclus.

## Prérequis

- Python 3.7+
- `requests`
- `qrcode`
- `Pillow` (PIL)

Installer les dépendances :

```bash
pip install requests qrcode Pillow
```

## Configuration

Modifiez les constantes au début du fichier `scriptn1.py` :

| Constante | Par défaut | Description |
|---|---|---|
| `USERNAME` | `"Michael-VT"` | Nom d'utilisateur GitHub |
| `OUTPUT_HTML` | `"repos_gallery.html"` | Nom du fichier de sortie |
| `MAX_REPOS` | `50` | Nombre maximum de dépôts |
| `QR_SIZE` | `160` | Taille du code QR en pixels |
| `IMG_SIZE` | `110` | Taille de la vignette de prévisualisation |

## Utilisation

```bash
python scriptn1.py
```

Le script :
1. Récupérera les dépôts depuis GitHub.
2. Générera les codes QR et téléchargera les prévisualisations.
3. Écrira `repos_gallery.html` dans le répertoire courant.

Ouvrez `repos_gallery.html` dans n'importe quel navigateur pour visualiser la galerie.

## Ajouter un lien depuis d'autres projets

Pour référencer la galerie depuis le README d'un autre dépôt :

### Markdown

```markdown
[Galerie de mes dépôts](https://htmlpreview.github.io/?https://github.com/Michael-VT/qr_link_repositories/main/repos_gallery.html)
```

Si vous utilisez GitHub Pages pour ce dépôt :

```markdown
[Galerie de mes dépôts](https://michael-vt.github.io/qr_link_repositories/repos_gallery.html)
```

### HTML

```html
<a href="https://htmlpreview.github.io/?https://github.com/Michael-VT/qr_link_repositories/main/repos_gallery.html">
    Galerie de mes dépôts
</a>
```

### Astuce QR Code

Vous pouvez également générer un code QR pointant vers l'URL du fichier `repos_gallery.html` hébergé et l'intégrer dans d'autres projets, documents imprimés ou présentations.

## Aperçu du résultat

La page générée est une grille responsive au thème sombre. Chaque carte contient :
- Un code QR avec un lien vers le dépôt
- Le nom du dépôt (lien cliquable)
- La description
- L'image de prévisualisation OpenGraph (si disponible)
- Le nombre d'étoiles et le langage principal

## Licence

Ce projet est fourni tel quel pour un usage personnel.
