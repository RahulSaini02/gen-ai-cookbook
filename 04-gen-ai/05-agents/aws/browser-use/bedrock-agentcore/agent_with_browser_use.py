from browser_use import Agent
from browser_use.browser.session import BrowserSession
from bedrock_agentcore.tools.browser_client import BrowserClient
from browser_use.browser import BrowserProfile
from langchain_aws import ChatBedrockConverse
from rich.console import Console
from contextlib import suppress
import argparse
import asyncio
from boto3.session import Session

console = Console()

boto_session = Session()
region = boto_session.region_name or "us-west-2"


async def run_browser_task(
    browser_session: BrowserSession, bedrock_chat: ChatBedrockConverse, task: str
) -> None:
    """
    Run a browser automation task using browser_use

    Args:
        browser_session: Existing browser session to reuse
        bedrock_chat: Bedrock chat model instance
        task: Natural language task for the agent
    """
    try:
        # Show task execution
        console.print(f"\n[bold blue]🤖 Executing task:[/bold blue] {task}")

        # Create and run the agent
        agent = Agent(task=task, llm=bedrock_chat, browser_session=browser_session)

        # Run with progress indicator
        with console.status(
            "[bold green]Running browser automation...[/bold green]", spinner="dots"
        ):
            await agent.run()

        console.print("[bold green]✅ Task completed successfully![/bold green]")

    except Exception as e:
        console.print(f"[bold red]❌ Error during task execution:[/bold red] {str(e)}")
        import traceback

        if console.is_terminal:
            traceback.print_exc()


async def agent_with_browser_use(prompt: str, region: str = "us-west-2"):
    """
    Main function that demonstrates browser use with Agent automation.

    Workflow:
    1. Creates Amazon Bedrock AgentCore browser client in us-west-2 region
    2. Waits for browser initialization (10-second required delay)
    """
    try:
        # Step 1: Create browser session
        client = BrowserClient(region)
        client.start()

        # Extract ws_url and headers
        ws_url, headers = client.generate_ws_headers()

        # Create persistent browser session and model
        browser_session = None
        bedrock_chat = None

        try:
            # Create browser profile with headers
            browser_profile = BrowserProfile(
                headers=headers,
                timeout=1500000,  # 150 seconds timeout
            )

            # Create a browser session with CDP URL and keep_alive=True for persistence
            browser_session = BrowserSession(
                cdp_url=ws_url,
                browser_profile=browser_profile,
                keep_alive=True,  # Keep browser alive between tasks
            )

            # Initialize the browser session
            console.print("[cyan]🔄 Initializing browser session...[/cyan]")
            await browser_session.start()

            # Create ChatBedrockConverse once
            bedrock_chat = ChatBedrockConverse(
                model_id="anthropic.claude-3-5-sonnet-20240620-v1:0",
                region_name=region,
            )

            console.print(
                "[green]✅ Browser session initialized and ready for tasks[/green]\n"
            )

            task = prompt

            await run_browser_task(browser_session, bedrock_chat, task)

        finally:
            # Close the browser session
            if browser_session:
                console.print("\n[yellow]🔌 Closing browser session...[/yellow]")
                with suppress(Exception):
                    await browser_session.close()
            console.print("[green]✅ Browser session closed[/green]")

    except Exception as e:
        console.print(f"\n[red]Error: {e}[/red]")
        import traceback

        traceback.print_exc()

    finally:
        console.print("\n\n[yellow]Shutting down...[/yellow]")
        if "client" in locals():
            client.stop()
            console.print("✅ Browser session terminated")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--prompt", required=True, help="Browser Search instruction")
    parser.add_argument("--region", default="us-west-2", help="AWS region")
    args = parser.parse_args()

    asyncio.run(agent_with_browser_use(args.prompt, args.region))
