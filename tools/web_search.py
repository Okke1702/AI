from ddgs import DDGS


def web_search(query, max_results=5):

    query = query.strip()

    if not query:
        return "Không có nội dung tìm kiếm."


    try:

        results = []

        with DDGS() as ddgs:

            search_results = ddgs.text(
                query,
                max_results=max_results
            )

            for result in search_results:

                title = result.get("title", "")
                url = result.get("href", "")
                body = result.get("body", "")

                results.append({
                    "title": title,
                    "url": url,
                    "body": body
                })


        if not results:

            return "Không tìm thấy kết quả."


        # =====================================
        # TẠO KẾT QUẢ CHO QWEN
        # =====================================

        output = "KẾT QUẢ TÌM KIẾM:\n\n"


        for index, result in enumerate(results, start=1):

            output += f"""
[{index}]
Tiêu đề: {result["title"]}
URL: {result["url"]}
Nội dung: {result["body"]}

"""


        return output.strip()


    except Exception as e:

        return f"Lỗi khi tìm kiếm Internet: {e}"