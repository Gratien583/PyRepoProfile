from github_api import get_repos
from html_generator import generate_html

def main():
    # ユーザー名と自己紹介を入力
    username = input("GitHubのユーザー名を入力してください: ")
    about_me = input("自己紹介を入力してください: ")

    # GitHub APIからリポジトリ情報を取得
    try:
        repos, avatar_url = get_repos(username)
    except Exception as e:
        print(f"エラーが発生しました: {e}")
        return

    # HTMLページを生成
    generate_html(username, about_me, repos, avatar_url)
    print("自己紹介ページのHTMLが生成されました。")

if __name__ == "__main__":
    main()
