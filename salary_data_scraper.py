#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 23:16:29 2023

@author: miriammalament
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
import time

# Set up the webdriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://salaryguide.dbknews.com/')

# Create an empty DataFrame
df = pd.DataFrame(columns=['Year', 'School', 'Department', 'Division', 'Title', 'Employee', 'Salary'])

# Add explicit wait
wait = WebDriverWait(driver, 10)

# Extract the list of years first
year_dropdown = Select(wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "select[label='years']"))))
years_list = [option.text for option in year_dropdown.options]

# Iterate over each year
for year in years_list:
    # Navigate to the main page and wait for it to load
    driver.get('https://salaryguide.dbknews.com/')
    time.sleep(5)

    # Locate the year drop-down and select the year
    year_dropdown = Select(wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "select[label='years']"))))
    year_dropdown.select_by_visible_text(year)

    # Wait for the page to update
    time.sleep(5)

    # Perform the search for 'economics'
    search_box = wait.until(EC.presence_of_element_located((By.ID, 'search-box')))
    search_box.clear()
    search_box.send_keys('economics')
    search_box.send_keys(Keys.ENTER)

    # Wait for the results to load
    time.sleep(5)

    # Scrape data for the selected year
    while True:
        employees = driver.find_elements(By.CLASS_NAME, 'adt-employee')
        for employee in employees:
            name = employee.find_element(By.CLASS_NAME, 'employee-name').text
            details = employee.find_elements(By.CLASS_NAME, 'employee-detail')
            department_detail = details[0].text.split('|') if len(details) > 0 else ['', '']
            school = department_detail[0].strip()
            department = department_detail[1].strip() if len(department_detail) > 1 else ''
            division = details[1].text if len(details) > 1 else ''
            title = details[2].text if len(details) > 2 else ''
            salary = employee.find_element(By.CLASS_NAME, 'employee-salary').text

            df = df.append({
                'Year': year,
                'School': school,
                'Department': department,
                'Division': division,
                'Title': title,
                'Employee': name,
                'Salary': salary
            }, ignore_index=True)

        # Check if there's a next page
        try:
            next_button = driver.find_element(By.ID, 'btn-next')
            if 'ui-disabled' in next_button.get_attribute('class'):
                break
            next_button.click()
            time.sleep(5)
        except NoSuchElementException:
            break  # Exit the loop if there's no next page button

# Quit the driver and save the DataFrame
driver.quit()
df.to_excel('scraped_salary_data_allyears.xlsx', index=False)
