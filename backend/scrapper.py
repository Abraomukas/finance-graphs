import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt


def extract_values_from_url(url):
    try:
        response = requests.get(url)

        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, "html.parser")

            # Find the specific <div> element by its class
            stock_prize_div = soup.find("div", class_="kf1m0")

            if stock_prize_div:
                return stock_prize_div.text.strip()
            else:
                print(f"Div with class 'kf1m0' not found on the page.")
        else:
            print(
                f"Failed to retrieve content from {url}. Status code: {response.status_code}"
            )
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # url = input("Enter the URL: ")

    url = "https://www.google.com/finance/quote/ACN:NYSE?hl=en"
    extracted_elements = extract_values_from_url(url)

    print("Stock value - " + extracted_elements)

    x = ["10am", "12pm", "2pm", "4pm"]
    y = [float(extracted_elements.replace("$",""))-10.0, float(extracted_elements.replace("$",""))-5.0, float(extracted_elements.replace("$","")),float(extracted_elements.replace("$",""))+5.0]

    plt.plot(x, y)
    
    plt.xlabel("TIME")

    plt.ylabel("VALUE")


    plt.title("Accenture's stock")


    plt.show()
