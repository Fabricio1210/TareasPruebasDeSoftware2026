exports.config = {
    runner: 'local',
    framework: 'cucumber',

    specs: ['./features/**/*.feature'],

    maxInstances: 1,

    capabilities: [{
        platformName: 'Android',
        'appium:automationName': 'UiAutomator2',
        'appium:browserName': 'Chrome',
        'appium:chromeOptions': {
            args: [
                '--disable-blink-features=AutomationControlled'
            ]
        }
    }],

    services: [
        ['appium', {
            args: {
                relaxedSecurity: true,
                allowInsecure: ['chromedriver_autodownload']
            }
        }]
    ],

    logLevel: 'info',

    waitforTimeout: 10000,

    cucumberOpts: {
        require: ['./features/steps/*.js'],
        timeout: 60000
    },

    reporters: ['spec']
};