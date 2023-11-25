import os
import requests
from bs4 import BeautifulSoup
import argparse

def download_file(url, directory, filename):
    if not os.path.exists(directory):
        os.makedirs(directory)
    response = requests.get(url)
    filepath = os.path.join(directory, filename)
    with open(filepath, 'wb') as file:
        file.write(response.content)
    print(f'Downloaded file: {filepath}')

def fetch_and_check_abstract(abstract_url, keywords):
    """
    Fetch the abstract of the paper and check if it contains any of the specified keywords.
    """
    response = requests.get(abstract_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    abstract_text = soup.find('blockquote', class_='abstract').text
    return any(keyword.lower() in abstract_text.lower() for keyword in keywords)
if __name__ == "__main__":
    # Set up command line argument parsing
    parser = argparse.ArgumentParser(description='Download papers from arXiv based on keywords.')
    parser.add_argument('keywords', nargs='+', help='Keywords to search for in paper abstracts')
    parser.add_argument('--show', type=int, default=50, help='Number of papers to show (default is 50)')
    args = parser.parse_args()

    # URL of the page to scrape with the 'show' parameter from command line
    url = f'https://arxiv.org/list/cs.CV/pastweek?show={args.show}'

    # Directory to save the papers
    download_directory = os.path.join('.', 'papers')  # Change this to your desired path

    # Use keywords from command line
    keywords = args.keywords

    # Send a request to the URL
    response = requests.get(url)
    data = response.text

    # Parse the HTML content
    soup = BeautifulSoup(data, 'html.parser')

    # Find all paper entries
    for entry in soup.find_all('dt'):
        title = entry.find_next_sibling('dd').find('div', class_='list-title').text.replace('Title:', '').strip()
        filename = title.replace(' ', '_').replace(':', '').replace('?', '') + '.pdf'
        abstract_link = 'https://arxiv.org' + entry.find('span', class_='list-identifier').find('a', title='Abstract')['href']

        if fetch_and_check_abstract(abstract_link, keywords):
            pdf_link = 'https://arxiv.org' + entry.find('span', class_='list-identifier').find('a', title='Download PDF')['href']
            download_file(pdf_link, download_directory, filename)
