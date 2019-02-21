import json
import os


def try_get(object, key):
    """Tries to get the value of a key in an object, and politely notifies you if it cannot find it."""

    if key not in object:
        raise KeyError("Could not find " + key + " inside of " + object + "! Does it exist?")

    return object[key]


class Config:
    """Holds configuration information like filepaths, keys, etc."""

    # Filename of secrets file.
    SECRETS_FILE_NAME = "secrets.json"

    # Path to secrets file.
    SECRETS_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), SECRETS_FILE_NAME)

    # Does it exist?
    if not os.path.exists(SECRETS_PATH):
        raise IOError(
            "Could not find the file {0} located at {1}. Did you read the README?".format(SECRETS_FILE_NAME,
                                                                                          SECRETS_PATH))

    # Load secrets JSON into dictlike object.

    with open(SECRETS_PATH) as file:
        _json_object = json.load(file)

    # Twitter username.
    TWITTER_HANDLE = try_get(_json_object, 'twitter_handle')

    # Twitter API keys.
    CONSUMER_KEY = try_get(_json_object, 'consumer_key')
    CONSUMER_SECRET = try_get(_json_object, 'consumer_secret')
    ACCESS_TOKEN = try_get(_json_object, 'access_token')
    ACCESS_TOKEN_SECRET = try_get(_json_object, 'access_token_secret')