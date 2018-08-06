"""
monitor.py
A slack bot
Do a GET on each given URL and post a slack message when an error occurs.
"""
import requests, time
from settings import BACKOFF, HTTP_OK, INITIAL_DELAY, URLS, WEBHOOK


def slack_message(msg):
    """ Post this message to the slack webhook link."""
    print(msg)
    response = requests.post(
        WEBHOOK,
        json = {"text" : msg},
    )
    if response.status_code != HTTP_OK:
        print(
            "Error posting slack message : HTTP {} : {}".format(
                response.status_code,
                msg
            )
        )


def check_url(url):
    """ GET the url. Send slack msg if an error occurs. Return True is all is good."""
    try:
        response = requests.get(url)
        if response.status_code != HTTP_OK:
            slack_message(msg="Error {} {}".format(response.status_code, url))
        else:
            return True
    except:
        slack_message(msg="Exception {}".format(url))
    return False


if __name__ == '__main__':
    delay = INITIAL_DELAY
    while(True):
        get_success = True
        for url in URLS:
            if not check_url(url=url):
                if get_success:
                    get_success = False
                    # Increase the sleep time after an error is found.
                    delay = delay * BACKOFF
        # If all urls were successful, reset the delay back to initial value.
        if get_success:
            delay = INITIAL_DELAY
        time.sleep(delay)
