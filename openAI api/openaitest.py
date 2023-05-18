import openai

openai.api_key = "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"


while True:
    question = input("\n type LEAVE to terminate the chat. \n Whats ur question? ")
    if question.lower() == "leave":
      print("If u have more questions let me know! =D ")
      break
    openaicomp = openai.Completion.create(engine="text-davinci-003",
                                          prompt= question,
                                          max_tokens = 3160)
    print(openaicomp.choices[0].text)