import json
import tempfile
import unittest
from pathlib import Path

from scripts.training import append_progress, next_suggestion, normalize_blocker, read_last_progress


class TrainingScriptTests(unittest.TestCase):
    def test_chinese_no_blocker_is_normalized(self) -> None:
        self.assertEqual(normalize_blocker("无"), "")

    def test_record_creates_valid_jsonl(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            entry = append_progress(
                root,
                minutes=60,
                completed="RAII A 日",
                blocker="无",
                self_score=2,
                phase="A",
            )
            saved = read_last_progress(root)
            self.assertEqual(saved, entry)
            json.loads((root / "daily" / "progress.jsonl").read_text(encoding="utf-8"))

    def test_a_day_at_l1_advances_to_b_day(self) -> None:
        suggestion = next_suggestion({"blocker": "", "self_score": 1, "phase": "A"})
        self.assertIn("B 日", suggestion)
        self.assertIn("失败基线", suggestion)

    def test_blocker_prevents_advancement(self) -> None:
        suggestion = next_suggestion({"blocker": "MSVC 编译失败", "self_score": 3, "phase": "B"})
        self.assertIn("MSVC 编译失败", suggestion)
        self.assertNotIn("C 日", suggestion)


if __name__ == "__main__":
    unittest.main()
