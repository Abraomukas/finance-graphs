import requests
from bs4 import BeautifulSoup


def extract_values_from_url(url):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, "html.parser")

            # Find and extract the values you are interested in
            # For example, let's say you want to extract all the text within <p> tags
            values = []
            for paragraph in soup.find_all("p"):
                values.append(paragraph.text)

            return values
        else:
            print(
                f"Failed to retrieve content from {url}. Status code: {response.status_code}"
            )
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    url = input("Enter the URL: ")
    extracted_values = extract_values_from_url(url)

    if extracted_values:
        print("Extracted values:")
        for value in extracted_values:
            print(value)
