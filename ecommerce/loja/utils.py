import csv
from django.http import HttpResponse

def exportar_csv(info, relatorio):
    colunas = info.model._meta.fields
    nomes_colunas = [colunas.name for colunas in colunas]

    resposta = HttpResponse(content_type="text/csv")

    if relatorio == "compras":
        resposta["Content-Disposition"] = "attachment; filename=compras.csv"

    elif relatorio == "usuarios":
        resposta["Content-Disposition"] = "attachment; filename=usuarios.csv"

    elif relatorio == "produtos":
        resposta["Content-Disposition"] = "attachment; filename=produtos.csv"

    cr_csv = csv.writer(resposta, delimiter=";")

    cr_csv.writerow(nomes_colunas)

    for linha in info.values_list():
        cr_csv.writerow(linha)

    return resposta