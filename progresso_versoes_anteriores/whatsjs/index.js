const qrcode = require('qrcode-terminal');
const { Client, LocalAuth } = require('whatsapp-web.js');

const client = new Client({
    authStrategy: new LocalAuth(),
    puppeteer: {
        headless: true,
        args: [ '--no-sandbox', '--disable-gpu', ],
    },
    webVersionCache: { type: 'none', remotePath: 'https://raw.githubusercontent.com/wppconnect-team/wa-version/main/html/2.24.7.72.html', }
});

client.on('qr', qr => {
    qrcode.generate(qr, {small: true});
});

client.on('ready', () => {
    console.log('Client is ready!');
});

client.on('message_create', message => {
	if (message.body === '!ping') {

		client.sendMessage(message.from, 'pong');
	}
});

client.initialize();
