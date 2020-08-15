# Test automation framework for Phorest salon software demo

# Architecture

- Page object model (POM)
    - Separate elements in one place
    - Separate locators in one place
    - The test contain only abstract non-technical steps
    - The pages files contains the technical steps (assertion, etc.)

# Scenarios

- Pay with a picked amount($50/$100/$150) and send to me
    - Fill the details
    
- Pay with a picked amount($50/$100/$150) and send to someone else
- Pay with other amount ($256) and send to me
- Pay with other amount ($256) and send to someone else and check emails

## Checking emails arrives

 - Mailosaur: [link](http://mailosaur.com/)
    - Mailosaur is email testing software that lets you capture and test email, helping you build, test and present your product.
    It has a 14 days of free trial version

# Bug

- I didn't find any bug

# Report

 - Third part library called pyunitreport which is using HTMLTestRunner and create html reports and put it into the reports folder


# Log

- Built in logging folder

# Selenium webdriver

 - Version: 85.0.4183.38
 - Browser: Chrome
 - OS version: Mac