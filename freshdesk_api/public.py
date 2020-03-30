"""Functions for freshdesk api exposed to other modules."""

import requests
import json

from logzero import logger

from constants import API_KEY, API_URL


def create_agent(agent_data):
    """Create a new agent on freshdesk portal.

    Args:
        agent_data (dict): Dictionary with user details.

    """
    url = API_URL + "/agents"
    headers = {"Content-Type": "application/json"}
    json_data = json.dumps(agent_data)
    r = requests.post(url, auth=(API_KEY, ), data=json_data, headers=headers)

    if r.status_code == 201:
        logger.info(
            "Contact created successfully, the response is given below" + r.content
        )
    else:
        logger.error("Failed to create contact, errors are displayed below,")
        response = json.loads(r.content)
        logger.erro(response["errors"])
