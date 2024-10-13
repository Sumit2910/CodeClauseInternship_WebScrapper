import requests
from bs4 import BeautifulSoup

def fetch_html_content(url):
    """
    Fetch the HTML content from the given URL.

    Parameters:
    url (str): The URL of the website to scrape.

    Returns:
    str: HTML content of the website.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  
        html_content = response.content
        if html_content: 
            return html_content
        else:
            print("No HTML content found.")
            return None
    except requests.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return None

def parse_headlines(html_content):
    """
    Parse the HTML content to extract news headlines.

    Parameters:
    html_content (str): HTML content of the website.

    Returns:
    list: A list of extracted headlines.
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    headlines = []

    headline_elements = soup.find_all('h2', class_='headline')

    print(f"Found {len(headline_elements)} headline elements")

    for element in headline_elements:
        headline = element.get_text().strip()
        print(f"Headline: {headline}")
        headlines.append(headline)

    return headlines

def display_headlines(headlines):
    """
    Display the list of headlines.

    Parameters:
    headlines (list): A list of news headlines.
    """
    if headlines:
        print("News Headlines:")
        for idx, headline in enumerate(headlines, 1):
            print(f"{idx}. {headline}")
    else:
        print("No headlines found.")

def main():
    """
    Main function to run the web scraper.
    """
    url = input("Enter the entire URL of the desired website: ")
    html_content = fetch_html_content(url)

    if html_content:
        headlines = parse_headlines(html_content)
        display_headlines(headlines)

if __name__ == '__main__':
    main()
