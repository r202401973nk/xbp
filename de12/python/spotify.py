import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# 認証情報
client_id ="00875d1f171846cf855a7053b00af61f" # Client IDを入力してください
client_secret = "2dad4ca9e8b441439dd4de79b4f8033d" # Client secretを入力してください
ccm = SpotifyClientCredentials(client_id = client_id, client_secret = client_secret)
spotify = spotipy.Spotify(client_credentials_manager = ccm)

# 気分とジャンルを定義
mood = input("気分を教えてください 例 happy sad: ")
genre = int(input("ジャンルを選択しますか？ はい → 1  いいえ → 2: "))
if genre := "1":
    genre_select = input("指定するジャンルを教えてください 例 pop jazz: ")
else:
    genre_select = None


if genre_select is None:
    query = f'{mood}'  # 気分のみで検索
else:
    query = f'{mood} {genre_select}'  # 気分とジャンルで検索

# 検索
how_limit=int(input("いくつプレイリストを探しますか？: "))
results = spotify.search(q=query, type="playlist", limit=how_limit)

# 検索結果からプレイリスト名とその詳細を表示
for idx, playlist in enumerate(results['playlists']['items']):
    playlist_name = playlist['name']
    playlist_description = playlist['description']
    playlist_url = playlist['external_urls']['spotify']
    print(f"{idx + 1}. {playlist_name}")
    print(f"   説明: {playlist_description}")
    print(f"   URL: {playlist_url}\n")
