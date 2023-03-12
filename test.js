// Node and Selenium Script to open a headless browser and click on an icon 
const {Builder, By, Key, until} = require('selenium-webdriver');
 
async function example() {
    let driver = await new Builder().forBrowser('chrome').setChromeOptions(
        { args: ['--headless'] }
    ).build();

    try {
        // Navigate to the website
        await driver.get('https://floridascarwash.com');

        // Find the icon with the id of 'staticcallbutton'
        let element = await driver.findElement(By.id('staticcallbutton'));

        // Click on the element
        await element.click();
    } finally {
        await driver.quit();
    }
}

example();
