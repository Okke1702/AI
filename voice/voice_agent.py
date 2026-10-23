from agent.agent import Agent
from voice.speech import listen


def voice_loop():

    agent = Agent()

    print("=============================")
    print("        MY AI VOICE")
    print("=============================")
    print("Nói lệnh bằng microphone.")
    print("Nói 'thoát' để dừng.\n")

    while True:

        try:

            user_input = listen()

            if not user_input:
                continue

            print("Bạn:", user_input)

            if user_input.lower() in [
                "thoát",
                "dừng",
                "tắt ai"
            ]:
                print("AI: Tạm biệt!")
                break

            response = agent.run(user_input)

            print("AI:", response)
            print()

        except KeyboardInterrupt:

            print("\nAI: Tạm biệt!")
            break

        except Exception as e:

            print("Lỗi Voice:", e)