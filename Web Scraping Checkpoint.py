import requests
from bs4 import BeautifulSoup

# 1) Function to Get and parse HTML content
def get_wiki_soup(url):
    headers = {"User-Agent": "Mozilla/5.0"}  # Mimic a browser request
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return BeautifulSoup(response.content, 'html.parser')
    else:
        return None

# 2) Function to Extract article title
def extract_title(soup):
    title_element = soup.find('h1', id='firstHeading')
    return title_element.get_text() if title_element else "Title Not Found"

# 3) Function to Extract article text mapped to headings
def extract_content_by_headings(soup):
    content_map = {}
    current_heading = "Introduction"
    content_map[current_heading] = []
    
    body = soup.find('div', class_='mw-parser-output')
    if not body:
        return content_map

    for element in body.find_all(['h2', 'h3', 'p']):
        if element.name in ['h2', 'h3']:
            # Update the heading and clean the [edit] text
            current_heading = element.get_text().replace('[edit]', '').strip()
            content_map[current_heading] = []
        elif element.name == 'p':
            text = element.get_text().strip()
            if text:
                content_map[current_heading].append(text)
    
    return content_map

# 4) Function to collect links to other Wikipedia pages
def collect_internal_links(soup):
    links = []
    body_content = soup.find('div', id='bodyContent')
    if body_content:
        for link in body_content.find_all('a', href=True):
            href = link['href']
            # Filter for internal wiki articles (skip files, help, or external links)
            if href.startswith('/wiki/') and ':' not in href:
                full_url = f"https://en.wikipedia.org{href}"
                links.append(full_url)
    return list(set(links))  # Return unique links

# 5) Wrapper function
def scrape_wikipedia(url):
    soup = get_wiki_soup(url)
    if not soup:
        return "Failed to retrieve the page."

    return {
        "title": extract_title(soup),
        "content": extract_content_by_headings(soup),
        "internal_links": collect_internal_links(soup)
    }

# 6) Test the function
if __name__ == "__main__":
    target_url = "https://wikipedia.org"
    wiki_data = scrape_wikipedia(target_url)

    print(f"Title: {wiki_data['title']}")
    print(f"Number of internal links found: {len(wiki_data['internal_links'])}")
    
    # Print a snippet of the Introduction
    intro_text = " ".join(wiki_data['content'].get('Introduction', []))
    print(f"\nIntroduction Snippet:\n{intro_text[:200]}...")
