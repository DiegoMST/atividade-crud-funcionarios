"""Consultas SQL diretas no MySQL configurado no Django."""
from django.db import connection

print("Banco de dados:", connection.settings_dict["NAME"])
print("Gerenciador:", connection.vendor)
print("Tabela: app_funcionario")
print()
with connection.cursor() as cursor:
    cursor.execute("SELECT COUNT(*) FROM app_funcionario")
    total = cursor.fetchone()[0]
    print("Total de funcionarios cadastrados:", total)
    print()
    cursor.execute("SELECT id, nome, cpf, email, remuneracao FROM app_funcionario ORDER BY id")
    registros = cursor.fetchall()
    if not registros:
        print("Nenhum funcionario cadastrado. Cadastre pelo sistema e consulte novamente.")
    else:
        for id_, nome, cpf, email, remuneracao in registros:
            print(f"ID: {id_} | Nome: {nome} | CPF: {cpf} | E-mail: {email} | Remuneracao: R$ {remuneracao}")
