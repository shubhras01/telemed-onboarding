"""Functions for freshdesk api exposed to other modules."""
import configparser
import json
import requests

from logzero import logger

config = configparser.ConfigParser()['freshdesk']
config.read('freshdesk_secrets.ini')
API_KEY = config['api_key']
PASSWORD = config['password']
DOMAIN = config['domain']
API_URL = "https://{}.freshdesk.com/api/v2".format(DOMAIN)


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
    logger.info(r)
    if r.status_code == 201:
        logger.info(
            "Contact created successfully."
        )
    else:
        logger.error("Failed to create contact, errors are displayed below,")
        response = json.loads(r.content)
        logger.error(response["errors"])
