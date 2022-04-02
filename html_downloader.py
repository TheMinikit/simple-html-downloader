import requests


def fetch_pages(passed_urls, name="url"):

    if type(passed_urls) != "list":
        url_list = [passed_urls]
    else:
        url_list = passed_urls

    for url in url_list:
        response = requests.get(url)
        page_content = response.text
        with open(str(name) + ".html", 'w', encoding="utf8") as fp:
            fp.write(page_content)
