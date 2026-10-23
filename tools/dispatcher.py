from tools.applications import open_application
from tools.files import open_file, open_folder
from tools.browser import open_website
from tools.google import google_search
from tools.web_search import web_search
from tools.web_fetch import web_fetch
from tools.research import research
from tools.media import (
    media_play_pause,
    media_next,
    media_previous,
    media_mute,
    volume_up,
    volume_down,
    youtube_speed_up,
    youtube_speed_down,
    youtube_normal_speed,
)

from memory.memory import remember, forget, get_memory


# =====================================
# TOOL REGISTRY
# =====================================

TOOLS = {
     "open_application": open_application,
    "open_file": open_file,
    "open_folder": open_folder,
    "open_website": open_website,

    "google_search": google_search,

    "web_search": web_search,
    "web_fetch": web_fetch,
    "research": research,

    "remember": remember,
    "forget": forget,
    "get_memory": get_memory,

    "media_play_pause": media_play_pause,
    "media_next": media_next,
    "media_previous": media_previous,
    "media_mute": media_mute,
    "volume_up": volume_up,
    "volume_down": volume_down,
    "youtube_speed_up": youtube_speed_up,
    "youtube_speed_down": youtube_speed_down,
    "youtube_normal_speed": youtube_normal_speed,
    
}


# =====================================
# LẤY GIÁ TRỊ TỪ AI MESSAGE
# =====================================

def get_value(lines, prefix):

    for line in lines:

        line = line.strip()

        if line.startswith(prefix):

            return line[len(prefix):].strip()

    return None


# =====================================
# EXECUTE TOOL
# =====================================

def execute_tool(ai_message):

    lines = ai_message.splitlines()

    tool_name = None

    # Tìm TOOL

    for line in lines:

        line = line.strip()

        if line.startswith("TOOL:"):

            tool_name = line.replace("TOOL:", "").strip()

            break


    # Không có Tool

    if tool_name is None:

        return None


    # Tool không tồn tại

    if tool_name not in TOOLS:

        return f"Tool không tồn tại: {tool_name}"


    # =====================================
    # OPEN APPLICATION
    # =====================================

    if tool_name == "open_application":

        app_name = get_value(lines, "APP:")

        if not app_name:

            return "Thiếu APP."

        return TOOLS[tool_name](app_name)


    # =====================================
    # OPEN FILE
    # =====================================

    if tool_name == "open_file":

        file_path = get_value(lines, "FILE:")

        if not file_path:

            return "Thiếu FILE."

        return TOOLS[tool_name](file_path)


    # =====================================
    # OPEN FOLDER
    # =====================================

    if tool_name == "open_folder":

        folder_path = get_value(lines, "FOLDER:")

        if not folder_path:

            return "Thiếu FOLDER."

        return TOOLS[tool_name](folder_path)


    # =====================================
    # OPEN WEBSITE
    # =====================================

    if tool_name == "open_website":

        url = get_value(lines, "URL:")

        if not url:

            return "Thiếu URL."

        return TOOLS[tool_name](url)


    # =====================================
    # GOOGLE SEARCH
    # =====================================

    if tool_name == "google_search":

        query = get_value(lines, "QUERY:")

        if not query:

            return "Thiếu QUERY."

        return TOOLS[tool_name](query)
    if tool_name == "web_search":

        query = get_value(lines, "QUERY:")

        if not query:

            return "Thiếu QUERY."

        return TOOLS[tool_name](query)


    # =====================================
    # REMEMBER
    # =====================================

    if tool_name == "remember":

        key = get_value(lines, "KEY:")
        value = get_value(lines, "VALUE:")

        if not key:

            return "Thiếu KEY."

        if not value:

            return "Thiếu VALUE."

        return TOOLS[tool_name](key, value)
    
    if tool_name == "web_fetch":

        url = get_value(lines, "URL:")

        if not url:
            return "Thiếu URL."

        return TOOLS[tool_name](url)
    if tool_name == "research":

        query = get_value(lines, "QUERY:")

        if not query:
            return "Thiếu QUERY."

        return TOOLS[tool_name](query)
    if tool_name == "media_play_pause":
        return TOOLS[tool_name]()


    if tool_name == "media_next":
        return TOOLS[tool_name]()


    if tool_name == "media_previous":
        return TOOLS[tool_name]()


    if tool_name == "media_mute":
        return TOOLS[tool_name]()


    if tool_name == "volume_up":
        return TOOLS[tool_name]()


    if tool_name == "volume_down":
        return TOOLS[tool_name]()


    if tool_name == "youtube_speed_up":
        return TOOLS[tool_name]()


    if tool_name == "youtube_speed_down":
        return TOOLS[tool_name]()


    if tool_name == "youtube_normal_speed":
        return TOOLS[tool_name]()


    # =====================================
    # FORGET
    # =====================================

    if tool_name == "forget":

        key = get_value(lines, "KEY:")

        if not key:

            return "Thiếu KEY."

        return TOOLS[tool_name](key)


    # =====================================
    # GET MEMORY
    # =====================================

    if tool_name == "get_memory":

        return TOOLS[tool_name]()


    return f"Chưa hỗ trợ Tool: {tool_name}"