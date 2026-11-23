# Formato de mapa animado do Paulo Villarinho

Base: pesquisa de formatos de mapa animado (Agente Roteirista, 22/11/2026) + nicho dólar e câmbio + perfil de trader do Paulo.
Regra da pesquisa: não usar o que virou template (zoom da Terra, país aceso com emoji, countryball, estilo Harris pronto) nem os 3 estilos dos perfis irmãos (globo noturno do José, cards com emoji, HUD do Henrike).

> **Atenção:** o vídeo 1 ("De R$ 4,97 a R$ 5,81") foi feito com o **globo noturno**, que é o estilo do José. Serve como teste, mas não deve virar a identidade do Paulo.

## A pergunta certa
Qual objeto do dia a dia do nicho do Paulo carrega o número?
No nicho dele, o número **é o gráfico do dólar**. O Paulo é trader, vive olhando a cotação. Ninguém no mapa animado brasileiro liga o **gráfico real** ao **lugar** que mexeu nele.

---

## ⭐ Recomendado: "Gráfico-Mapa" (cada pico do dólar tem um endereço)
Prévia estática: `mock-grafico-mapa.png`.

**Como funciona**
- O vídeo abre num **painel de cotação estilo split-flap** (letreiro de aeroporto ou casa de câmbio) com as cifras girando até a cotação do dia. Esse é o gancho em movimento já no primeiro quadro.
- A **linha real do dólar** (série oficial do Banco Central, SGS 1) se desenha da esquerda para a direita, como na tela de um trader.
- A cada pico ou queda, a linha "puxa um barbante" vermelho até um **mapa claro, de papel**, logo abaixo. O alfinete cai no lugar que causou o movimento (Brasília, Washington, Pequim, Riad…) e a câmera dá zoom nele por 3 a 5 s.
- O painel vira de novo a cada capítulo (tique-taque das cifras = marcador de capítulo).
- O fecho volta ao painel com a cotação final (loop).

**Por que é o certo para o Paulo**
- É autoral e físico: dado real do BC, não template. Nenhuma IA gera isso certo, porque o dado precisa ser exato.
- É a identidade do Paulo: **o trader explica o gráfico**. O formato vira assinatura reconhecível ("cada pico tem um endereço").
- Visual claro e de papel, oposto ao globo noturno e ao HUD dos perfis irmãos.
- Serve para quase toda pauta do banco: eleição, Fed, tarifa, petróleo, BRICS, ouro (troca a série: USD/BRL, ouro, petróleo).

**Paleta:** papel creme `#F3EEE3`, tinta `#14202B`, verde trader `#1B6E45`, alfinete vermelho `#C0392B`, cifras amarelas `#F5C542` sobre placa preta.
**Frase fixa de abertura (assinatura):** "Todo pico do dólar tem um endereço. Hoje é…"
**Duração:** 30 a 60 s, voz humana ou voz com cara humana, sem pausas cortadas.
**Ritmo:** algo novo na tela a cada 2 a 3 s (cifra girando, linha andando, barbante, alfinete, zoom, número).

## Alternativas

**2. "Painel de Embarque"**
- Uma tela de aeroporto em que cada linha é um destino com a cotação e o custo real da viagem (IOF de 3,5% + spread).
- As linhas viram como split-flap e o mapa mostra a rota da viagem.
- Ótimo para pautas de bolso (viagem, compra no exterior, Black Friday).
- Ponto de atenção: fica perto do "recibo", e o "Cupom de Fronteira" foi reprovado para o Vinícius.

**3. "Mesa de Operação"**
- O mapa impresso fica numa mesa, filmado de cima, com a mão do Paulo, alfinetes e o celular com o gráfico aberto. Por cima, overlay de papel em stop-motion a 12 fps.
- Coloca o Paulo dentro do mapa sem ele precisar falar para a câmera.
- Exige uma gravação simples dele (só mãos, 2 a 3 min por vídeo).

## Como validar
1. Publicar a mesma pauta em dois formatos: vídeo 1 no globo e a versão Gráfico-Mapa.
2. Comparar a retenção aos 3 s e o número de compartilhamentos.
3. Abrir logado a aba Reels das referências e anotar as views dos últimos 12 vídeos.

## Fonte dos dados
- Cotação: Banco Central, SGS série 1 (dólar comercial, venda), por meio da API pública `api.bcb.gov.br/dados/serie/bcdata.sgs.1/dados`.
- Arquivo `ptax.json`: série de 02/01 a 19/11/2026.
