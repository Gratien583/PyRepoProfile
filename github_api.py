import requests

def get_repos(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"GitHub APIエラー。ステータスコード: {response.status_code}")
    
    repos = response.json()

    # リポジトリ情報に画像URL（GitHubにアップロードされた画像）を追加
    for repo in repos:
        repo['image_url'] = f"https://camo.githubusercontent.com/{repo['owner']['login']}/https://github.com/{repo['owner']['login']}/{repo['name']}/raw/main/repository-image.jpg"
    
    return repos
