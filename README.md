# multi-llm-demo
A simple multi-agent dialogue simulator using Gemini and DeepSeek LLMs.
一个简单的多智能体对话模拟器，基于 Google Gemini 和 DeepSeek 的大语言模型。

# 功能特点

Agent (LLM, Attribute1, Attribute2, Attribute3, ...)
Prompt
Conversition

- 使用 Agent 类模拟不同身份的角色对话  
- 支持多种 LLM（如 Gemini、DeepSeek）  
- 每个 Agent 拥有角色、性格和私有信息 (Attribute)  
- 根据上下文自动构造 prompt，生成轮流发言内容  
- LLM 的种类和 Agent 拥有的 attribute 都可以自由更改，便于拓展实验和对话模拟  
- 支持多轮对话，保留上下文历史，构建更连贯的多角色交流场景 


## 📦 环境依赖
- Python 3.8+
- 安装依赖：
  pip install google-generativeai openai

  注：现在代码用的agent是 Gemini和Qwen
