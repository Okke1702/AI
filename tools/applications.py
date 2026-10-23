import subprocess


APPLICATIONS = {
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
}


def open_application(app_name):
    app_name = app_name.lower().strip()

    if app_name not in APPLICATIONS:
        return f"Không được phép mở ứng dụng: {app_name}"

    try:
        subprocess.Popen([APPLICATIONS[app_name]])
        return f"Đã mở {app_name}."

    except Exception as e:
        return f"Lỗi khi mở {app_name}: {e}"