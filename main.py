from agent.agent import Agent


agent = Agent(max_steps=10)


print("=============================")
print("          MY AI")
print("=============================")
print("Gõ 'exit' để thoát.\n")


while True:

    user_input = input("Bạn: ")

    if user_input.lower() == "exit":

        print("AI: Tạm biệt!")

        break


    try:

        response = agent.run(user_input)

        # Agent đã in câu trả lời rồi
        # nên ở đây không cần print lại


    except Exception as e:

        print("Có lỗi xảy ra:", e)
        print()