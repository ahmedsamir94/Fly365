class ContactUsPage():

    def __init__(self,driver):
        self.driver= driver
        self.ContactUs_button_xpath="/html/body/div[1]/div/footer/div[1]/div/div/div[4]/div/div/strong/a"
        self.FullName_textbox_xpath="/html/body/div[1]/div/div[2]/div/div[3]/div/div[3]/div[1]/div/form/div/div[1]/div[1]/div/div[1]/div/input"
        self.Email_textbox_xpath="/html/body/div[1]/div/div[2]/div/div[3]/div/div[3]/div[1]/div/form/div/div[1]/div[2]/div/div/div/input"
        self.category_button_xpath="/html/body/div[1]/div/div[2]/div/div[3]/div/div[3]/div[1]/div/form/div/div[1]/div[3]/div/div/div/div/input"
        self.category_selection_button_xpath="/html/body/div[2]/div[1]/div[1]/ul/li[2]/span"
        self.message_textbox_xpath="/html/body/div[1]/div/div[2]/div/div[3]/div/div[3]/div[1]/div/form/div/div[2]/div/div/div/div/textarea"
        self.send_button_xpath="/html/body/div[1]/div/div[2]/div/div[3]/div/div[3]/div[1]/div/form/div/div[3]/button"

    def click_ContacUs(self):
        self.driver.find_element_by_xpath(self.ContactUs_button_xpath).click()

    def enter_FullName(self,fullname):
        self.driver.find_element_by_xpath(self.FullName_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.FullName_textbox_xpath).send_keys(fullname)

    def enter_email(self,email):
        self.driver.find_element_by_xpath(self.Email_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.Email_textbox_xpath).send_keys(email)

    def click_category(self):
        self.driver.find_element_by_xpath(self.category_button_xpath).click()

    def select_category(self):
        self.driver.find_element_by_xpath(self.category_selection_button_xpath).click()

    def enter_mesage(self,message):
        self.driver.find_element_by_xpath(self.message_textbox_xpath).send_keys(message)
    def click_send(self):
        self.driver.find_element_by_xpath(self.send_button_xpath).click()
