# PyRepoProfile 🐍📁

GitHubのリポジトリ情報を自動取得し、リポジトリ一覧ページを生成するPythonツールです。  
私が初めてPythonを使った作品です。

---

## 📌 概要

`PyRepoProfile` は、指定したGitHubユーザーのリポジトリ情報を取得し、静的なHTMLとして出力することで、リポジトリ一覧ページを自動生成します。  
あわせて自己紹介も入力でき、1つのHTMLファイルにまとめられたプロフィールページとして出力されます。

---

## 🔧 主な機能

- GitHubユーザーの全パブリックのリポジトリを取得
- 各リポジトリの説明、スター数、使用言語を表示
- 自己紹介欄を含めたHTMLファイルの出力

---

## 🛠️ 使用技術・ライブラリ

- Python 3.x
- requests（GitHub APIへのHTTPリクエストに使用）
- Jinja2（テンプレートエンジン）

---

## ▶️ 使い方

### 1. 環境構築

```bash
git clone https://github.com/Gratien583/PyRepoProfile.git
cd PyRepoProfile
pip install -r requirements.txt
```

### 2. 実行

```bash
python3 main.py
```

実行すると、以下のように対話形式で入力を求められます：

```
GitHubのユーザー名を入力してください: <GitHubのユーザー名>
自己紹介を入力してください: <自己紹介文>
HTMLポートフォリオが生成されました: output/index.html
自己紹介ページのHTMLが生成されました。
```

### 3. 出力

以下のようなフォルダ構成でHTMLが生成されます：

```
output/
└── index.html
```

ブラウザで `index.html` を開くと、入力した自己紹介とリポジトリ情報がまとめられたページが表示されます。

---

## 🖼️ 出力サンプル

準備中
---