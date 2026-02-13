import json

from langchain.agents import create_agent
from langchain.agents.middleware import HumanInTheLoopMiddleware
from langchain.tools import tool
from langgraph.checkpoint.memory import InMemorySaver


@tool
def write_file(filename: str, content: str) -> str:
    """Write content to a file."""
    with open(filename, "w") as f:
        f.write(content)
    return f"Successfully wrote to {filename}"

@tool
def propose_plan(task: str, steps: list[str]) -> str:
    """Propose an execution plan for a complex task. Returns the plan for review."""
    plan = {"task": task, "steps": steps}
    return json.dumps(plan, ensure_ascii=False, indent=2)

@tool
def execute_step(step: str) -> str:
    """Execute a single step of the plan."""
    # 实际执行逻辑
    return f"✅ 完成：{step}"

agent = create_agent(
    model="deepseek-chat",
    tools=[propose_plan, execute_step],
    middleware=[
        HumanInTheLoopMiddleware(
            interrupt_on={
                # Plan 需要审批，允许编辑
                "propose_plan": {
                    "allowed_decisions": ["approve", "edit", "reject"],
                    "description": "📋 执行计划待确认",
                },
                # 单步执行不需要审批（Plan 已经批过了）
                "execute_step": False,
            },
        ),
    ],
    checkpointer=InMemorySaver(),
)