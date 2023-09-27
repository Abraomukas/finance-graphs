import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta
import time

TIMESTAMP_FORMAT = "%b %d, %I:%M:%S %p UTC%z"
URL = "https://www.google.com/finance/quote/ACN:NYSE?hl=en"

def extract_values_from_url():
    try:
        response = requests.get(URL)

        if response.status_code == 200:
            # Calculate the offset (NY UTC = -4)
            utc_offset = timedelta(hours=-4)

            # Save the time when the request was made
            timestamp = (datetime.utcnow() + utc_offset).strftime(TIMESTAMP_FORMAT)

            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, "html.parser")

            # Find the specific <div> element by its class
            stock_prize_div = soup.find("div", class_="kf1m0")

            if stock_prize_div:
                return timestamp, stock_prize_div.text.strip()
            else:
                print(f"Div with class 'kf1m0' not found on the page.")
        else:
            print(
                f"Failed to retrieve content from {URL}. Status code: {response.status_code}"
            )
    except Exception as e:
        print(f"An error occurred: {e}")


def populate_values():
    with open("output.txt", "a") as file:
        time, value = extract_values_from_url()

        input_date = datetime.strptime(time, "%b %d, %I:%M:%S %p UTC")

        timestamp = input_date.strftime("%I:%M %p")

        file.write(timestamp + " <> " + value.replace("$", "") + "\n")

        print("Entry added!")


if __name__ == "__main__":
    # time, value = extract_values_from_url()

    # print("Timestamp - " + time)
    # print("Stock value - " + value)

    # timeAxis = ["10am", "12pm", "2pm", "4pm"]
    # valueAxis = np.array([3, 8, float(value.replace("$", "")), 10])

    # plt.plot(timeAxis, valueAxis, marker="o", linestyle="dashed")

    # plt.xlabel("TIME")
    # plt.ylabel("VALUE")
    # plt.title("Accenture's stock")

    # plt.show()

    ###

    while True:
        populate_values()

        time.sleep(60)

