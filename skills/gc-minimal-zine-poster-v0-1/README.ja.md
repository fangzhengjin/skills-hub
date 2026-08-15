# GC Minimal Zine Poster v0.3.1

[English](README.md) · [简体中文](README.zh-CN.md) · **日本語**

Minimal Zine Poster v0.3.1 は、テーマ、短い文章、記事のアイデア、物、雰囲気、写真、参照画像のセットから、紙の質感を持つミニマルなエディトリアルポスター、実用的な画像生成プロンプト、または再利用可能なビジュアルシステムを作る Codex Skill です。

呼び出し名は `gc-minimal-zine-poster-v0-3` です。

## v0.3.1 の主な変更点

- 文字通りに誤解される可能性がある抽象的な構図用語を、明確な焦点要素と色のアクセント表現に置き換えました。
- 最終画像生成プロンプトでは、写真の切り抜き、紙片、インクの面、標本、印刷イラスト、テクスチャ窓、文字など、実際に見える媒体を明記します。
- 意図しない航海用シンボルや一般的なアイコンを検出する品質チェックを追加しました。
- 非海事テーマと鮮やかな赤い焦点要素を使う回帰評価を追加しました。
- Generate、Reference Analysis、Prompt-only、Analyze + Generate、Photo Input の各ルートは維持されます。
- 後方互換性のため、呼び出し名は `gc-minimal-zine-poster-v0-3` のままです。

## ビジュアル方針

各リクエストを、余白を活かした縦長の紙のポスターとして構成します。

- 標準は 3:5 比率の古びた紙のキャンバス
- 70%〜90% のネガティブスペース
- 小さく明確な一つの主題または視覚的な出来事
- セリフ、タイプライター、等幅、または控えめな小型サンセリフ書体
- はっきり見える一つの高彩度カラーアクセント
- ゼロックス、リソグラフ、ハーフトーン、活版印刷、スキャン紙の欠けや質感
- 静かな日本／韓国のインディー ZINE、またはミニマルなエディトリアルデザインの空気感

商業広告のレイアウト、光沢のあるモックアップ、映画的な照明、3D レンダリング、ネオン、密集したスクラップブック、参照元のアイデンティティの複製、大量の整った文章は避けます。

## 作例

以下の 6 点はすべてリポジトリ作者が制作したものです。

| Night Door | Yellow Step |
| --- | --- |
| ![Night Door](examples/night-door.jpeg) | ![Yellow Step](examples/yellow-step.jpeg) |

| Shore Pause | Pause Map |
| --- | --- |
| ![Shore Pause](examples/shore-pause.jpeg) | ![Pause Map](examples/pause-map.jpeg) |

| Typhoon Memory | Moon Tide |
| --- | --- |
| ![Typhoon Memory](examples/typhoon-memory.jpeg) | ![Moon Tide](examples/moon-tide.jpeg) |

## 動作要件

- Codex、または互換性のある Skill 実行環境。
- 参照分析と品質確認には画像を読み取る機能が必要です。
- Generate と Analyze + Generate には、実行環境の画像生成機能が必要です。

Skill パッケージには、スクリプト、外部フォント、API キー、非公開パス、追加ダウンロードが必要な実行素材は含まれていません。最終的な生成品質と写真の保持精度は、実行環境で利用できる画像モデルに依存します。

## インストール

現在の v0.3.1 を、名前が一致する Skill ディレクトリへクローンします。

```bash
git clone https://github.com/LiamGvchi/gc-minimal-zine-poster.git \
  ~/.codex/skills/gc-minimal-zine-poster-v0-3
```

Skill がすぐに表示されない場合は Codex を再起動してください。

## v0.3.0 からのアップグレード

呼び出し名とインストール先は変わりません。既存の v0.3 インストールが変更のない Git チェックアウトであれば、次を実行できます。

```bash
git -C ~/.codex/skills/gc-minimal-zine-poster-v0-3 pull --ff-only
```

Git チェックアウトではない場合やローカル変更がある場合は、新しいコピーを別にインストールして差分を確認し、既存の変更を直接上書きしないでください。

## v0.1 からのアップグレード

既存の `~/.codex/skills/gc-minimal-zine-poster-v0-1` ディレクトリ内で、そのまま v0.3.1 を pull しないでください。ディレクトリ名と Skill の frontmatter 名を一致させる必要があります。

上のコマンドを使い、v0.3.1 を旧版とは別のディレクトリにインストールしてください。v0.3.1 の動作確認後、旧ディレクトリを残すか削除するかは利用者が選べます。

保存された v0.1 をインストールする場合：

```bash
git clone --branch v0.1.0 \
  https://github.com/LiamGvchi/gc-minimal-zine-poster.git \
  ~/.codex/skills/gc-minimal-zine-poster-v0-1
```

## 使い方

ポスターを生成：

```text
$gc-minimal-zine-poster-v0-3 を使って、雨の日の古書店をテーマにしたポスターを作って。
```

画像を生成せず参照セットを分析：

```text
$gc-minimal-zine-poster-v0-3 を使ってこの画像フォルダを分析し、固定ルールと可変ルールを分け、元画像の文章をコピーせず再利用可能なプロンプトを返して。
```

入力写真を編集対象として使用：

```text
$gc-minimal-zine-poster-v0-3 を使ってこの人物写真をポスターにして。人物の同一性と服装は保持し、レイアウトと紙の質感だけを変更して。
```

プロンプトのみを取得：

```text
$gc-minimal-zine-poster-v0-3 を使って、夜に閉店する古書店の最終画像生成プロンプトだけを返して。画像は生成しないで。
```

## リクエストモード

- **Generate：**内容 → 視覚的な比喩 → プロンプト → ラスター画像 → 検査。
- **Photo Input：**画像の役割と保持レベルを決め、実際の対象画像を生成に渡し、元の特徴が保持されたか確認します。
- **Reference Analysis：**実ファイルを調べ、観察証拠、固定ルール、可変ルール、サンプル残留、再利用可能なプロンプト、制限を返します。
- **Prompt-only：**画像を生成したと主張せず、4 段落の最終プロンプトと Recipe だけを返します。
- **Analyze + Generate：**先にビジュアルシステムを抽出し、参照元の構図を複製しない新しい作品を生成します。

## 出力

生成リクエストでは、次を返します。

1. 生成されたラスター形式のポスター
2. 最終画像生成プロンプト
3. 選択した Recipe
4. 短い解釈メモ
5. 写真が指定された場合の画像の役割と保持情報

参照分析では、証拠に基づくビジュアルシステムと再利用可能なプロンプトを返します。生成も明示的に依頼された場合を除き、画像は生成しません。

## リポジトリ構成

- `SKILL.md`：リクエストのルーティングと実行ワークフロー
- `references/style-system.md`：固定アイデンティティ、可変要素、色、主題ロジック、避ける方向
- `references/prompt-compiler.md`：プロンプトの項目順序と 4 段落コンパイラ
- `references/variation-engine.md`：レイアウトとバリエーションのレシピ
- `references/reference-analysis.md`：参照画像の証拠収集と統合手順
- `references/quality-gate.md`：生成、参照分析、Prompt-only の品質確認
- `agents/openai.yaml`：Codex UI メタデータ
- `evals/evals.json`：再利用可能な評価プロンプト
- `examples/`：作者制作の 6 点のポスター作例
- `LICENSE`：MIT ライセンス

## 謝辞

小紅書ユーザー **@李李** さんが、抽象的な構図用語が文字通りに解釈され、意図しない航海用アイコンが生成される可能性を報告してくださいました。この指摘をきっかけに、v0.3.1 では用語、プロンプトコンパイラ、品質チェック、回帰評価を体系的に修正しました。

## ライセンス

MIT。詳細は [LICENSE](LICENSE) を参照してください。
