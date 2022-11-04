<img width="1110" alt="Screenshot 2022-11-04 at 11 44 49" src="https://user-images.githubusercontent.com/90323785/199942770-9996644c-e496-45ac-9ea8-b9aca9954bfa.png">


# Property-Scraper

This is a scraper that will return results found on a specific website/category.
Currently, it returns the results for Cluj-Napoca, Romania.

It creates a CSV file with the results which can be sorted out or interogated by other platforms. 


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install a few packages.

```bash
pip install bs4
pip install requests
```


## Usage

If you feel you need more details, you can add them by class in the list. 
I've added Title, Location, Price and Characteristics.

```python

        title = list.find('h2', class_="titlu-anunt").text.replace('\n', '')
        location = list.find('div', class_="location_wp").text.replace('\n', '')
        price = list.find('span', class_="pret-mare").text.replace('\n', '')
        characteristics = list.find('div', class_="swiper-wrapper").text.replace('\n', '')
```



## Future Development

Ability to work on multiple websites at once, and return locations according to some values inputed by the user (ex: cheapest from and area, most rooms for a certain price, etc.)
