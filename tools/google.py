import webbrowser
import urllib.parse


def google_search(query):
    query = query.strip()

    encoded_query = urllib.parse.quote_plus(query)

    url = f"https://www.google.com/search?q={encoded_query}"

    try:
        webbrowser.open(url)
        return f"Đã tìm kiếm Google: {query}"

    except Exception as e:
        return f"Lỗi khi mở Google: {e}"