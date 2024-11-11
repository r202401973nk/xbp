import time

print("体内時計ゲームゲーム")
print("このゲームは自分の体内時計が正確か確かめるゲームです。誤差±0.5秒まではチャレンジ成功です。")

player_input = int(input("チャレンジする秒数を入力してください。"))

input("準備ができたらEnterキーを押してスタートしてください")
start_time = time.time()

input("あなたがチャレンジする秒数が経ったと思ったらEnterキーを押してください")
end_time = time.time()

elapsed_time = end_time - start_time
print(f"秒数: {elapsed_time:.2f}秒")

if  player_input - 0.5 <=elapsed_time <= player_input + 0.5:
    print("おめでとうございます！あなたの体内時計は正確です！")
else:
    print("残念！あなたの体内時計は正確ではありません！")

