def filtrarLeadsQualificados(leads: list[dict]) -> list[dict]:
    result = [] #declarando uma lista para append dicionários com score acima de 70
    for linha in leads: #cada linha vai ser um dicionário
        print(linha) #imprimir dicionário
        if linha.get("score") > 70: #puxar valor contido na chave "score" do dicionário da linha para verificar se é maior que 70
            print(f"maior que 70\n")
            result.append(linha) #adicionar o dicionário com score>70 a lista result

    return result #retornar lista de dicionários com score>70

def calcularTaxaConversaoOrigem(a: list[dict]) -> dict:
    totais: dict[str, int] = {}
    ganho: dict[str, int] = {}

    for lead in a:
        origem = lead.get('origem')
        status = lead.get('status')

        if origem not in totais:
            totais[origem] = 0
            ganho[origem] = 0

        totais[origem] += 1
        
        if status == 'ganho':
            ganho[origem]+=1

    #calculando taxa de conversão
    for chaveOrigem in totais:
        #quando você faz um for sobre um dicionário, o iterador percorre as chaves — por padrão.
        #logo, o chaveOrigem sempre será "Instagram" ou "Google Ads" ou "Indicação"

        tot = totais.get(chaveOrigem)
        gan = ganho.get(chaveOrigem)

        if tot > 0:
            taxa = gan / tot 
            print(f"{chaveOrigem} possui uma taxa de {(taxa*100):.2f}%")

def main():
    leads = [
    {"nome":"Ana","origem":"Instagram","score":82,"status":"ganho"},
    {"nome":"Beto","origem":"Google Ads","score":65,"status":"perdido"},
    {"nome":"Cris","origem":"Indicação","score":90,"status":"ganho"},
    {"nome":"Duda","origem":"Instagram","score":74,"status":"perdido"},
    {"nome":"Enzo","origem":"Google Ads","score":71,"status":"ganho"},
    ] #leads é uma lista de dicionário
    # dicionário é uma linha: {"nome":"Ana","origem":"Instagram","score":82,"status":"ganho"}

    a = filtrarLeadsQualificados(leads)
    print(a)
    calcularTaxaConversaoOrigem(leads)

    

if __name__ == "__main__":
    main()