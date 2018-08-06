from webhook import WEBHOOK
# WEBHOOK = "https://hooks.slack.com/services/your-private-channel-id"

HTTP_OK = 200

# Number of seconds to sleep between each GET call.
# INITIAL_DELAY = 5 * 60  # 5 minutes
INITIAL_DELAY = 30
BACKOFF = 2

# The web sites to monitor.
URLS = [
    'http://localhost:8000/api/quicktest',
    'http://www.google.com',
    'http://www.yahoo.com',
]


