import csv
import requests
from bs4 import BeautifulSoup


BASE_URL = "https://www.truecar.com/used-cars-for-sale/listings/"


def scrape_car_data(car_name: str):
    """
    Scrape used car information from TrueCar.
    """
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 Chrome/136.0 Safari/537.36")}
    url = BASE_URL + car_name
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException as error:
        print(f"Request failed:\n{error}")
        return
    soup = BeautifulSoup(response.text, "html.parser")
    cars = soup.find_all("div", class_="w-full truncate")
    if not cars:
        print("No cars found.")
        return
    output_file = f"{car_name}_cars_info.csv"
    with open(output_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Car Name", "Price", "Mileage"])
        for car in cars[:20]:
            price = car.find(
                "span",
                attrs={"data-test": "vehicleCardPriceLabelAmount"})
            mileage = car.find(
                "div",
                attrs={"data-test": "vehicleMileage"})
            writer.writerow([
                car_name,
                price.get_text(strip=True) if price else "N/A",
                mileage.get_text(strip=True) if mileage else "N/A"])
    print(f"\nSaved successfully to '{output_file}'")


if __name__ == "__main__":
    car = input("Enter car name: ").strip()
    scrape_car_data(car)