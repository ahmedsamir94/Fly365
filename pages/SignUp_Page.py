class SignUpPage():

    def __init__(self,driver):
        self.driver=driver
        # self.sign_in_button_xpath="/html/body/div[1]/div/div[1]/div/div/div[2]/div/div[3]/a"
        self.sign_up_button_xpath="/html/body/div[1]/div/footer/div[2]/div/div/div[2]/div/ul/li[4]/a"
        self.first_name_textbox_xpath="/html/body/div[1]/div/div[2]/div/div[2]/div[3]/div/form/div/div[1]/div[1]/div/div[2]/div/div/div[1]/input"
        self.family_name_textbox_xpath="/html/body/div[1]/div/div[2]/div/div[2]/div[3]/div/form/div/div[1]/div[2]/div/div[2]/div/div/div[1]/input"
        self.email_textbox_xpath="/html/body/div[1]/div/div[2]/div/div[2]/div[3]/div/form/div/div[2]/div/div/div[2]/div/div/div/input"
        self.password_textbox_xpath="/html/body/div[1]/div/div[2]/div/div[2]/div[3]/div/form/div/div[3]/div/div/div[2]/div/div/div/div/input"
        self.create_account_button_xpath="/html/body/div[1]/div/div[2]/div/div[2]/div[3]/div/form/div/div[4]/div/button"
        self.click_acount_button_xpath="/html/body/div[1]/div/div[2]/div/div/div[2]/div/div[3]/span"
        self.click_SignOut_button_xpath="/html/body/ul/li[3]"
        self.UserName_textbox_xpath="/html/body/div[1]/div/div[2]/div/div[2]/div[3]/div/form/div[2]/div[1]/div/div/div[2]/div/div/div/input"
        self.Password_textbox_xpath="/html/body/div[1]/div/div[2]/div/div[2]/div[3]/div/form/div[2]/div[2]/div/div/div[2]/div/div/div/div[1]/input"
        self.click_SignIn="/html/body/div[1]/div/div[2]/div/div[2]/div[3]/div/form/div[2]/div[4]/div/button"

    def click_SignUp(self):
        self.driver.find_element_by_xpath(self.sign_up_button_xpath).click()
    def enter_first_name(self,firstname):
        self.driver.find_element_by_xpath(self.first_name_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.first_name_textbox_xpath).send_keys(firstname)

    def enter_family_name(self,familyname):
        self.driver.find_element_by_xpath(self.family_name_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.family_name_textbox_xpath).send_keys(familyname)
    def enter_email(self,email):
        self.driver.find_element_by_xpath(self.email_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.email_textbox_xpath).send_keys(email)

    def enter_password(self,password):
        self.driver.find_element_by_xpath(self.password_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.password_textbox_xpath).send_keys(password)

    def create_account(self):
        self.driver.find_element_by_xpath(self.create_account_button_xpath).click()

    def click_account(self):
        self.driver.find_element_by_xpath(self.click_acount_button_xpath).click()
    def click_SignOut(self):
        self.driver.find_element_by_xpath(self.click_SignOut_button_xpath).click()
    def enter_username(self,username):
        self.driver.find_element_by_xpath(self.UserName_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.UserName_textbox_xpath).send_keys(username)

    def enter_Password(self,Password):
        self.driver.find_element_by_xpath(self.Password_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.Password_textbox_xpath).send_keys(Password)

    def click_SignIn(self):
        self.driver.find_element_by_xpath(self.click_SignIn).click()