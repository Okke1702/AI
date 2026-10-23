import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse


TIMEOUT = 15
MAX_CONTENT_LENGTH = 12000

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 "
        "(Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 "
        "(KHTML, like Gecko) "
        "Chrome/151.0.0.0 Safari/537.36"
    )
}


def is_valid_url(url):

    try:
        parsed = urlparse(url)

        return (
            parsed.scheme in ("http", "https")
            and bool(parsed.netloc)
        )

    except Exception:
        return False


def web_fetch(url):

    url = url.strip()

    if not url:
        return "URL không được để trống."

    if not is_valid_url(url):
        return f"URL không hợp lệ: {url}"

    try:

        response = requests.get(
            url,
            headers=HEADERS,
            timeout=TIMEOUT
        )

        response.raise_for_status()

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        # Xóa thành phần không cần thiết
        for element in soup([
            "script",
            "style",
            "noscript",
            "header",
            "footer",
            "nav",
            "aside"
        ]):
            element.decompose()

        # Lấy text
        text = soup.get_text(
            separator="\n"
        )

        # Làm sạch
        lines = []

        for line in text.splitlines():

            line = line.strip()

            if line:
                lines.append(line)

        text = "\n".join(lines)

        # Giới hạn dữ liệu gửi cho AI
        if len(text) > MAX_CONTENT_LENGTH:

            text = text[:MAX_CONTENT_LENGTH]

            text += (
                "\n\n"
                "[Nội dung đã được cắt bớt.]"
            )

        if not text:
            return "Không đọc được nội dung trang web."

        return f"""
WEB PAGE

URL:
{url}

NỘI DUNG:

{text}
""".strip()

    except requests.exceptions.Timeout:

        return "Trang web phản hồi quá lâu."

    except requests.exceptions.ConnectionError:

        return "Không thể kết nối tới trang web."

    except requests.exceptions.HTTPError as e:

        return f"Lỗi HTTP: {e}"

    except Exception as e:

        return f"Lỗi khi đọc trang web: {e}"