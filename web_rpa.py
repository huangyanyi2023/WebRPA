from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import URL, ACTIONS, OUTPUT_FILE

class WebRPA:
    def __init__(self):
        self.driver = webdriver.Chrome()  # Change to the appropriate web driver

    def fill_form(self, url, data):
        self.driver.get(url)
        for field, value in data.items():
            element = self.driver.find_element(By.NAME, field)
            element.send_keys(value)

    def click_button(self, url):
        self.driver.get(url)
        button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button")))
        button.click()

    def extract_table_data(self, url):
        self.driver.get(url)
        table = self.driver.find_element(By.XPATH, "//table")
        rows = table.find_elements(By.TAG_NAME, "tr")
        table_data = []
        for row in rows:
            columns = row.find_elements(By.TAG_NAME, "td")
            row_data = [column.text for column in columns]
            table_data.append(row_data)
        return table_data

if __name__ == '__main__':
    rpa = WebRPA()
    with open(OUTPUT_FILE, 'w') as file:
        for action in ACTIONS:
            action_type = action['type']
            action_url = action['url']
            if action_type == 'fill_form':
                action_data = action['data']
                rpa.fill_form(action_url, action_data)
                file.write(f'Filled form on {action_url}\n')
            elif action_type == 'click_button':
                rpa.click_button(action_url)
                file.write(f'Clicked button on {action_url}\n')
            elif action_type == 'extract_table_data':
                table_data = rpa.extract_table_data(action_url)
                file.write(f'Table data from {action_url}:\n')
                for row in table_data:
                    file.write(','.join(row) + '\n')
