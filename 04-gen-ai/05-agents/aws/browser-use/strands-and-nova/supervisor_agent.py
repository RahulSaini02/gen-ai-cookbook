import nova_act_agent
from strands import Agent
from dotenv import load_dotenv
import json

load_dotenv()

if __name__ == "__main__":
    tracking_id = "9400150105796009472614"
    website_url = "https://tools.usps.com/go/TrackAction"

    # Ask the agent a question that uses the available tools
    message = f"""
    I have these requests. You can run things in parallel to speed up analysis if you find it appropriate. 

    1. Locate input field for tracking ID. 
    2. Type {tracking_id} into the input box and click Track.
    3. Wait until text 'Status' or 'Delivered' appears on the page. If you see and blank page, reload the page.
    4. Extract the tracking update: status, date, time, and location.
    5. Format into json
    """

    agent = Agent(
        tools=[
            nova_act_agent.browser_automation_tool(
                starting_url=website_url, instr=message
            )
        ]
    )
