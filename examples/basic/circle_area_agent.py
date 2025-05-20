import asyncio
from math import pi

from agents import Agent, Runner, function_tool


@function_tool
def area_of_circle(radius: float) -> float:
    """Return the area of a circle given its radius."""
    return pi * radius**2


async def main() -> None:
    agent = Agent(
        name="Area Assistant",
        instructions="Use the area_of_circle tool to compute areas when asked.",
        tools=[area_of_circle],
    )

    result = await Runner.run(agent, "What is the area of a circle with radius 5?")
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
