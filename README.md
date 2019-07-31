
# Describtion

  - Sign Up test case it will make registration to new account then verify it by logging in . 
  - Search test case it will fill all textboxes then click search.
  - Contact us test case will go to contact Us and fill all textboxes then click send.
  


### Installation

```sh
$ download python
$ install python
$ add python to payj environment variable (if not already exist)
$ install selenium 
$ install pytest
$ install allure reports
```

### Running commands

```sh
$ python -m pytest --alluredir=reports/allure-reports
$ allure serve reports/allure-reports
```

### Notes
* you need to change the data in utils file like  [email](https://nodejs.org/) and [message](https://nodejs.org/)   to pass these test cases
