# Twitter Trends Scraper

This project is a web scraper that logs into Twitter (now known as X), fetches the top trending topics, and stores them in a MongoDB database.

## Features

- Logs into Twitter using Selenium WebDriver.
- Fetches the top 5 trending topics.
- Stores the trending topics in a MongoDB database with a unique ID and timestamp.
- Uses a proxy server to avoid IP blocking.
- Automatically handles Twitter login flow.

## Prerequisites

- Python 3.x
- Selenium
- ChromeDriver
- MongoDB
- Git
- Twitter (X) account for login

## Setup Instructions

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/twitter-trends-scraper.git
    cd twitter-trends-scraper
    ```

2. **Create a virtual environment and activate it:**

    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Install ChromeDriver:**

    - Download ChromeDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).
    - Make sure ChromeDriver is in your PATH or specify the path in the script.

5. **Set up MongoDB:**

    - Install MongoDB from [here](https://docs.mongodb.com/manual/installation/).
    - Start the MongoDB service.

6. **Configure MongoDB URI:**

    Update the MongoDB URI in the script if needed.

    ```python
    MONGO_URI = 'mongodb://localhost:27017/'
    ```

7. **Update Twitter Credentials:**

    Replace `YOUR_TWITTER_USERNAME` and `YOUR_TWITTER_PASSWORD` in the script with your Twitter login credentials.

## Running the Scraper

1. **Run the scraper script:**

    ```sh
    python run.py
    ```

    This script will:
    - Open a Chrome browser.
    - Log into Twitter.
    - Navigate to the trending topics page.
    - Scrape the top 5 trending topics.
    - Store the trending topics in the MongoDB database and render it in your html file.

## Configuration

### MongoDB URI

You can obtain the MongoDB URI from the MongoDB Atlas website if you are using MongoDB's cloud service.

### Twitter (X) Login

Make sure to update the Twitter username and password in the script.

### Proxy Configuration

If you are using a proxy, configure it in the script as shown:

```python
proxy = "http://username:password@proxyserver:port"
options.add_argument('--proxy-server=%s' % proxy)
```


## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss changes.


## Contact

For any inquiries, please contact `workwithpranay.pandey@gmail.com`.