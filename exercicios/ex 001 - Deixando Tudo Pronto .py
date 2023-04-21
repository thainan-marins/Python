# impostamos a biblioteca para poder printar os emojis
import emoji
# usando o código \033[m para adiconar cores ao terminal
print('\033[1;34m-=-' * 7)
# usei a função print para escrever na tela
print('\033[32m Olá, Mundo!\033[m')
# aqui printamos o emoji usando: da biblioteca emoji pegue o método emojize(que serve para trancrever as palavras
# em emojis.
# o parâmetro 'language' serve para definir a língua do emoji, sem esse parâmetro ele não funcionará
print(emoji.emojize(':wave:' * 5, language='alias'))
# finalizamos retpetindo uma string com o código de cor
