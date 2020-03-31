"""Functions for freshdesk api exposed to other modules."""
import configparser
import json
import requests

from logzero import logger

config = configparser.ConfigParser()
config.read("freshdesk_secrets.ini")
secrets = config["freshdesk"]
API_KEY = secrets["api_key"]
PASSWORD = secrets["password"]
DOMAIN = secrets["domain"]
API_URL = "https://{}.freshdesk.com/api/v2".format(DOMAIN)
AGENT_TICKET_SCOPE = 1
print(API_URL)

def create_agent(agent_data):
    """Create a new agent on freshdesk portal.

    Args:
        agent_data (dict): Dictionary with user details.
            `email` and `ticket_scope` are required fields.

    """
    url = API_URL + "/agents"
    headers = {"Content-Type": "application/json"}
    json_data = json.dumps(agent_data)
    r = requests.post(url, auth=(API_KEY, PASSWORD), data=json_data, headers=headers)
    response = json.loads(r.content)
    if r.status_code == 201:
        logger.info("Contact created successfully.\n {}".format(response))
    else:
        logger.error("Failed to create contact, errors are displayed below,")
        logger.error(response["errors"])
    return r.status_code

