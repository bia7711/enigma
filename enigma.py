mapa = {
  '6': 'F',
  '5': 'e',
  '50': 'l',
  '1': 'i',
  '26': 'z',
  'mm': '2000',
  'r': '18',
} 

mensagem = input("Digite o código: ")
if mensagem != '6550126mmr':
    print("Erro: código incorreto!")
else:
    enigma = ''.join([mapa.get(chave) 
      for chave in ['6', '5', '50', '1', '26', 'mm', 'r']])                

    numero1 = enigma.replace("2000", " 20")
    print("Mensagem decodificada é:",numero1)
