import requests

from tools import open_application
from tools_file import open_file, open_folder
from duongdan import open_website
from google import google_search
from memory import remember, forget, get_memory, load_memory

URL = "http://localhost:11434/api/chat"
MODEL = "qwen3:8b"
memory = load_memory()

messages = [
    {
        "role": "system",
        "content": f"""
Bạn là MyAI, trợ lý AI local của tôi.

Bạn giao tiếp bằng tiếng Việt.
Bạn trả lời rõ ràng và thân thiện.

Đây là thông tin người dùng đã cho phép bạn ghi nhớ:

{memory}

Nếu thông tin cần thiết để trả lời câu hỏi có trong Memory,
hãy sử dụng thông tin đó.

Bạn không được tự bịa thông tin không có trong Memory.

Bạn có các công cụ:

1. open_application(app_name)
Dùng để mở ứng dụng.

2. open_file(file_path)
Dùng để mở file.

3. open_folder(folder_path)
Dùng để mở thư mục.

4. open_website(url)
Dùng để mở website.

5. google_search(query)
Dùng để tìm kiếm Google.

6. remember(key, value)
Dùng để ghi nhớ thông tin.

7. forget(key)
Dùng để quên thông tin.

8. get_memory()
Dùng để đọc bộ nhớ.

Khi cần ghi nhớ:

TOOL: remember
KEY: tên thuộc tính
VALUE: giá trị

Khi cần quên:

TOOL: forget
KEY: tên thuộc tính

Khi cần đọc Memory:

TOOL: get_memory
"""
    }
]


print("=============================")
print("          MY AI")
print("=============================")
print("Gõ 'exit' để thoát.\n")


while True:

    user_input = input("Bạn: ")

    if user_input.lower() == "exit":
        print("AI: Tạm biệt!")
        break

    messages.append({
        "role": "user",
        "content": user_input
    })

    data = {
        "model": MODEL,
        "messages": messages,
        "stream": False
    }

    try:

        response = requests.post(
            URL,
            json=data,
            timeout=120
        )

        response.raise_for_status()

        result = response.json()

        ai_message = result["message"]["content"]

        print("AI:", ai_message)
        print()

        # =========================
        # TOOL: OPEN APPLICATION
        # =========================

        if "TOOL: open_application" in ai_message:

            lines = ai_message.splitlines()

            app_name = None

            for line in lines:

                if line.startswith("APP:"):
                    app_name = line.replace("APP:", "").strip()

            if app_name:
                tool_result = open_application(app_name)

                print("TOOL:", tool_result)
                print()


        # =========================
        # TOOL: OPEN FILE
        # =========================

        elif "TOOL: open_file" in ai_message:

            lines = ai_message.splitlines()

            file_path = None

            for line in lines:

                if line.startswith("FILE:"):
                    file_path = line.replace("FILE:", "").strip()

            if file_path:
                tool_result = open_file(file_path)

                print("TOOL:", tool_result)
                print()


        # =========================
        # TOOL: OPEN FOLDER
        # =========================

        elif "TOOL: open_folder" in ai_message:

            lines = ai_message.splitlines()

            folder_path = None

            for line in lines:

                if line.startswith("FOLDER:"):
                    folder_path = line.replace("FOLDER:", "").strip()

            if folder_path:
                tool_result = open_folder(folder_path)

                print("TOOL:", tool_result)
                print()
        elif "TOOL: open_website" in ai_message:

            lines = ai_message.splitlines()

            url = None

            for line in lines:

                if line.startswith("URL:"):
                    url = line.replace("URL:", "").strip()

            if url:
                tool_result = open_website(url)

                print("TOOL:", tool_result)
                print()
        elif "TOOL: google_search" in ai_message:

            lines = ai_message.splitlines()

            query = None

            for line in lines:

                if line.startswith("QUERY:"):
                    query = line.replace("QUERY:", "").strip()

            if query:
                tool_result = google_search(query)

                print("TOOL:", tool_result)
                print()
        elif "TOOL: remember" in ai_message:

            lines = ai_message.splitlines()

            key = None
            value = None

            for line in lines:

                if line.startswith("KEY:"):
                    key = line.replace("KEY:", "").strip()

                elif line.startswith("VALUE:"):
                    value = line.replace("VALUE:", "").strip()

            if key and value:

                tool_result = remember(key, value)

                print("MEMORY:", tool_result)
                print()
        elif "TOOL: forget" in ai_message:

            lines = ai_message.splitlines()

            key = None

            for line in lines:

                if line.startswith("KEY:"):
                    key = line.replace("KEY:", "").strip()

            if key:

                tool_result = forget(key)

                print("MEMORY:", tool_result)
                print()

        elif "TOOL: get_memory" in ai_message:

            memory = get_memory()

            print("MEMORY:", memory)
            print()

        messages.append({
            "role": "assistant",
            "content": ai_message
        })


    except requests.exceptions.RequestException as e:

        print("Lỗi kết nối Ollama:", e)
        print()


    except Exception as e:

        print("Có lỗi xảy ra:", e)
        print()