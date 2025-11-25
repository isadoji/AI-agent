import click
from agent import show_python_code_and_result, root_agent
from google.adk.runners import InMemoryRunner
import asyncio

@click.command()
@click.argument("query", type=str)
def run_code(query):
    runner = InMemoryRunner(agent=root_agent)
    response = asyncio.run(runner.run(query))  # <-- Usa run(query)
    show_python_code_and_result(response)

if __name__ == "__main__":
    run_code()

