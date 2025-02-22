# LangChain (랭체인) 실습
from dotenv import load_dotenv

load_dotenv()

from langchain.chat_models import init_chat_model

# openai 의 gpt-4o-mini 모델을 사용하겠다.
model = init_chat_model("gpt-4o-mini", model_provider="openai")

from langchain_core.messages import HumanMessage, SystemMessage

messages = [
    SystemMessage("Translate the following from English into Italian"),
    HumanMessage("hi!"),
]
# print(model.invoke(messages))

# for token in model.stream(messages):
#     print(token.content, end="|")

from langchain_core.prompts import ChatPromptTemplate

system_template = "Translate the following from English into {language}"

prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)

prompt = prompt_template.invoke({"language": "Korean", "text": "hi!"})
response = model.invoke(prompt)
print(response.content)