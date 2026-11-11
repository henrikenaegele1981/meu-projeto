"""Gera o token do Instagram pelo login direto do Instagram (sem passar pelo Facebook).

Use quando o botao "Gerar token" do painel da Meta der erro.
Nada e enviado para fora alem dos servidores oficiais do Instagram.
"""
from __future__ import annotations

import json
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
import webbrowser

REDIRECT = "https://localhost/"
PERMISSOES = ",".join([
    "instagram_business_basic",
    "instagram_business_content_publish",
    "instagram_business_manage_insights",
])


class Erro(Exception):
    pass


def _pedir(url: str, dados: dict | None = None) -> dict:
    corpo = urllib.parse.urlencode(dados).encode() if dados is not None else None
    try:
        with urllib.request.urlopen(url, data=corpo, timeout=60) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        texto = e.read().decode(errors="replace")
        try:
            info = json.loads(texto)
            msg = info.get("error_message") or info.get("error", {}).get("message") or texto
        except json.JSONDecodeError:
            msg = texto
        raise Erro(msg[:500])
    except urllib.error.URLError as e:
        raise Erro(f"Sem conexao com o Instagram: {e.reason}")


def extrair_codigo(colado: str) -> str:
    colado = colado.strip()
    if "code=" in colado:
        consulta = urllib.parse.urlparse(colado).query or colado.split("?", 1)[-1]
        codigo = urllib.parse.parse_qs(consulta).get("code", [""])[0]
    else:
        codigo = colado
    codigo = codigo.split("#")[0].strip()
    if not codigo:
        raise Erro("Nao achei o codigo no endereco colado. Copie o endereco inteiro da barra do navegador.")
    return codigo


def copiar(texto: str) -> bool:
    if sys.platform != "win32":
        return False
    try:
        subprocess.run("clip", input=texto.encode("utf-16-le"), check=True, shell=True)
        return True
    except (OSError, subprocess.CalledProcessError):
        return False


def main() -> None:
    print("=== Gerar token do Instagram (login direto) ===\n")
    print("No painel do app da Meta, copie o 'ID do app do Instagram' e a")
    print("'Chave secreta do app do Instagram' (botao Mostrar).\n")
    app_id = input("Cole o ID do app do Instagram e aperte Enter: ").strip()
    segredo = input("Cole a chave secreta do app do Instagram e aperte Enter: ").strip()
    if not app_id.isdigit() or not segredo:
        raise Erro("O ID deve ter so numeros e a chave secreta nao pode ficar vazia.")

    url = "https://www.instagram.com/oauth/authorize?" + urllib.parse.urlencode({
        "enable_fb_login": "0",
        "force_authentication": "1",
        "client_id": app_id,
        "redirect_uri": REDIRECT,
        "response_type": "code",
        "scope": PERMISSOES,
    })
    print("\nVou abrir o Instagram no navegador. Entre na sua conta e clique em Permitir.")
    print("Depois disso o navegador vai mostrar uma pagina de ERRO (localhost). E normal!")
    print("Copie o endereco INTEIRO da barra do navegador (comeca com https://localhost/?code=).\n")
    print("Se o navegador nao abrir, copie este link e abra manualmente:")
    print(url + "\n")
    webbrowser.open(url)

    codigo = extrair_codigo(input("Cole aqui o endereco copiado e aperte Enter: "))

    curto = _pedir("https://api.instagram.com/oauth/access_token", {
        "client_id": app_id,
        "client_secret": segredo,
        "grant_type": "authorization_code",
        "redirect_uri": REDIRECT,
        "code": codigo,
    })
    if isinstance(curto.get("data"), list) and curto["data"]:
        curto = curto["data"][0]
    token_curto = curto.get("access_token")
    if not token_curto:
        raise Erro(f"Resposta inesperada do Instagram: {str(curto)[:300]}")

    longo = _pedir("https://graph.instagram.com/access_token?" + urllib.parse.urlencode({
        "grant_type": "ig_exchange_token",
        "client_secret": segredo,
        "access_token": token_curto,
    }))
    token = longo.get("access_token") or token_curto

    conta = _pedir("https://graph.instagram.com/v21.0/me?" + urllib.parse.urlencode({
        "fields": "user_id,username", "access_token": token,
    }))

    print(f"\nDeu certo! Conta: @{conta.get('username', '?')}")
    if copiar(token):
        print("O token ja foi COPIADO. Va no Meu Estudio > Configuracoes > Instagram,")
        print("clique no campo, aperte Ctrl+V e salve.")
    else:
        print("Copie o token abaixo e cole no Meu Estudio > Configuracoes > Instagram:\n")
        print(token)
    print("\nNao mande o token para ninguem.")


if __name__ == "__main__":
    try:
        main()
    except Erro as e:
        print(f"\nDeu erro: {e}")
        print("Tire uma foto desta tela (sem mostrar a chave secreta) e mande para o Claude.")
    except KeyboardInterrupt:
        pass
    input("\nAperte Enter para fechar.")
