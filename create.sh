#!/bin/bash

# This shell script will create and populate the necessary directories and files that are used for this project.
# It will also install all of the dependencies needed for this project using the “npm install” command.

# Create directories
mkdir lib
mkdir test

# Install dependencies
npm install selenium-webdriver
npm install chromedriver

# Create a headless browser
touch lib/headless_browser.js

# Populate headless_browser.js
echo "const {Builder, By, Key, until} = require('selenium-webdriver');
const chrome = require('selenium-webdriver/chrome');

module.exports = {
    // initialize a headless browser
    init: async function () {
        let options = new chrome.Options();
        options.addArguments('headless');
        let driver = await new Builder()
            .forBrowser('chrome')
            .setChromeOptions(options)
            .build();
        return driver;
    }
};" > lib/headless_browser.js

# Create a file for the test
touch test/test.js

# Populate test.js
echo "const HeadlessBrowser = require('../lib/headless_browser');

describe('Static Call Button Click Test', function () {
    let driver;

    before(async function () {
        driver = await HeadlessBrowser.init();
    });

    after(async function () {
        await driver.quit();
    });

    it('should click the static call button', async function () {
        await driver.get('http://floridascarwash.com');
        await driver.findElement(By.id('staticcallbutton')).click();
        let chatbotOpen = await driver.findElement(By.className('send_a_message_text')).isDisplayed();
        chatbotOpen.should.be.true;
    });
});" > test/test.js

# Start chromedriver
chromedriver --url-base=/wd/hub

# Run the test
node test/test.js
