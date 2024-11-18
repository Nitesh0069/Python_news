import requests  # Importing the requests library to make HTTP requests
import json  # Importing the json library to work with JSON data

# Prompting the user to input the type of news they are interested in
query = input("What kind of news are you interested in? ")

# Constructing the URL with parameters to fetch news from News API
# 'q' parameter takes the user's input for a search query
# 'from' specifies the start date for the news articles
# 'sortBy' arranges articles by published date
# 'apiKey' is the API key for authentication (ensure this key is valid)
url = f"https://newsapi.org/v2/everything?q={query}&from=2024-10-18&sortBy=publishedAt&apiKey=9d43991268704613a402836ab715903c"
# get free api keys from https://newsapi.org/

# Making an HTTP GET request to the constructed URL
response = requests.get(url)

# Parsing the response's text content (which is in JSON format) into a Python dictionary
news = json.loads(response.text)

# Checking if the request was successful by verifying the HTTP status code (200 indicates success)
if response.status_code == 200:
    print("\n--- News Articles ---")  # Header to indicate the start of news output
    
    # Iterating through each article in the 'articles' list within the response
    for article in news.get("articles", []):
        # Displaying the title of the article
        print(f"Title: {article['title']}")
        # Displaying the name of the source/publisher of the article
        print(f"Source: {article['source']['name']}")
        # Displaying when the article was published
        print(f"Published At: {article['publishedAt']}")
        # Displaying a brief description of the article, if available
        print(f"Description: {article['description']}")
        # Displaying the URL of the full article for further reading
        print(f"URL: {article['url']}\n")
        # Adding a line separator for better readability between articles
        print("-" * 80)
else:
    # If the request failed (non-200 status code), print an error message with details
    print(f"Failed to fetch news. Status Code: {response.status_code}")
    # Displaying the reason for failure, if available from the API response
    print("Reason:", news.get("message", "No additional information available."))
