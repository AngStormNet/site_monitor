HTTP_OK = 200

# Number of seconds to sleep between each GET call.
INITIAL_DELAY = 5 * 60  # 5 minutes
INITIAL_DELAY = 30

# The web sites to monitor.
URLS = [
    'http://localhost:8000/api/quicktest',
    'http://www.google.com',
    'http://www.yahoo.com',
]

WEBHOOK = "https://hooks.slack.com/services/your-slack-bot-setup"
