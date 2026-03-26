# 論文添削ボット

## 概要
公務員試験の論文対策として作成した、AIを活用した論文添削ツールです。
GeminiAPIを使用して、論文の構成・改善点・点数を自動でフィードバックします。

## 作成の背景
公務員試験の論文対策において、添削者を確保することが難しいという課題がありました。
PythonとGemini APIを活用することで、いつでも添削を受けられる環境を自作しました。

## 機能
- 論文ファイル（.txt）の読み込み
- AIによる論文の構成評価
- 良い点・改善点の具体的なフィードバック
- 100点満点での採点
- 添削結果のファイル保存（タイムスタンプ付き）

## 使用技術
- Python 3.14
- Google Gemini API（gemini-2.5-flash）
- python-dotenv

## 使い方
1. リポジトリをクローンする
2. 必要なライブラリをインストールする
   pip install google-genai python-dotenv
3. .envファイルを作成してAPIキーを設定する
   GEMINI_API_KEY=あなたのAPIキー
4. ronbun.txtに添削したい論文を入力する
5. 実行する
   python main.py

## ファイル構成
- main.py：メインの実行ファイル
- ronbun_bot.py：RonbunBotクラスの定義
- ronbun.txt：添削対象の論文ファイル
