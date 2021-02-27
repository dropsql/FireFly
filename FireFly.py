API_KEY = '' # https://numverify.com/
API_URL = 'http://apilayer.net/api/validate?access_key={key}&number={phone_number}&country_code=&format={format}'

import requests, sys

from rich.console import Console

BANNER = '''[magenta]
   __ _          __ _      
  / _(_)_ _ ___ / _| |_  _ 
 |  _| | '_/ -_)  _| | || | [green]A fork of https://github.com/Lexxrt/FireFly[/green]
 |_| |_|_| \___|_| |_|\_, | [green]by https://github.com/dropsql[/green]
                      |__/ 
[/magenta]
'''

console = Console()
console.print(BANNER)

if not __import__('re').match(r'[a-f0-9]{32}', API_KEY):
	console.print(f'[red][-][/red] {API_KEY} isn\'t a numverify.com api key.')
	sys.exit()

if len(sys.argv) == 1:
	console.print(f'py {sys.argv[0]} <number 1> <number 2> (etc.)')
	sys.exit(-1)

for number in sys.argv[1:]:
	console.rule(f'results for number: \'{number}\'')

	r = requests.get(
		url=API_URL.format(key=API_KEY, phone_number=number, format=1)
	)
	
	if 'You have not supplied a valid API Access Key' in r.text:
		console.print('[red][-][/red] your API key seems invalid :/')
		sys.exit()

	json_data = r.json()
	if json_data['valid'] == True:
		for key, value in json_data.items():
			if value:
				if '_' in key:
					out = ''
					for y in key.split('_'):
						out += f'{y[0].upper()}{y[1:]} '
					out = out[:-1] if out.endswith(' ') else out
				else:
					out = f'{key[0].upper()}{key[1:]}'
				console.print(f'[green][+][/green] {out}: {value}')
	else:
		console.print('[red][-][/red] the phone number seems invalid :/')

console.rule('done')