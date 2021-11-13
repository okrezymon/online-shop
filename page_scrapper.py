from typing import List, Dict
import requests
from bs4 import BeautifulSoup
import pandas as pd

PRODUCT_QUANTITY = 1000


def _get_product_categories() -> List[str]:
    categories = []
    url = "https://strefakursow.pl"
    page = requests.get(url)
    assert page.status_code == 200
    soup = BeautifulSoup(page.content, "html.parser")
    category_details_container = soup.find(
        "div", {"class": "js-category-details-container u-display-none"}
    )
    for category_details in category_details_container.find_all(
        "div", {"class": "menu-navigation__content js-category-details"}
    ):
        categories.append(category_details["id"])
    return categories


def _get_category_url(category: str, page_no: int) -> str:
    if page_no == 0:
        return f"https://strefakursow.pl/kursy/{category}.html"
    else:
        return f"https://strefakursow.pl/kursy/{category}/{page_no}.html"


def _download_image(img_tag):
    img_data_src = img_tag["data-src"]
    print(f"Downloading image {img_data_src}")
    img_data = requests.get(img_data_src).content
    with open(f"images/{img_tag['alt']}.jpg", "wb") as handler:
        handler.write(img_data)


def _get_product_details(soup, category, products_df):
    category = category.replace("_", " ").upper()
    site_container = soup.find("div", {"class": "js-mobile-site-container"})
    l_container = site_container.find("div", {"class": "l-container u-mb-45"})
    product_list = l_container.find("div", {"class": "b-product-list"})
    for product_box in product_list.find_all("div", {"class": "b-product-box desktop"}):
        for a_div in product_box.find_all("a", href=True):
            if a_div.contents[1] is not None:
                try:
                    my_div = a_div.contents[1]
                    description = my_div.find("div", {"class": "description"}).text
                    title = my_div.find("div", {"class": "name desktop"}).text
                    price = my_div.find("div", {"class": "new desktop"}).text.replace(
                        "zł", ""
                    )
                    information_divs = my_div.find_all(
                        "div", {"class": "information desktop"}
                    )
                    level = information_divs[0].text.split(":")[1].strip()
                    lectures_count_txt = my_div.find_all(
                        "div", {"class": "information desktop"}
                    )[1].text
                    lectures_count = [
                        int(s) for s in lectures_count_txt.split() if s.isdigit()
                    ][0]
                    training_materials_count_txt = my_div.find_all(
                        "div", {"class": "information desktop"}
                    )[2].text
                    training_materials_count = [
                        int(s)
                        for s in training_materials_count_txt.split()
                        if s.isdigit()
                    ][0]
                    product_details = f"{training_materials_count} materiałów treningowych i {lectures_count} wykładów."
                    img_tag = my_div.find("img")
                    img_src = img_tag["data-src"]
                    # _download_image(img_tag)
                    img_alt = img_tag["alt"]
                    product_details = {
                        "category": category,
                        "title": title,
                        "description": description,
                        "price": price,
                        "level": level,
                        "img_alt": img_alt,
                        "img_src": img_src,
                        "product_quantity": PRODUCT_QUANTITY,
                        "product_details": product_details,
                    }
                    products_df = products_df.append(
                        product_details, ignore_index=True,
                    )
                except Exception as e:
                    print(e)
    return products_df


def _download_product_details(
    categories: List[str], products_df: pd.DataFrame
) -> pd.DataFrame:
    for category in categories:
        for i in range(0, 9):
            url = _get_category_url(category=category, page_no=i)
            page = requests.get(url)
            if page.status_code != 200:
                continue
            soup = BeautifulSoup(page.content, "html.parser")
            products_df = _get_product_details(soup, category, products_df)
    return products_df


def _save_df_to_csv(df: pd.DataFrame, file_name: str):
    df.to_csv(f"{file_name}.csv", sep="\t", encoding="utf-8")


if __name__ == "__main__":
    products_df = pd.DataFrame(
        columns=[
            "category",
            "title",
            "description",
            "price",
            "level",
            "img_alt",
            "img_url" "product_quantity",
            "product_details",
        ]
    )
    categories = _get_product_categories()
    products_df = _download_product_details(
        categories=categories, products_df=products_df
    )
    _save_df_to_csv(df=products_df, file_name="products_data")
