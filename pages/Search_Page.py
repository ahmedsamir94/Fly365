
class SearchPage():


    def __init__(self,driver):
        self.driver = driver

        self.origin_textbox_xpath = "/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/div/div[2]/div[1]/form/div/div/div[1]/div/div[1]/div/div/div[1]/input"
        self.origin_textbox_xpath_click="/html/body/div[2]/div[1]/div[1]/ul/li[1]/div"

        self.destination_textbox_xpath = "/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/div/div[2]/div[1]/form/div/div/div[1]/div/div[2]/div/div/div[1]/input"
        self.destination_textbox_xpath_click="/html/body/div[3]/div[1]/div[1]/ul/li[1]/div"

        self.departure_textbox_xpath ="/html/body/div[4]/div[1]/div/div[2]/table/tbody/tr[2]/td[5]/div/span"
        self.arrival_textbox_xpath="/html/body/div[4]/div[1]/div/div[2]/table/tbody/tr[6]/td[6]/div/span"

        self.search_button_xpath="/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/div/div[2]/div[1]/form/div/div/div[4]/button"

    def enter_origin(self,origin):
        self.driver.find_element_by_xpath(self.origin_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.origin_textbox_xpath).send_keys(origin)
        self.driver.find_element_by_xpath(self.origin_textbox_xpath_click).click()

    def enter_destination(self,destination):
        self.driver.find_element_by_xpath(self.destination_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.destination_textbox_xpath).send_keys(destination)
        self.driver.find_element_by_xpath(self.destination_textbox_xpath_click).click()

    def enter_date_time(self):
        self.driver.find_element_by_xpath(self.departure_textbox_xpath).click()
        self.driver.find_element_by_xpath(self.arrival_textbox_xpath).click()

    def click_search(self):
        self.driver.find_element_by_xpath(self.search_button_xpath).click()