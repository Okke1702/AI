import webbrowser


def open_website(url):
    url = url.strip()

    try:
        webbrowser.open(url)
        return f"Đã mở website: {url}"

    except Exception as e:
        return f"Lỗi khi mở website: {e}"