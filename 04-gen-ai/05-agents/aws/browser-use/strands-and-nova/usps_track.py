from dotenv import load_dotenv

load_dotenv()

from nova_act import NovaAct

tracking_id = "9400150105796009472614"
website_url = "https://tools.usps.com/go/TrackAction"

with NovaAct(starting_page=website_url) as nova:
    nova.start()

    # Step-by-step instructions for clarity and reliability
    nova.act("Locate input field for tracking ID.")
    nova.act(f"Type {tracking_id} into the input box and click Track.")
    nova.act("Wait until text 'Status' or 'Delivered' appears on the page.")

    nova.act(
        "Extract the most recent tracking update: status, date, time, and location."
    )
    nova.act(
        """Format the extracted information into the following JSON structure:
        {
            "status": "<Current package status>",
            "date": "<Date of the latest update>",
            "time": "<Time of the latest update>",
            "location": "<Location of the latest update>"
        }"""
    )

    nova.stop()
