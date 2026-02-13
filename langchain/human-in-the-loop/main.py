from langchain.agents import create_agent
from langchain.agents.middleware import HumanInTheLoopMiddleware
from langchain.tools import tool
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.types import Command
from dotenv import load_dotenv

load_dotenv("../.env")

# 定义一个“危险”的工具
@tool
def write_file(filename: str, content: str) -> str:
    """Write content to a file."""
    with open(filename, "w") as f:
        f.write(content)
    return f"Successfully wrote to {filename}"

# 用 1.0 提供的新 API `create_agent`，创建一个 ReAct Agent
agent = create_agent(
    model="deepseek-chat",
    # 挂载 `write_file` 工具
    tools=[write_file],
    # 挂载 Human-in-the-Loop Middleware
    middleware=[
        HumanInTheLoopMiddleware(
            interrupt_on={
                "write_file": True,  # `write_file` 工具每次执行都需要审批
            },
            description_prefix="⚠️ 文件操作需要审批",  # 消息的前缀
        ),
    ],
    checkpointer=InMemorySaver(),
)

def main():
    # 重点：必须指定一个唯一的 `thread_id`，推荐使用 UUID 或 NanoID
    # 否则用户反馈后，无法 `resume` 回原来的 Thread
    config = {"configurable": {"thread_id": "demo-001"}}
    
    # 首次执行 Agent 的 `demo-001` Thread：
    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "帮我创建一个 hello.txt，内容是 Hello World",
                }
            ]
        },
        config=config,
    )

    # 检查是否触发了中断
    if "__interrupt__" in result:
        interrupt = result["__interrupt__"][0]
        # 可能不止一个需要审批的操作：
        for action in interrupt.value["action_requests"]:
            print(action["description"])
            print(f"   工具: {action['name']}")
            print(f"   参数: {action['args']}")

        # 模拟审批（实际场景中这里会是一个 UI 或 API）
        decision = input("输入决策 (approve/reject): ")

        # 带上用户反馈，再次 Resume 并执行 Agent 的 `demo-001` Thread：
        if decision == "approve":
            final_result = agent.invoke(
                Command(resume={"decisions": [{"type": "approve", "message": "允许"}]}),
                config=config,
            )
            print("✅ 操作已执行")
            final_result["messages"][-1].pretty_print()
        else:
            agent.invoke(
                Command(
                    resume={
                        "decisions": [{"type": "reject", "message": "不允许创建文件"}]
                    }
                ),
                config=config,
            )
            print("❌ 操作已拒绝")

if __name__ == "__main__":
    main()
