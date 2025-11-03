# Bloco de leitura de arquivo
with open('alunos.txt', 'r', encoding='utf-8') as arquivo:
    aprovados = 0
    
    for linha in arquivo:
        linha = linha.strip()
        nome, nota1, nota2 = linha.split(';')
        print(f"Aluno: {nome} | Nota 1: {nota1} | Nota 2: {nota2}")
        
        media = float(nota1) + float(nota2)
        media/=2
        print(f"{nome} -> {media:.2f}") 
        
        if media >= 7.0:
            aprovados+=1
        