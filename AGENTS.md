# yuki-atelier project instructions

## 役割と共通利用

- `yuki-atelier`は、学習担当が学習済み範囲の復習問題を提供する場所を主用途とする。
- assistant／tutor／PMは、共通運用規則の許可範囲で読み取り・編集・テスト・ビルド・Git差分確認を行える。
- commit、push、公開、削除、破壊的変更は、ユーザーの明示的な指示がある時だけ行う。
- 同じ内容をObsidian、Vault、Memoryへ複製せず、用途ごとのSSOTを守る。

## 学習SSOT

- 詳細知識、教科書、学習計画、進捗、間違い、学習ログの唯一のSSOTは`/mnt/s/hermes/obsidian-study/CCNA/`とする。
- `yuki-atelier/ccna`は、学習済み範囲を選択式で復習する派生問題集であり、教科書や進捗管理の正本にしない。
- `yuki-atelier/ccna`からObsidianへ逆同期しない。Obsidianの私的な記録を公開サイトへそのまま転載しない。
- Notionは廃止済みのarchiveであり、現行の学習SSOTや同期先として使わない。

## 変更時の検証

- 今回変更したpathだけを検証・stageし、`git add -A`や`git add .`で無関係な差分を巻き込まない。
- 既存のGit、CCNA、asset、デザイン機能を変更対象外として保持する。
- 完了時は、focused test、全体test、`git diff --check`、exact path集合、local／remote状態を分けて報告する。
