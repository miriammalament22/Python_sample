# Salary Data Scraper

## Overview

This script scrapes salary data from the [DBK News Salary Guide](https://salaryguide.dbknews.com/) for the 'Economics' department over multiple years and saves the data in an Excel file.

## Requirements

- Python 3.x
- Selenium
- WebDriver Manager for Chrome
- Pandas

# Usage

1. Ensure Google Chrome is installed.
2. Clone this repository.
3. Run the script:

    ```bash
    python salary_data_scraper.py
    ```

   The script will open a Chrome browser, navigate to the DBK News Salary Guide, and scrape data, saving it to `scraped_salary_data_allyears.xlsx`.

## Details

### Setup

- Initializes Selenium WebDriver.
- Opens the salary guide website.

### Year Extraction

- Extracts years from the dropdown menu.

### Data Scraping

- Selects each year.
- Searches for 'economics'.
- Scrapes employee data.
- Paginates through results.

### Data Storage

- Saves data to `scraped_salary_data_allyears.xlsx`.

## Data

Ensure necessary data directories are available. The data will be uploaded as permissions are obtained in the future.

## Contribution

Contributions are welcome. Fork the repository and create a pull request for improvements or features.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
