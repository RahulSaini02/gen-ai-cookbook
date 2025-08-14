from strands import tool
from nova_act import NovaAct


@tool
def run_tracking_tool(starting_url: str, tracking_id: str) -> str:
    """
    With starting url, automates tasks in browser based on instructions provided. Can run multiple sessions in parallel.
    The tool can do some reasoning of its own but can sometimes not give good results when you ask complex tasks.

    Args:
        starting_url (str): The website url to perform actions on
        instr (str): the instruction in natural language to be sent to the browser for the task to be performed

    Returns:
        str: The result of the action performed.
    """
    instr = f"""
    1. Locate the input field for tracking ID.
    2. Type {tracking_id} into the input box and click Track.
    3. Wait until text 'Status' or 'Delivered' appears. If page is blank, reload the page.
    4. Extract status, date, time, location in JSON format.
    """

    with NovaAct(starting_page=starting_url) as nova:
        return nova.act(instr)
