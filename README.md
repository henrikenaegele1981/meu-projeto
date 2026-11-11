# 🎬 Meu Estúdio

App que roda no seu computador para planejar, agendar e postar no Instagram (e, nas próximas partes, no TikTok).

**O que já funciona (Parte 1)**
- **Configurações:** conectar o Instagram pela API oficial colando o token. O app mostra o @ conectado e renova o token sozinho a cada 30 dias (ele vale 60).
- **Agenda (Reels):** subir o vídeo, escrever a legenda, escolher dia e hora, marcar collab. A fila mostra o status de cada post (agendado, postando, publicado, erro) e a mensagem quando dá erro. Dá para editar, cancelar e tentar de novo.
- **Vigia:** confere a fila a cada 15 segundos e posta na hora marcada. Se o PC estava desligado na hora, ele posta assim que o app abrir.

**Próximas partes:** TikTok, Carrosséis, Painel e Posts.

---

## 1. Instalar (só uma vez)

1. Instale o **Python** em https://www.python.org/downloads/. Na primeira tela do instalador, marque **"Add python.exe to PATH"**.
2. Baixe este projeto: na página do repositório no GitHub, clique em **Code → Download ZIP** e extraia numa pasta **fora do OneDrive** (por exemplo `C:\MeuEstudio`).
3. Dê dois cliques em **`instalar.bat`**.

## 2. Abrir o app

- Dê dois cliques em **`iniciar.bat`**. O navegador abre sozinho em http://localhost:5252.
- Deixe a janela preta aberta (pode minimizar). Se fechar, o app desliga e não posta.
- **Para abrir sozinho quando o PC ligar:** dê dois cliques em `ligar_com_windows.bat`. O app passa a ficar escondido em segundo plano, e para ver as telas é só abrir http://localhost:5252 ou rodar o `iniciar.bat`. Para desfazer, use `desligar_do_windows.bat`.

> O vigia só posta enquanto o app estiver aberto e o PC ligado. Se o PC estiver desligado na hora marcada, o post sai assim que o app abrir de novo.

## 3. Conectar o Instagram

1. **Conta profissional:** no Instagram, vá em Configurações → Tipo de conta e ferramentas e mude para **Criador de conteúdo** ou **Comercial**.
2. **Conta de desenvolvedor:** entre em https://developers.facebook.com com o seu Facebook e aceite o cadastro de desenvolvedor.
3. **Criar o app:** Meus apps → Criar app → caso de uso **"Gerenciar mensagens e conteúdo no Instagram"** → dê um nome (ex.: Meu Estúdio) → Criar.
4. **Gerar o token:** no painel do app, vá em Casos de uso → Instagram → **Configuração da API com login do Instagram** → Gerar tokens de acesso → Adicionar conta → entre no seu Instagram e autorize → **Gerar token**.
5. **Permissões:** deixe marcadas:
   - `instagram_business_basic`
   - `instagram_business_content_publish` (para postar)
   - `instagram_business_manage_insights` (para o Painel; sem ela o Painel fica vazio)
6. Copie o token e cole em **Configurações → Instagram** no Meu Estúdio.

Observações:
- Não precisa publicar o app nem pedir revisão da Meta: postando na sua própria conta, ele funciona em modo de desenvolvimento.
- Se o token vencer (por exemplo, se o app ficou mais de 60 dias sem abrir), gere outro no passo 4.
- **Nunca mande o token para ninguém nem coloque no código.**

## Onde ficam os seus dados

Tudo fica em `%LOCALAPPDATA%\MeuEstudio\` (cole esse endereço na barra do Explorador de Arquivos), nunca na pasta do código:
- `config.json`: o token do Instagram (é segredo)
- `fila.json`: os posts agendados
- `midia\`: os vídeos que você subiu
- `estudio.log`: o registro do que o app fez, útil quando algo dá errado

## Como o Reel é postado

A API do Instagram só aceita vídeo que esteja num link público. Por isso, na hora de postar, o app sobe o vídeo em **litterbox.catbox.moe**, que apaga o arquivo sozinho depois de 1 hora. O Instagram busca o vídeo nesse link, processa e publica. Durante essa 1 hora, quem tiver o link consegue ver o vídeo, mas ele já vai ser publicado no seu perfil de qualquer jeito.

Requisitos do Instagram para Reels: arquivo MP4 ou MOV, de preferência vertical (9:16), com 3 segundos a 15 minutos.
