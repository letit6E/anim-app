import requests as req
import validators
from bs4 import BeautifulSoup

IGNORE_TAGS = ['nav', 'script', 'figure', 'footer', 'header']
IGNORE_ATTRIBUTES = {
	'class': ['sidebar-header', 'navbar', 'footer', 'jumbotron'],
	'id': ['sidebar', 'navbar', 'footer']
}
ELEMENT_CONTENT_MIN_SIZE = 5


# syntax summarizer for html web page with article
def get_article_text(html_soup):
	result = ""
	for s in html_soup.select('article'):
		for line in s.text.split('\n'):
			if len(line.split()) >= ELEMENT_CONTENT_MIN_SIZE:
				result += line + '\n'
	return result


# syntax summarizer for html web page
def get_text(url):
	if not validators.url(url):
		return None

	page = req.get(url)
	html = page.text
	soup = BeautifulSoup(html, 'html.parser')

	if soup.select('article'):
		return get_article_text(soup)

	for tag in IGNORE_TAGS:
		for elem in soup.select(tag):
			elem.extract()

	for elem in soup.select('div'):
		if len(elem.text.split()) < ELEMENT_CONTENT_MIN_SIZE:
			elem.extract()

	for elem in soup.find_all():
		for attr in elem.attrs.keys():
			for attr_value in elem.attrs[attr]:
				if attr in IGNORE_ATTRIBUTES.keys() and attr_value in IGNORE_ATTRIBUTES[attr]:
					elem.extract()

	return soup.text
