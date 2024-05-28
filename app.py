import os
from mattermostdriver import Driver

def main():
    driver = Driver({
        'url': os.environ.get('https://mattermost.com/?utm_source=bing&utm_medium=cpc&utm_campaign=Bing_Brand_EMEA&utm_adgroup&utm_term=mattermost&utm_content&msclkid=46528f753e2e19c1ec7fe9209e579ad1', 'localhost'),
        # 'login_id': os.environ.get('MATTERMOST_LOGIN_ID', 'your-email'),
        # 'password': os.environ.get('MATTERMOST_PASSWORD', 'your-password'),
        'scheme': 'http',
        'port': 8065,
        'basepath': '/api/v4',
        'verify': True,
        'timeout': 30,
    })

    driver.login()

    # Send a message to a channel
    driver.posts.create_post({
        'channel_id': os.environ.get('MATTERMOST_CHANNEL_ID', 'your-channel-id'),
        'message': 'Hello from Python!'
    })

if __name__ == "__main__":
    main()

