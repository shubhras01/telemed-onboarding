"""Functions for freshdesk api exposed to other modules."""
import configparser
import json
import requests, os

from logzero import logger

script_path = "."  # os.path.dirname(os.path.abspath(__file__))
config_path = script_path + "/freshdesk_secrets.ini"
config = configparser.ConfigParser()
config.read(config_path)
secrets = config["freshdesk"]
API_KEY = secrets["api_key"]
PASSWORD = secrets["password"]
DOMAIN = secrets["domain"]
API_URL = "https://{}.freshdesk.com/api/v2".format(DOMAIN)
AGENT_TICKET_SCOPE = 1


def check_response(res):
    response = json.loads(res.content)
    if res.status_code == 201:
        logger.info("Contact created successfully.\n {}".format(response))
    else:
        logger.error("Failed to create contact, errors are displayed below,")
        logger.error(response["errors"])


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
    check_response(r)
    return r.status_code


def fetch_groups():
    """Fetch list of all groups in freshdesk."""
    url = API_URL + "/groups"
    r = requests.get(url, auth=(API_KEY, PASSWORD))
    return json.loads(r.content)
