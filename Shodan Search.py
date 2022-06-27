import shodan
import argparse

parser = argparse.ArgumentParser(description='API Shodan Search ')
parser.add_argument('--key', '-k', help="Shodan API Key", required=True)
args = parser.parse_args()

api = shodan.Shodan(args.key)

"Dorks mais usados"
'''
    country: filtro para um país específico
    city: filtro para uma cidade especifica
    geo: filtro para coordenada
    hostname: procure um nome de host correspondente
    net: limite a um IP/prefixo
    os: filtro baseado no sistema operacional
    port: filtro baseado em portas abertas
'''

try:
    # Buscar no Shodan
    pesquisa = input("pesquisar:")
    results = api.search(pesquisa)

    # Mostrar os resultados
    print("Results found: %s" % results['total'])
    for result in results['matches']:
        print('IP: %s' % result['ip_str'])
        print(result['data'])
        print('')

except shodan.APIError as e:
    print('Error: %s' % e)
