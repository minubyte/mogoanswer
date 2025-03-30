import requests

with open("ans/list.txt") as file:
    urls = file.readlines()

for index, url in enumerate(urls):
    url = url.strip()
    filename = url.split("/")[5]
    response = requests.get(url, stream=True)

    with open(f"ans/img/{filename}.{url[-3:]}", "wb") as img_file:
        for chunk in response.iter_content(1024):
            img_file.write(chunk)
    print(f"done: {filename}")