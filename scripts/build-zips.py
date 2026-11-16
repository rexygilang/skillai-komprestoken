r"""Bangun ulang ZIP unggahan Claude dengan entry path memakai '/'.

Compress-Archive bawaan Windows menulis backslash (\), ditolak Claude Desktop
dengan error 'Zip file contains path with invalid characters'.
"""

import shutil
import zipfile
from pathlib import Path

repo = Path(__file__).resolve().parent.parent
dist = repo / "dist"
dist.mkdir(exist_ok=True)

skill_md = repo / "skills" / "kompres-token-claude" / "SKILL.md"
plugin_json = repo / ".claude-plugin" / "plugin.json"
marketplace_json = repo / ".claude-plugin" / "marketplace.json"
command_md = repo / "commands" / "kompres-token.md"
version_json = repo / "version.json"
readme = repo / "README.md"


def write_zip(path, entries):
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        for arcname, src in entries:
            z.write(src, arcname)


skill_zip = dist / "kompres-token-claude.zip"
write_zip(skill_zip, [("SKILL.md", skill_md)])
shutil.copyfile(skill_zip, dist / "kompres-token-claude.skill")

write_zip(
    dist / "kompres-token-claude-plugin.zip",
    [
        (".claude-plugin/plugin.json", plugin_json),
        (".claude-plugin/marketplace.json", marketplace_json),
        ("skills/kompres-token-claude/SKILL.md", skill_md),
        ("commands/kompres-token.md", command_md),
        ("version.json", version_json),
        ("README.md", readme),
    ],
)

write_zip(
    dist / "kompres-token-claude-unified.zip",
    [
        (".claude-plugin/plugin.json", plugin_json),
        ("SKILL.md", skill_md),
        ("skills/kompres-token-claude/SKILL.md", skill_md),
        ("commands/kompres-token.md", command_md),
        ("version.json", version_json),
        ("README.md", readme),
    ],
)

for path in sorted(dist.glob("kompres-token-claude*")):
    if path.suffix not in {".zip", ".skill"}:
        continue
    with zipfile.ZipFile(path) as z:
        print(path.name, path.stat().st_size, [i.filename for i in z.infolist()])
