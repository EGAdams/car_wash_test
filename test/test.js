const HeadlessBrowser = require('../lib/headless_browser');

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
});
