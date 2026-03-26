import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
import datetime

# .envファイルを読み込む
load_dotenv()

class RonbunBot:
    def __init__(self):
        # APIキーを環境変数から読み込む
        api_key = os.getenv("GEMINI_API_KEY")
        self.client = genai.Client(api_key=api_key)
        self.system_prompt = """
あなたは公務員試験の論文添削の専門家です。
以下のルールに従って添削してください。

- 論文の構成（課題・問題点・解決策・まとめ）を評価する
- 良い点を必ず1つ以上挙げる
- 改善点を具体的に指摘する
- 最後に100点満点で点数をつける
"""

    def analyze(self, text):
        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[{"role": "user", "parts": [{"text": text}]}],
            config=types.GenerateContentConfig(
                system_instruction=self.system_prompt
            )
        )
        return response.text

    def save(self, ronbun, result):
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"result_{timestamp}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write("【論文】\n")
            f.write(ronbun)
            f.write("\n\n【添削結果】\n")
            f.write(result)
        return filename