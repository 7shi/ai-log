# [browser console]
# document.getElementsByTagName("xap-inline-dialog-container")[0]

import sys
from bs4 import BeautifulSoup

args = sys.argv[1:]
if len(args) != 1:
    print(f"Usage: python {sys.argv[0]} html")
    sys.exit(1)

with open(args[0], "r") as f:
    html = f.read()

# BeautifulSoupオブジェクトを作成
soup = BeautifulSoup(html, "html.parser")

# テーブルを見つける
table = soup.find("table", {"class": "preview-table"})

# テーブルの各行を処理する
for i, row in enumerate(table.find_all("tr")):
    # 2列目（コンテンツ）を取得
    content = row.find('td', {"class": "prompt-text"}).get_text(strip=True)
    # Markdown形式で出力
    if i % 2 == 0:
        if i:
            print()
        print("## \n")
        for line in content.splitlines():
            print(" " * 4, line, sep="")
    else:
        print("\n", content, sep="")

# トークン数を取得
if item_about := soup.find('div', class_='item-about'):
    title = item_about.find(string=True, recursive=False).strip()
    content = item_about.find_next_sibling('div').get_text(strip=True)
    # Markdown形式で出力
    print(f"\n## {title}\n\n{content}\n")
