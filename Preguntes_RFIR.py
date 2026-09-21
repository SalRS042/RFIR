import random
import pandas as pd
from IPython.display import clear_output

Pregs = pd.read_csv('Pregs.csv')

print(f'Hay {len(Pregs)} preguntas registradas.\n')

def mostrar_instrucciones():
    print(
        'INSTRUCCIONES\n'
        '1 - Las preguntas se responden con 1, 2, 3 o 4.\n'
        '2 - Para terminar la sesión de estudio escribe "Terminar".\n'
        '3 - Para pasar una pregunta escribe "Pasar".\n'
        '4 - Si la respuesta es incorrecta, permanecerás en la misma pregunta.\n'
    )

mostrar_instrucciones()

def mostrar_pregunta(indice):
    print('Pregunta:', Pregs.loc[indice, 'Preguntes'])
    print('Respuesta 1:', Pregs.loc[indice, 'A'])
    print('Respuesta 2:', Pregs.loc[indice, 'B'])
    print('Respuesta 3:', Pregs.loc[indice, 'C'])
    print('Respuesta 4:', Pregs.loc[indice, 'D'])

while True:
    numero_aleatorio = random.randrange(len(Pregs))

    mostrar_pregunta(numero_aleatorio)

    while True:

        resposta = input('\n¿Cuál es la respuesta? ').strip()
        resposta_minuscula = resposta.lower()

        if resposta_minuscula == 'terminar':
            clear_output(wait=True)
            print('\nFin de la sesión de estudio.\n')
            break

        elif resposta_minuscula == 'pasar':
            clear_output(wait=True)
            break

        elif resposta not in ['1', '2', '3', '4']:
            print('\nEntrada no válida.')
            print('Introduce 1, 2, 3, 4, "Pasar" o "Terminar".\n')

        elif resposta == str(Pregs.loc[numero_aleatorio, 'Correcta']):
            clear_output(wait=True)
            print('\n¡Muy bien! Siguiente pregunta.\n')
            mostrar_instrucciones()
            break

        else:
            print('\nRespuesta incorrecta. Vuelve a intentarlo.\n')
            mostrar_pregunta(numero_aleatorio)

    if resposta_minuscula == 'terminar':
        break


'''
¡Suerte!
Sort!

Nostre Senyor ens ampare.
Salva.
'''