# 환경변수 로딩
from dotenv import load_dotenv
load_dotenv()

# 모델 초기화
from langchain.chat_models import init_chat_model
model = init_chat_model("gpt-4o-mini", model_provider="openai")

from langchain_core.messages import HumanMessage

response = model.invoke([HumanMessage(content="Hi! I'm Bob")])
print(response)