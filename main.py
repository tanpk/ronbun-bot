from ronbun_bot import RonbunBot

# ボットを作成
bot = RonbunBot()

# 論文ファイルを読み込む
with open("ronbun.txt", "r", encoding="utf-8") as f:
    ronbun = f.read()

print("論文を読み込みました。添削を開始します。\n")

# 添削する
result = bot.analyze(ronbun)
print(f"【添削結果】\n{result}")

# 保存する
filename = bot.save(ronbun, result)
print(f"\n添削結果を{filename}に保存しました。")