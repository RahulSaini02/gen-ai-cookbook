from pydantic import BaseModel
from strands import Agent, tool
from nova_act import NovaAct
from dotenv import load_dotenv
import json

load_dotenv()


class TrackingResult(BaseModel):
    status: str
    date: str
    time: str
    location: str


@tool
def usps_track(tracking_id: str, url: str) -> dict:
    with NovaAct(starting_page=url) as nova:
        nova.act("Locate the tracking input box and type the tracking number")
        nova.act(f"Type {tracking_id} into the input box and click Track")
        nova.act(
            "Wait until 'Status' or 'Delivered' appears on the page, if blank reload"
        )
        res = nova.act(
            "Extract tracking update: status, date, time, location",
            schema=TrackingResult.model_json_schema(),
        )
    if not res.matches_schema:
        raise ValueError("Failed schema validation: {res=}")
    return res.parsed_response


if __name__ == "__main__":
    tracking_id = "9400150105796009472614"
    website_url = "https://tools.usps.com/go/TrackAction"

    agent = Agent(
        system_prompt="Use the usps_track tool to fetch tracking info",
        tools=[usps_track],
    )

    output: TrackingResult = agent.structured_output(
        TrackingResult,
        f"Please fetch the USPS tracking information for tracking id: {tracking_id} in the webiste: {website_url}",
    )

    with open("tracking.json", "w") as f:
        json.dump(output.model_dump(), f, indent=2)
