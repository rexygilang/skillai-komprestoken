# skillai-komprestoken

Skill AI untuk jawaban ringkas: memangkas basa-basi, bukan mengubah isi teknis.

## Isi repo

- `skills/kompres-token-claude/` -- skill Claude (Desktop, web, mobile, Claude Code).
- `skills/kompres-token-antigravity/` -- varian Antigravity, gaya telegrafis Bahasa Indonesia.
- `.agents/skills/kompres-token-opencode/` -- varian OpenCode.
- `.claude-plugin/` -- manifest plugin Claude.
- `commands/kompres-token.md` -- slash command untuk plugin Claude.

## Claude Desktop atau web, plan free

Plugin marketplace memerlukan plan berbayar. Alternatif gratis: unggah skill langsung.

1. Buka `Settings > Capabilities`, aktifkan `Code execution` dan `Create and edit files`.
2. Buka `Plugins` (dulu bernama `Customize`) -> `Skills` -> `+` -> `Upload skill`.
3. Unggah `dist/kompres-token-claude.zip` (atau `dist/kompres-token-claude.skill`). Jangan memakai berkas plugin.

Skill aktif otomatis saat permintaan cocok dengan description. Jalur ini juga bekerja di Claude Code.

## Claude Desktop, plan berbayar (opsional)

1. Buka `Plugins` -> `Add` -> `Add marketplace`.
2. Masukkan `rexygilang/skillai-komprestoken`.
3. Pasang plugin `kompres-token-claude`.

Slash command `/kompres-token` tersedia lewat plugin. Alternatif unggah manual: `Plugins` -> `Add` -> `Upload plugin` -> pilih `dist/kompres-token-claude-plugin.zip`.

## Claude mobile

Mobile tidak mendukung plugin maupun skill. Salin isi `skills/kompres-token-claude/SKILL.md` ke Custom Instructions.

## OpenCode

Salin `.agents/skills/kompres-token-opencode/` ke `%USERPROFILE%\.config\opencode\skills\` di Windows, atau `~/.config/opencode/skills/` di macOS/Linux. Lalu panggil `/kompres-token-opencode`.

## Atribusi

Diadaptasi dari [Caveman](https://github.com/JuliusBrussee/caveman) oleh JuliusBrussee (MIT).
