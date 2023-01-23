# HTTPX-Selectolax tutorial

To use `httpx` and `selectolax` to scrape data from a website:

Install the libraries by running pip install `httpx` and pip install `selectolax`
Import the libraries in your script
Use the `httpx.get(url)` function to make a request to the website, where url is the URL of the website you want to scrape
Use the `HTMLParser(response.content)` function to parse the HTML content of the website
Use the `root.css(selector)` function to find elements in the HTML using CSS selectors, where root is the parsed HTML content and selector is the CSS selector for the elements you want to find
Extract the data from the elements and use it as needed
It's good to practice web scraping on a website that allows web scraping and you have permission to scrape the data.

You'll find a full example script of scraping data from a specialized website in sell music instruments 


don't forget "ENJOY lEARNING"