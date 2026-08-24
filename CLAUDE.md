@AGENTS.md

# yuki-atelier プロジェクトの作業ルール

## サイトの概要

- 学習用の静的サイト「yuki's atelier」。ジャンルごとに `index.html` から各ディレクトリへ遷移する。
- 共通 CSS は `css/style.css`。フォントは Google Fonts CDN 経由のみ（ttf/otf を直接置かない）。
- アプリ／キャラクターアイコン（マスコット = `atelier-icon.png`、branch/team の概念アイコン）は `assets/icons/*.png` を使用する。
- 技術ジャンルのロゴ（Git など）は **Devicon CDN** (`cdn.jsdelivr.net/gh/devicons/devicon@v2.16.0/icons/<tech>/<tech>-original.svg`) の公式ロゴを `<img>` で読み込む。
- **絵文字は使わない**。UI アイコンは `assets/icons/ui-icons.svg`（SVG スプライト、`<symbol id="ic-…">`）に追加し、`<svg class="ui-icon"><use href="…#ic-…"/></svg>` で参照する。JS から差し込む場合は `git/js/app.js` の `svgIcon(name, extraClass)` ヘルパー経由とする。
