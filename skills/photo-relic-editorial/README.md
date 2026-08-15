# Photo Relic Editorial / 纸上留影
把真实照片压缩成一张安静的纸上记忆版画。  
Turn real photographs into quiet paper-memory editorial artworks.

## Paper Beijing / 纸上北京

<table>
  <tr>
    <td align="center" width="33%">
      <img src="examples/paper-beijing/geese-procession.png" alt="Geese procession Photo Relic example" width="280"><br>
      <sub>碎石成队 / Gravel Falls Into Line</sub>
    </td>
    <td align="center" width="33%">
      <img src="examples/paper-beijing/bird-nest-reflection.png" alt="Bird Nest reflection Photo Relic example" width="280"><br>
      <sub>巢光入水 / Nest Light Enters Water</sub>
    </td>
    <td align="center" width="33%">
      <img src="examples/paper-beijing/temple-of-heaven.png" alt="Temple of Heaven Photo Relic example" width="280"><br>
      <sub>天光有序 / Ordered Sky Light</sub>
    </td>
  </tr>
  <tr>
    <td align="center" width="33%">
      <img src="examples/paper-beijing/china-zun.png" alt="China Zun skyline Photo Relic example" width="280"><br>
      <sub>暮色立住 / Dusk Stands Still</sub>
    </td>
    <td align="center" width="33%">
      <img src="examples/paper-beijing/great-wall-ridge.png" alt="Great Wall ridge Photo Relic example" width="280"><br>
      <sub>山脊有路 / A Road Along the Ridge</sub>
    </td>
    <td align="center" width="33%">
      <img src="examples/paper-beijing/corner-tower-water.png" alt="Forbidden City corner tower Photo Relic example" width="280"><br>
      <sub>水照宫墙 / Palace Wall in Water</sub>
    </td>
  </tr>
</table>

## 中文

Photo Relic Editorial 是一个 Codex skill，用来把用户提供的照片转化成竖版编辑艺术图：上半部分保留真实照片，下半部分生成一张可识别、克制、带纸张质感的“纸上留影”。

它不是把照片简单画成插画，也不是极简到失去主体。它会从原图里提取结构、光线、颜色、重心和情绪，再把这些信息压缩成类似现代版画、东方留白、旅行记忆标本的视觉语言。

适合的照片类型：

- 古建筑、城市地标、天际线、桥、塔、体育馆
- 有清楚轮廓、强光影、倒影或秩序感的场景
- 旅行、人群、动物队列、街头瞬间
- 可以被压缩成“形状 + 光 + 少量颜色”的摄影作品

### 安装

把整个 `photo-relic-editorial` 文件夹复制到你的 Codex skills 目录。

Windows PowerShell:

```powershell
Copy-Item -Recurse .\photo-relic-editorial $env:USERPROFILE\.codex\skills\
```

macOS / Linux:

```bash
cp -R ./photo-relic-editorial ~/.codex/skills/
```

如果安装后没有立刻出现，重启 Codex。

### 使用

附上一张照片，然后输入：

```text
Use $photo-relic-editorial to turn this photo into a Photo Relic artwork.
```

中文系列可以这样说：

```text
Use $photo-relic-editorial. Make it feel like the "Paper Beijing" series, with a short four-character Chinese title.
```

## English

Photo Relic Editorial is a Codex skill for transforming user-provided photographs into vertical editorial artworks: the top half keeps the real photograph truthful, while the lower half becomes a recognizable, restrained, paper-textured "photo relic."

It is not a generic illustration filter, and it should not simplify the subject until the shape disappears. The skill extracts structure, light, color, visual weight, and mood from the source photo, then compresses them into a modern printmaking language with quiet Eastern restraint and generous negative space.

Best suited for:

- historic architecture, landmarks, skylines, bridges, towers, stadiums
- scenes with strong silhouettes, light, reflections, or visual order
- travel moments, crowds, animal processions, and quiet street scenes
- photographs that can be distilled into "shape + light + a few colors"

### Install

Copy the entire `photo-relic-editorial` folder into your Codex skills directory.

Windows PowerShell:

```powershell
Copy-Item -Recurse .\photo-relic-editorial $env:USERPROFILE\.codex\skills\
```

macOS / Linux:

```bash
cp -R ./photo-relic-editorial ~/.codex/skills/
```

Restart Codex if the skill does not appear immediately.

### Use

Attach a photo and ask:

```text
Use $photo-relic-editorial to turn this photo into a Photo Relic artwork.
```

For a Chinese social-video series:

```text
Use $photo-relic-editorial. Make it feel like the "Paper Beijing" series, with a short four-character Chinese title.
```

## License

MIT. Use this skill with original photos, licensed photos, or images you have permission to transform. Example images are included as visual references for the skill's aesthetic.
