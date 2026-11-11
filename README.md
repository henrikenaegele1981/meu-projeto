# 🎬 Meu Estúdio

App que roda no seu computador para planejar, agendar e postar no Instagram (e, nas próximas partes, no TikTok).

**O que já funciona (Parte 1)**
- **Configurações:** conectar o Instagram pela API oficial colando o token (funciona com apps novos da Meta, de login unificado, e com apps antigos). O app mostra o @ conectado.
- **Agenda (Reels e fotos):** subir o vídeo (Reel) ou uma foto (post estático), escrever a legenda, escolher dia e hora, marcar collab. A fila mostra o status de cada post (agendado, postando, publicado, erro) e a mensagem quando dá erro. Dá para editar, cancelar e tentar de novo.
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

Primeiro, nos dois casos:
1. **Conta profissional:** no Instagram, vá em Configurações → Tipo de conta e ferramentas e mude para **Criador de conteúdo** ou **Comercial**.
2. **Conta de desenvolvedor:** entre em https://developers.facebook.com com o seu Facebook e aceite o cadastro de desenvolvedor.
3. **Criar o app:** Meus apps → Criar app → caso de uso **"Gerenciar mensagens e conteúdo no Instagram"** → dê um nome (ex.: Meu Estúdio) → Criar.

Depois, veja qual tela o seu app mostra em Casos de uso → Instagram → Personalizar:

### Apps novos ("login unificado")

Se aparecer o aviso *"A configuração da API com login do Instagram não está disponível para apps mais recentes"*, o seu app usa o login unificado. O token vem de um **usuário do sistema** do seu portfólio empresarial:

1. Em https://business.facebook.com, crie (ou abra) o seu **portfólio empresarial**.
2. **Configurações do negócio → Contas → Contas do Instagram → Adicionar:** conecte o seu Instagram.
3. **Configurações do negócio → Contas → Apps → Adicionar:** conecte o app que você criou (pelo ID do app).
4. **Configurações do negócio → Usuários → Usuários do sistema → Adicionar:** crie um usuário com função **Administrador**.
5. Nesse usuário, **Atribuir ativos:** dê **controle total** do app e da conta do Instagram.
6. **Gerar token:** escolha o app, validade **Nunca** e marque as permissões do Instagram (as de publicar conteúdo, informações básicas e insights).
7. No Meu Estúdio, em **Configurações → Instagram**, cole o token e preencha o **ID da conta do Instagram** (o número que aparece embaixo do seu @ na seção "Gerar tokens de acesso" do painel do app).

### Apps antigos ("login do Instagram")

1. No painel do app: Casos de uso → Instagram → **Configuração da API com login do Instagram** → Gerar tokens de acesso → Adicionar conta → entre no seu Instagram e autorize → **Gerar token**.
2. Permissões: `instagram_business_basic`, `instagram_business_content_publish` e `instagram_business_manage_insights`.
3. Cole o token em **Configurações → Instagram** (o ID não é necessário). O app renova esse token sozinho a cada 30 dias.

Observações:
- Não precisa publicar o app nem pedir revisão da Meta: postando na sua própria conta, ele funciona em modo de desenvolvimento.
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

Requisitos para fotos (post estático): JPG, PNG ou WEBP (o app converte para JPG), com proporção entre 4:5 (vertical, 1080×1350) e 1,91:1 (horizontal). Quadrada (1080×1080) também serve. Foto de story (9:16) não é aceita no feed.
