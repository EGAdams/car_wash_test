const {Builder, By, Key, until} = require('selenium-webdriver');
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
};
