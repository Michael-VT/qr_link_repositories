# QR Link Repositories

Um script em Python que gera uma galeria HTML autossuficiente dos seus repositórios GitHub com códigos QR e cards de visualização OpenGraph.

[English](README.md) | [Русский](README.ru.md) | [Українська](README.uk.md) | [Deutsch](README.de.md) | [Français](README.fr.md)

## O Que o Script Faz

1. Obtém os repositórios públicos de um utilizador GitHub através da REST API (paginado, ordenado por data de atualização).
2. Gera um código QR para o URL de cada repositório e incorpora-o como PNG base64.
3. Obtém uma imagem de pré-visualização OpenGraph para cada repositório (via `opengraph.githubassets.com`).
4. Cria uma página HTML com tema escuro e grelha de cards responsiva. **Todos os dados estão incorporados no ficheiro — sem recursos externos ou servidores necessários.**
5. Guarda o resultado em `repos_gallery.html`.

Repositórios arquivados e desativados são excluídos automaticamente.

## Requisitos

- Python 3.7+
- `requests`
- `qrcode`
- `Pillow` (PIL)

Instalar dependências:

```bash
pip install requests qrcode Pillow
```

## Configuração

Edite as constantes no início do ficheiro `scriptn1.py`:

| Constante | Padrão | Descrição |
|---|---|---|
| `USERNAME` | `"Michael-VT"` | Nome de utilizador GitHub |
| `OUTPUT_HTML` | `"repos_gallery.html"` | Nome do ficheiro de saída |
| `MAX_REPOS` | `50` | Número máximo de repositórios |
| `QR_SIZE` | `160` | Tamanho do código QR em pixels |
| `IMG_SIZE` | `110` | Tamanho da miniatura de pré-visualização |

## Utilização

```bash
python scriptn1.py
```

O script irá:
1. Obter os repositórios do GitHub.
2. Gerar códigos QR e obter pré-visualizações.
3. Guardar `repos_gallery.html` no diretório atual.

Abra `repos_gallery.html` em qualquer navegador para ver a galeria.

## Como Adicionar um Link a Partir de Outros Projetos

Para referenciar a galeria a partir do README de outro repositório:

### Markdown

```markdown
[Galeria dos Meus Repositórios](https://htmlpreview.github.io/?https://github.com/Michael-VT/qr_link_repositories/main/repos_gallery.html)
```

Se utilizar GitHub Pages para este repositório:

```markdown
[Galeria dos Meus Repositórios](https://michael-vt.github.io/qr_link_repositories/repos_gallery.html)
```

### HTML

```html
<a href="https://htmlpreview.github.io/?https://github.com/Michael-VT/qr_link_repositories/main/repos_gallery.html">
    Galeria dos Meus Repositórios
</a>
```

### Dica de Código QR

Também pode gerar um código QR apontando para o URL do `repos_gallery.html` alojado e incorporá-lo noutros projetos, documentos impressos ou apresentações.

## Pré-visualização do Resultado

A página gerada é uma grelha responsiva com tema escuro. Cada card contém:
- Um código QR com link para o repositório
- Nome do repositório (link clicável)
- Descrição
- Imagem de pré-visualização OpenGraph (quando disponível)
- Contagem de estrelas e linguagem principal

## Licença

Este projeto é fornecido como está para uso pessoal.
