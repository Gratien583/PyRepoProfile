import requests

def get_repos(username):
    # ユーザー情報を取得（アバター画像など）
    user_url = f"https://api.github.com/users/{username}"
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        raise Exception(f"ユーザー情報の取得に失敗しました（{user_response.status_code}）")

    user_data = user_response.json()
    avatar_url = user_data.get('avatar_url', '')

    # リポジトリ一覧を取得
    repos_url = f"https://api.github.com/users/{username}/repos"
    repos_response = requests.get(repos_url)
    if repos_response.status_code != 200:
        raise Exception(f"GitHub APIエラー（{repos_response.status_code}）")

    repos = repos_response.json()

    # リポジトリ一覧とアバター画像URLを返す
    return repos, avatar_url
