# multi-llm-demo
A simple multi-agent dialogue simulator using Gemini and Qwen LLMs.

一个简单的多智能体对话模拟器，基于 Google Gemini 和 Qwen 的大语言模型。

# 项目简介
项目旨在模拟多个智能体（Agent）围绕某一话题展开的对话流程。

每个 Agent 拥有：
- 明确的角色定位（如“教授”或“学生”）
- 独立的个性描述（如“温和”“直接”）
- 私有信息（如“你不喜欢吃辣”）
- 可选择使用不同的 LLM 后端进行推理（Gemini / Qwen）

系统通过拼接公共信息、对话历史与 Agent 私有信息构造 prompt，引导每个智能体依次发言，形成多轮完整的模拟对话流程。该设计特别适合用来：
- 比较多种 LLM 在相同上下文下的响应差异
- 分析对话中角色扮演与信息隐含的效果
- 构建教学场景、决策模拟、角色扮演训练等应用原型

## ✨ 功能特点
- 使用 Agent 类模拟不同身份的角色对话  
- 支持多种 LLM（如 Gemini、Qwen）  
- 每个 Agent 拥有角色、性格和私有信息  
- 根据上下文自动构造 prompt，生成轮流发言内容  
- LLM 的种类/ Agent的数量/ 对话的轮数/ Agent 拥有的 attribute 都可以自由更改，便于拓展实验和对话模拟  
- 支持多轮对话，保留上下文历史，构建更连贯的多角色交流场景  

## 📦 环境依赖
- Python 3.8+
- 安装依赖：
  pip install google-generativeai openai

## 🖼️ 示例场景：午餐选择讨论
公共信息：  
大家要一起点午餐，可选项有：和声书院食堂外送、麦当劳、披萨。

角色设置：
- Tom（教授）| 性格：温和 | 私人信息：你不喜欢吃辣的
- Jimmy（学生）| 性格：直接 | 私人信息：你想吃得健康

示例输出：

 第 1 轮讨论
 
Tom：同学们，大家好。看来午餐的选择已经有了几个方向了，和声书院食堂外送、麦当劳和披萨，都是不错的选择。大家还有没有其他的提议呢？如果没有的话，我们可以开始讨论一下，看看哪个更符合大家的口味和需求。我个人对辣的食物不太适应，希望选择的时候可以稍微考虑一下。

Jimmy：嘿，Tom，我觉得你说得很对。我们确实要考虑到每个人的口味。说到吃，我其实更倾向于健康饮食。我觉得和声书院食堂外送可能会有更多健康的选项，比如蔬菜沙拉和瘦肉，这些对我来说更好。麦当劳和披萨虽然好吃，但总感觉不太健康。你们怎么看？

 第 2 轮讨论
 
Tom：Jimmy说得很有道理，健康确实很重要。和声书院食堂外送的健康选项确实是一个优势。我个人也比较倾向于食堂外送，主要是因为可以避开一些过于油腻或者辛辣的食物。 
不过，我们也可以看看和声食堂外送的具体菜单，了解一下都有哪些菜品可以选择。这样大家可以更清楚地知道是否符合自己的口味和健康需求。或者，我们可以比较一下，麦当劳和披萨有没有相对健康一些的选择，比如麦当劳的沙拉或者披萨的蔬菜口味，等等。 
大家觉得呢？我们先看看菜单或者选项，再做决定，好吗？

Jimmy：好主意，Tom！看看具体菜单会更有帮助。我个人肯定会选食堂的沙拉或者鸡胸肉。不过，也理解有些人可能更喜欢麦当劳的沙拉或者蔬菜披萨。我们先把菜单看一下，然后再投票决定吧。这样既考虑到了健康，也能尊重大家的个人喜好。
