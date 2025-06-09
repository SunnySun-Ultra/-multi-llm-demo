import google.generativeai as genai
from openai import OpenAI

# 初始化 Gemini 模型
genai.configure(api_key="Key1")
model = genai.GenerativeModel("gemini-2.0-flash")

# 初始化 Qwen 客户端
qwen_client = OpenAI(
    api_key="Key2",
    base_url="https://api.siliconflow.cn/v1"
)

# 定义 Agent 类
class Agent:
    def __init__(self, name, role, private_info, personality, llm_type="gemini"):
        self.name = name
        self.role = role
        self.private_info = private_info
        self.personality = personality
        self.llm_type = llm_type
        self.memory = []

    def generate_prompt(self, public_info, conversation_history):
        prompt = f"""你是 {self.name}，你的角色是 {self.role}。
你的性格是 {self.personality}。
已知的公共信息：{public_info}
你的私有信息：{self.private_info}

以下是当前对话记录：
{conversation_history}

请你作为该角色继续下一轮发言："""
        return prompt

    def speak(self, gemini_model, qwen_client, public_info, conversation_history):
        prompt = self.generate_prompt(public_info, conversation_history)
        if self.llm_type == "gemini":
            response = gemini_model.generate_content(prompt)
            text = response.text.strip()
        elif self.llm_type == "qwen":
            response = qwen_client.chat.completions.create(
                model="Qwen/Qwen2.5-72B-Instruct",
                messages=[{"role": "user", "content": prompt}]
            )
            text = response.choices[0].message.content.strip()
            if text.startswith(f"{self.name}：") or text.startswith(f"{self.name}:"):
                text = text[len(self.name)+1:].lstrip()
        else:
            text = ""
        if text.startswith(f"{self.name}：") or text.startswith(f"{self.name}:"):
            text = text[len(self.name)+1:].lstrip()
        return text

# 设置 Agent 列表
agents = [
    Agent("Tom", "教授", "你不喜欢吃辣的", "温和", "gemini"),
    Agent("Jimmy", "学生", "你想吃得健康", "直接", "qwen")
]

# 公共信息
public_info = "大家要一起点午餐，可选项有：和声书院食堂外送、麦当劳、披萨。"
conversation = ""

# 模拟一轮对话
for round_num in range(2):
    print(f"\n🔁 第 {round_num+1} 轮讨论")
    for agent in agents:
        response = agent.speak(model, qwen_client, public_info, conversation)
        print(f"{agent.name}：{response}")
        conversation += f"\n{agent.name}：{response}"
