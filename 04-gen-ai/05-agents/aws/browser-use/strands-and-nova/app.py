from strands import Agent
from nova_act_agent import run_tracking_tool
from pydantic import BaseModel
from dotenv import load_dotenv
import json

load_dotenv()


class TrackingResult(BaseModel):
    status: str
    date: str
    time: str
    location: str


agent = Agent(tools=[])

tracking_id = "9400150105796009472614"
website_url = "https://tools.usps.com/go/TrackAction"

tool_output = run_tracking_tool(tracking_id=tracking_id, starting_url=website_url)
result = agent.structured_output(TrackingResult, tool_output)

with open("tracking.json", "w") as f:
    json.dump(result.model_dump(), f, indent=2)
