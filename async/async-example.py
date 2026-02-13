#!/usr/bin/env python3

import asyncio
import time

# 定义一个异步函数
async def say_after(delay, what):
    """等待指定时间后打印消息"""
    await asyncio.sleep(delay)  # 等待指定时间，不会阻塞事件循环
    print(what)

# 定义主异步函数
async def main():
    """主异步函数，演示异步操作"""
    print(f"程序开始于: {time.strftime('%X')}")
    
    # 并发执行两个异步任务
    task1 = asyncio.create_task(say_after(1, "Hello"))  # 创建第一个任务
    task2 = asyncio.create_task(say_after(2, "World"))  # 创建第二个任务
    
    print(f"任务创建完成于: {time.strftime('%X')}")
    
    # 等待两个任务完成
    await task1
    await task2
    
    print(f"程序结束于: {time.strftime('%X')}")

# 运行主异步函数
if __name__ == "__main__":
    asyncio.run(main())