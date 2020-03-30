"""Functions for freshdesk api exposed to other modules."""
import configparser
import json
import requests

from logzero import logger

config = configparser.ConfigParser()["freshdesk"]
config.read("freshdesk_secrets.ini")
API_KEY = config["api_key"]
PASSWORD = config["password"]
DOMAIN = config["domain"]
API_URL = "https://{}.freshdesk.com/api/v2".format(DOMAIN)
AGENT_TICKET_SCOPE = 1


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
    return response


def create_user_agent(doctor):
    """Create a agent in freshdesk from doctor object.

    Args:
        doctor (onboarding.models.Doctor)

    Returns:
        response from api (dict)

    """
    agent_data = {
        "email": doctor.email,
        "name": doctor.full_name,
        "mobile": doctor.contact_number,
        "language": doctor.language,
        "ticket_scope": AGENT_TICKET_SCOPE,
    }
    return create_agent(agent_data)
