from datetime import datetime, timedelta
import pytz

data_hora_atual = datetime.now(pytz.timezone("America/Recife"))
data_hora_str = "2023-10-20 10:20"
mascara_ptbr = "%d/%m/%Y %H:%M"
mascara_en = "%Y-%m-%d %a"
intervalo_tempo = 3

'''
Imprime data e hora calculados de acordo com periodização especificada (intervalo_tempo),
no formato padrão do tipo objeto datetime:
'''
data_hora_anterior = data_hora_atual - timedelta(days = intervalo_tempo)
print(data_hora_anterior)
print(type(data_hora_anterior))

'''
Imprime data e hora calculados de acordo com periodização especificada (intervalo_tempo),
no formato especificado do tipo string:
'''
data_hora_anterior_str = data_hora_anterior.strftime(mascara_ptbr)
print(data_hora_anterior_str)
print(type(data_hora_anterior_str))

'''
Imprime data e hora calculados de acordo com periodização especificada (intervalo_tempo),
no formato convertido para o padrão do tipo objeto datetime, com as mesmas especificações
descritas na variável string (mascara_ptbr):
'''
data_hora_anterior_str_conv = datetime.strptime(data_hora_anterior_str, mascara_ptbr)
print(data_hora_anterior_str_conv)
print(type(data_hora_anterior_str_conv))