import requests


def fetch_pages(passed_url):
    url_list = [passed_url]
    for url in url_list:
        response = requests.get(url)
        page_content = response.text
        with open(str(url) + ".html", 'w', encoding="utf8") as fp:
            fp.write(page_content)
