import json
import urllib.request

import pyautogui
import websocket


CHROME_DEBUG_URL = "http://127.0.0.1:9222"


# =====================================================
# WINDOWS MEDIA
# =====================================================

def media_play_pause():
    try:
        pyautogui.press("playpause")
        return "Đã phát hoặc tạm dừng media."
    except Exception as e:
        return f"Lỗi play/pause: {e}"


def media_next():
    try:
        pyautogui.press("nexttrack")
        return "Đã chuyển sang media tiếp theo."
    except Exception as e:
        return f"Lỗi next: {e}"


def media_previous():
    try:
        pyautogui.press("prevtrack")
        return "Đã quay lại media trước."
    except Exception as e:
        return f"Lỗi previous: {e}"


def media_mute():
    try:
        pyautogui.press("volumemute")
        return "Đã bật/tắt âm thanh."
    except Exception as e:
        return f"Lỗi mute: {e}"


def volume_up():
    try:
        pyautogui.press("volumeup")
        return "Đã tăng âm lượng."
    except Exception as e:
        return f"Lỗi tăng âm lượng: {e}"


def volume_down():
    try:
        pyautogui.press("volumedown")
        return "Đã giảm âm lượng."
    except Exception as e:
        return f"Lỗi giảm âm lượng: {e}"


# =====================================================
# TÌM TAB YOUTUBE
# =====================================================

def get_youtube_tab():

    try:

        url = CHROME_DEBUG_URL + "/json"

        with urllib.request.urlopen(
            url,
            timeout=3
        ) as response:

            tabs = json.loads(
                response.read().decode("utf-8")
            )

        for tab in tabs:

            tab_url = tab.get("url", "")

            if "youtube.com" in tab_url:

                return tab

        return None

    except Exception:

        return None


# =====================================================
# CHẠY JAVASCRIPT TRONG TAB YOUTUBE
# =====================================================

def execute_chrome_javascript(script):

    tab = get_youtube_tab()

    if not tab:

        return (
            None,
            "Không tìm thấy tab YouTube. "
            "Hãy mở Chrome bằng remote debugging "
            "port 9222."
        )

    websocket_url = tab.get(
        "webSocketDebuggerUrl"
    )

    if not websocket_url:

        return (
            None,
            "Không lấy được WebSocket của Chrome."
        )

    try:

        ws = websocket.create_connection(
            websocket_url,
            timeout=5
        )

        command = {
            "id": 1,
            "method": "Runtime.evaluate",
            "params": {
                "expression": script,
                "returnByValue": True
            }
        }

        ws.send(
            json.dumps(command)
        )

        while True:

            response = json.loads(
                ws.recv()
            )

            if response.get("id") == 1:

                ws.close()

                return (
                    response,
                    None
                )

    except Exception as e:

        return (
            None,
            f"Lỗi kết nối Chrome: {e}"
        )


# =====================================================
# YOUTUBE PLAY / PAUSE
# =====================================================

def youtube_play_pause():

    script = """
    (() => {

        const video =
            document.querySelector("video");

        if (!video) {
            return "NO_VIDEO";
        }

        if (video.paused) {

            video.play();

            return "PLAY";

        } else {

            video.pause();

            return "PAUSE";
        }

    })()
    """

    result, error = execute_chrome_javascript(
        script
    )

    if error:
        return error

    return "Đã phát hoặc tạm dừng YouTube."


# =====================================================
# YOUTUBE MUTE
# =====================================================

def youtube_mute():

    script = """
    (() => {

        const video =
            document.querySelector("video");

        if (!video) {
            return "NO_VIDEO";
        }

        video.muted = !video.muted;

        return video.muted;

    })()
    """

    result, error = execute_chrome_javascript(
        script
    )

    if error:
        return error

    return "Đã bật/tắt tiếng YouTube."


# =====================================================
# YOUTUBE TĂNG TỐC
# =====================================================

def youtube_speed_up():

    script = """
    (() => {

        const video =
            document.querySelector("video");

        if (!video) {
            return "NO_VIDEO";
        }

        let speed =
            video.playbackRate + 0.25;

        speed = Math.min(
            speed,
            2.0
        );

        video.playbackRate = speed;

        return speed;

    })()
    """

    result, error = execute_chrome_javascript(
        script
    )

    if error:
        return error

    return "Đã tăng tốc độ YouTube."


# =====================================================
# YOUTUBE GIẢM TỐC
# =====================================================

def youtube_speed_down():

    script = """
    (() => {

        const video =
            document.querySelector("video");

        if (!video) {
            return "NO_VIDEO";
        }

        let speed =
            video.playbackRate - 0.25;

        speed = Math.max(
            speed,
            0.25
        );

        video.playbackRate = speed;

        return speed;

    })()
    """

    result, error = execute_chrome_javascript(
        script
    )

    if error:
        return error

    return "Đã giảm tốc độ YouTube."


# =====================================================
# ĐẶT TỐC ĐỘ YOUTUBE
# =====================================================

def youtube_set_speed(speed):

    try:

        speed = float(speed)

    except (ValueError, TypeError):

        return "Tốc độ không hợp lệ."

    if speed < 0.25 or speed > 2.0:

        return (
            "Tốc độ phải nằm trong khoảng "
            "0.25x đến 2x."
        )

    script = f"""
    (() => {{

        const video =
            document.querySelector("video");

        if (!video) {{
            return "NO_VIDEO";
        }}

        video.playbackRate = {speed};

        return video.playbackRate;

    }})()
    """

    result, error = execute_chrome_javascript(
        script
    )

    if error:
        return error

    return (
        f"Đã đặt tốc độ YouTube "
        f"thành {speed}x."
    )


# =====================================================
# VỀ 1X
# =====================================================

def youtube_normal_speed():

    return youtube_set_speed(1.0)