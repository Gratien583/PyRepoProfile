from jinja2 import Environment, FileSystemLoader

def generate_html(name, about_me, repos, avatar_url, output_file="output/index.html",):
    # テンプレートファイルのディレクトリを設定
    env = Environment(loader=FileSystemLoader('template'))
    template = env.get_template('template.html')
    
    # HTMLに埋め込むデータ
    html_content = template.render(name=name, about_me=about_me, repos=repos, avatar_url=avatar_url)
    
    # HTMLファイルに書き込む
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"HTMLポートフォリオが生成されました: {output_file}")
