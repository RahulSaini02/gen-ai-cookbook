# 🤖 05-agents: Building Autonomous and Tool-Using AI Agents

This module explains how to build, understand, and deploy **AI agents** — intelligent LLM-driven systems that reason, use tools, and interact autonomously or semi-autonomously.

---

## 🧠 What is an Agent?

An agent is more than a chatbot. It's an LLM that can:
- **Reason** step-by-step (ReAct)
- **Use tools** (APIs, calculators, retrievers)
- **Remember context** (memory)
- **Act autonomously** toward goals

---

## 📂 Folder Structure

```
05-agents/
├── 01_intro_to_agents.md              # What are agents? ReAct, tools, loops
├── 02_react_framework.ipynb          # ReAct prompt loop (Think → Act → Observe)
├── 03_langchain_agents.ipynb         # Tool-using agents using LangChain
├── 04_memory_and_context.ipynb       # Adding memory: summary, buffer, vector
├── 05_multitool_agent.ipynb          # Use multiple tools (search + calc + DB)
├── 06_eval_and_debug.ipynb           # Debugging agent chains, cost tracking
├── 07_planner_executor_agents.ipynb  # Planner + executor separation
├── 08_langgraph_multi_agent.ipynb    # Multi-agent flow using LangGraph
├── assets/                           
├── README.md
```

---

## 📘 Learning Goals

- Understand the anatomy of an agent (LLM, tools, memory, loop)
- Implement ReAct and planner-executor agent flows
- Use LangChain or LangGraph to create modular agent logic
- Add memory to agents (short/long term)
- Evaluate agent performance and debug step-by-step

---

## 🛠️ Topics Covered

- ReAct framework and custom prompts
- LangChain agent creation
- Tool definition and action parsing
- Using OpenAI tools or custom Python functions
- Working with multi-step agent workflows
- Evaluation, error tracing, and token cost tracking

---

## 📚 References

- LangChain Docs: [https://docs.langchain.com](https://docs.langchain.com)
- LangGraph Bootcamp: [https://www.udemy.com/course/complete-agentic-ai-bootcamp-with-langgraph-and-langchain](https://www.udemy.com/course/complete-agentic-ai-bootcamp-with-langgraph-and-langchain)

---

## 🧪 Example Use Cases

- Research Assistant: Search → Summarize → Cite
- Data Analyst Agent: Upload CSV → Answer queries → Chart outputs
- Autonomous Agent: Create blog ideas → Research → Draft content


# Resources

- [What are AI Agents](https://youtu.be/F8NKVhkZZWI?si=__0D-tp8qpKzyscb)
- [AI Agents Fundamentals](https://youtu.be/qU3fmidNbJE?si=qpqsUZdMW7d1Ou-j)
- [ReAct with LangChain](https://youtu.be/Eug2clsLtFs?si=PFcNbGYwxk-p-fCF)
- [Building AI Agents](https://youtu.be/_Udb5NC6vTI?si=xiLvR_hCBC-pM7A8)
- [Building AI Agent: Step by Step](https://www.youtube.com/live/8QQjOSB0ERo?si=ADRXSpxxYbS71YjG)
- 