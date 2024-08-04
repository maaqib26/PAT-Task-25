"""
Program - PAT-Task-25 - Enter Data on IDMB Site and search the data
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class IMDB:

    # Locators Data
    expand_all_locator = '//div[@role="tabpanel"]//div//button[@data-testid="adv-search-expand-all"]'
    name_locator = 'name-text-input'
    from_year_locator = 'birth-year-month-start-input'
    to_year_locator = 'birth-year-month-end-input'
    page_topics_selection_locator = '//div[@role="tabpanel"]//div//button[@data-testid="test-chip-id-BIOGRAPHY"]'
    search_within_topic_locator = 'within-topic-dropdown'
    drop_down_option_locator = '//div//select//option[@value="BIRTH_PLACE"]'
    gender_identity_locator = '//div[@role="tabpanel"]//div//button[@data-testid="test-chip-id-MALE"]'
    adult_name_choice_locator = 'include-adult-names'
    see_results_locator = '//div[@role="tabpanel"]//div//button[@data-testid="adv-search-get-results"]'


    # Constructor of the class
    def __init__(self,url):
        self.url = url
        # Initializing the webdriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 15)

    # Method for Starting the automation
    def start_automation(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            return True
        except:
            print("ERROR: Not able to start python automation")
            return False

    # Method to Fill Data in the IDMB Site
    def fill_data(self):
        try:
                # Creating an instance for action class
                actions = ActionChains(self.driver)
                # Clicking on the expand all button
                expand_all_button = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.expand_all_locator)))
                expand_all_button.click()

                # Entering the data in the name field
                name = self.wait.until(EC.presence_of_element_located((By.NAME,self.name_locator)))
                # Moving to the element using action chains
                actions.move_to_element(name).perform()
                name.send_keys('Logan Williams')

                # Entering the data in the date field
                from_date = self.wait.until(EC.presence_of_element_located((By.NAME,self.from_year_locator)))
                # Moving to the element using action chains
                actions.move_to_element(from_date).perform()
                from_date.send_keys('1999')

                to_date = self.wait.until(EC.presence_of_element_located((By.NAME, self.to_year_locator)))
                # Moving to the element using action chains
                actions.move_to_element(to_date).perform()
                to_date.send_keys('2010')

                # Selecting desired options in the "Page Topics" section
                page_topic = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.page_topics_selection_locator)))
                # Entering the data in the date field
                actions.move_to_element(page_topic).perform()
                page_topic.click()

                topic = self.wait.until(EC.element_to_be_clickable((By.NAME, self.search_within_topic_locator)))
                # Entering the data in the date field
                actions.move_to_element(topic).perform()
                topic.click()

                option = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.drop_down_option_locator)))
                option.click()

                #Selecting the gender
                gender_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.gender_identity_locator)))
                # Entering the data in the date field
                actions.move_to_element(gender_button).perform()
                gender_button.click()

                #Including adult names
                adult_name_button = self.wait.until(EC.element_to_be_clickable((By.ID, self.adult_name_choice_locator)))
                actions.move_to_element(adult_name_button).perform()
                # Entering the data in the date field
                adult_name_button.click()

        except (NoSuchElementException, ElementNotVisibleException) as e:
                print("ERROR : ", e)

    # Method to search data in IDMB Site
    def search_data(self):
        try:
            # Searching the results in the IDMB Site
            search_result = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.see_results_locator)))
            search_result.click()

        except (NoSuchElementException, ElementNotVisibleException) as e:
            print("ERROR : ", e)

        finally:
            print("Input Data entered and searched the data on the site, search url returned is ,\n",self.driver.current_url)

    # Method to shutdown automation
    def shutdown(self):
        self.driver.quit()

# Main block
if __name__=="__main__":
    # Setting the URL
    url = "https://www.imdb.com/search/name/"
    obj = IMDB(url)
    obj.start_automation()
    obj.fill_data()
    obj.search_data()
    obj.shutdown()
