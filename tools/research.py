from tools.web_search import web_search
from tools.web_fetch import web_fetch


MAX_SOURCES = 3


def research(query, max_sources=MAX_SOURCES):

    query = query.strip()

    if not query:
        return "QUERY không được để trống."

    try:

        # ==============================
        # 1. TÌM KIẾM
        # ==============================

        search_result = web_search(
            query,
            max_results=max_sources
        )

        if not search_result:
            return "Không tìm thấy kết quả."


        # ==============================
        # 2. LẤY URL
        # ==============================

        urls = extract_urls(search_result)

        if not urls:
            return "Không tìm thấy URL trong kết quả."


        # ==============================
        # 3. ĐỌC WEBSITE
        # ==============================

        results = []

        total = min(
            len(urls),
            max_sources
        )

        for index, url in enumerate(
            urls[:max_sources],
            start=1
        ):

            print(
                f"[Research] Đọc nguồn "
                f"{index}/{total}..."
            )

            content = web_fetch(url)

            results.append(
                f"""
===== NGUỒN {index} =====

URL:
{url}

NỘI DUNG:

{content}
""".strip()
            )


        # ==============================
        # 4. TRẢ KẾT QUẢ
        # ==============================

        return "\n\n".join(results)


    except Exception as e:

        return f"Lỗi Research: {e}"


def extract_urls(search_result):

    urls = []

    for line in search_result.splitlines():

        line = line.strip()

        if line.startswith("URL:"):

            url = line.replace(
                "URL:",
                "",
                1
            ).strip()

            if url and url not in urls:

                urls.append(url)

    return urls