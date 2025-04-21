import os
os.environ["OPENAI_API_KEY"] = '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'


from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chat_models import ChatOpenAI

callback = StreamingStdOutCallbackHandler()

chatgpt = ChatOpenAI(
    model_name='gpt-4o-mini',
    streaming=True,
    callbacks=[callback],
    temperature=0
)

user_input = input("질문을 입력하세요: ")
answer = chatgpt.predict(user_input)
print("답변\n", answer)