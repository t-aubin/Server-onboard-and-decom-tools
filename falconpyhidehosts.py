import sys
from falconpy import Hosts

# To use python hide_host.py <hostname> <client_secret>

# Replace this with your Client ID (assumes it's static)
CLIENT_ID = "your_client_id"

def hide_host(device_hostname, client_secret):
    """Check if a host exists in CrowdStrike and hide it."""
    try:
        # Initialize the Hosts API
        falcon = Hosts(client_id=CLIENT_ID, client_secret=client_secret)
        
        # Search for the host by hostname
        response = falcon.query_devices_by_filter(filter=f"hostname:'{device_hostname}'")
        if response["status_code"] != 200:
            raise Exception(f"API Error: {response.get('errors', 'Unknown error')}")

        # Get device IDs from the response
        device_ids = response.get("body", {}).get("resources", [])
        if not device_ids:
            print("Host not in CrowdStrike")
            return

        # Hide the host(s)
        hide_response = falcon.perform_action(action_name="hide_host", ids=device_ids)
        if hide_response["status_code"] == 200:
            print("Success")
        else:
            print("Host not in CrowdStrike")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Check if correct arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python script.py <hostname> <client_secret>")
        sys.exit(1)

    # Parse command-line arguments
    hostname_to_hide = sys.argv[1]
    client_secret = sys.argv[2]

    # Execute the hide host function
    hide_host(hostname_to_hide, client_secret)
