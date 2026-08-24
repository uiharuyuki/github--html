import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class PublicExplanationsDecommissionContractTests(unittest.TestCase):
    def test_public_explanation_workflow_is_removed_and_common_contract_remains(self):
        explanation_paths = (
            ROOT / "explanations" / "index.html",
            ROOT / "explanations" / "first-test.html",
            ROOT / "explanations" / "windows-publication-design.html",
        )
        self.assertTrue(all(not path.exists() for path in explanation_paths))
        self.assertFalse((ROOT / "explanations").exists())

        index_html = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertNotIn("explanations/", index_html)
        self.assertNotIn("解説HTML", index_html)

        agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        claude = (ROOT / "CLAUDE.md").read_text(encoding="utf-8")
        for instructions in (agents, claude):
            for forbidden in (
                "README.html",
                "PostToolUse",
                "markdown_to_html",
                "explanations",
                "HTML自動変換",
                "自動変換",
                "htmlで解説",
                "HTML形式で公開用",
                "GitHub Pages",
                r"B:\yuki\niray\03_knowledge",
                "一方向",
                "逆流",
                "直接 `main`",
            ):
                self.assertNotIn(forbidden, instructions)

        for required in (
            "assistant／tutor／PM",
            "読み取り・編集・テスト・ビルド・Git差分確認",
            "commit、push、公開、削除、破壊的変更",
            "ユーザーの明示的な指示",
            "/mnt/s/hermes/obsidian-study/CCNA/",
            "唯一のSSOT",
            "yuki-atelier/ccna",
            "派生問題集",
            "教科書や進捗管理の正本にしない",
            "逆同期しない",
        ):
            self.assertIn(required, agents)

        self.assertTrue(claude.startswith("@AGENTS.md"))
        claude_site_rules = claude.split("\n", 1)[1]
        for forbidden in ("Git 運用方針", "SSOT", "Obsidian", "commit", "push", "同期", "main"):
            self.assertNotIn(forbidden, claude_site_rules)
        for required in (
            "共通 CSS は `css/style.css`",
            "Google Fonts CDN",
            "assets/icons/*.png",
            "Devicon CDN",
            "絵文字は使わない",
            "ui-icons.svg",
        ):
            self.assertIn(required, claude_site_rules)
