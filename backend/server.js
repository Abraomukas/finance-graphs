const puppeteer = require('puppeteer');

// (async () => {
// 	const browser = puppeteer.launch({
// 		headless: false,
// 		defaultViewport: false,
// 		userDataDir: './tmp',
// 	});

// 	let stock = 'ACN';

// 	const page = await browser.newPage();

// 	await page.goto(`https://www.google.com/finance/quote/${stock}:NYSE?hl=en`);
// 	await page.screenshot({ path: 'example.png' });

// 	await browser.close();
// })();

// module.exports = run = async () => {
// 	console.log('!');

// 	const stock = 'ACN';
// 	const url = `https://www.google.com/finance/quote/${stock}:NYSE?hl=en`;

// 	const browser = await puppeteer.launch();
// 	const page = await puppeteer.newPage();

// 	await page.goto(url);

// 	return browser;
// };

(async () => {
	// Launch a headless browser
	const browser = await puppeteer.launch();

	// Open a new page
	const page = await browser.newPage();

	// Navigate to the URL
	const stock = 'ACN';
	const url = `https://www.google.com/finance/quote/${stock}:NYSE?hl=en`;
	await page.goto(url);

	// Wait for some time to ensure the data is loaded (you may need to adjust the timeout)
	const milliseconds = 3000;
	new Promise((r) => setTimeout(r, milliseconds));

	// Extract the data you need
	const data = await page.evaluate(() => {
		const assetName = document.querySelector('.YMlKec.fxKbKc').innerText;
		const assetPrice = document.querySelector(
			'.YMlKec.fxKbKc span[jsname="vWLAgc"]'
		).innerText;

		return {
			assetName,
			assetPrice,
		};
	});

	// Close the browser
	await browser.close();

	// Display the extracted data
	console.log('Asset Name:', data.assetName);
	console.log('Asset Price:', data.assetPrice);
})();
