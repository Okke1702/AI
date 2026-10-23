import os
import sys


# =========================================================
# PATH CỦA PROJECT
# =========================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

SITE_PACKAGES = os.path.join(
    BASE_DIR,
    ".venv",
    "Lib",
    "site-packages"
)


# =========================================================
# NVIDIA CUDA DLL
# =========================================================

NVIDIA_PATH = os.path.join(
    SITE_PACKAGES,
    "nvidia"
)

CUDA_PATHS = [
    # CUBLAS
    os.path.join(
        NVIDIA_PATH,
        "cublas",
        "bin"
    ),

    # cuDNN
    os.path.join(
        NVIDIA_PATH,
        "cudnn",
        "bin"
    ),

    # CUDA NVRTC
    os.path.join(
        NVIDIA_PATH,
        "cuda_nvrtc",
        "bin"
    ),
]


# =========================================================
# LOAD CUDA DLL PATH
# =========================================================

if sys.platform == "win32":

    for path in CUDA_PATHS:

        if os.path.isdir(path):

            # Python 3.8+
            try:
                os.add_dll_directory(path)
            except Exception:
                pass

            # Thêm vào PATH của process hiện tại
            os.environ["PATH"] = (
                path
                + os.pathsep
                + os.environ.get("PATH", "")
            )


# =========================================================
# IMPORT WHISPER
# =========================================================

from faster_whisper import WhisperModel


# =========================================================
# CONFIG
# =========================================================

MODEL_SIZE = "small"

SAMPLE_RATE = 16000

LANGUAGE = "vi"


# =========================================================
# LOAD WHISPER MODEL
# =========================================================

print("Đang tải Whisper...")

try:

    model = WhisperModel(
        MODEL_SIZE,
        device="cuda",
        compute_type="float16"
    )

    print("Whisper CUDA: OK")

except Exception as e:

    print("Lỗi khi tải Whisper:")
    print(e)

    raise


# =========================================================
# LISTEN
# =========================================================

def listen():

    import sounddevice as sd
    import numpy as np

    print()
    print("🎤 Đang nghe...")

    duration = 5

    try:

        audio = sd.rec(
            int(duration * SAMPLE_RATE),
            samplerate=SAMPLE_RATE,
            channels=1,
            dtype="float32"
        )

        sd.wait()

    except Exception as e:

        print("Lỗi microphone:")
        print(e)

        return ""


    # Chuyển audio thành 1 chiều

    audio = np.squeeze(audio)


    # =====================================================
    # WHISPER TRANSCRIBE
    # =====================================================

    try:

        segments, info = model.transcribe(
            audio,
            language=LANGUAGE,
            beam_size=5
        )

        text = ""

        for segment in segments:

            text += segment.text

        text = text.strip()

        print("Bạn nói:", text)

        return text


    except Exception as e:

        print("Lỗi Whisper:")
        print(e)

        return ""