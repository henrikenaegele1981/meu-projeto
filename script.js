/* =========================================================
   CONFIGURAÇÃO: edite só este bloco
   ========================================================= */
const CONFIG = {
  // WhatsApp do Fred (quem conduz a conversa), só números, com 55 + DDD
  whatsapp: '5522981173962',

  // Número do registro no CRN
  crn: '00000',

  // OPCIONAL: endereço que recebe os contatos (Google Planilhas via Apps Script, Make, Zapier, n8n...).
  // Se ficar vazio, nada é enviado: o contato só chega quando a pessoa manda a mensagem no WhatsApp.
  webhook: '',
};

/* =========================================================
   PERGUNTAS
   multi: true → "Marque quantas quiser"
   ========================================================= */
const PERGUNTAS = [
  {
    id: 'objetivo',
    titulo: 'Qual é o seu objetivo principal?',
    opcoes: [
      ['emagrecer', 'Emagrecer e reduzir gordura'],
      ['massa', 'Ganhar massa muscular'],
      ['definicao', 'Definição e desempenho no treino'],
      ['saude', 'Melhorar a saúde e a autoestima'],
      ['comer', 'Aprender a comer melhor, sem neura'],
    ],
  },
  {
    id: 'treino',
    titulo: 'Como está o seu treino hoje?',
    opcoes: [
      ['nao', 'Não treino'],
      ['iniciante', 'Comecei há pouco (menos de 6 meses)'],
      ['regular', 'Treino com regularidade há mais de 6 meses'],
      ['avancado', 'Treino pesado há anos'],
    ],
  },
  {
    id: 'historico',
    titulo: 'Qual frase mais parece com você?',
    opcoes: [
      ['nunca', 'Nunca fiz dieta de verdade'],
      ['larga', 'Começo a dieta, mas não consigo manter'],
      ['semresultado', 'Treino, faço dieta e não vejo resultado'],
      ['tentou', 'Já tentei de tudo e não sei mais o que fazer'],
    ],
  },
  {
    id: 'trava',
    titulo: 'O que mais te atrapalha hoje?',
    apoio: 'Marque quantas quiser.',
    multi: true,
    opcoes: [
      ['fome', 'Fome e vontade de doce'],
      ['fds', 'O fim de semana desfaz a semana'],
      ['tempo', 'Falta de tempo'],
      ['naosei', 'Não sei o que nem quanto comer'],
      ['info', 'Cada lugar da internet fala uma coisa'],
      ['ansiedade', 'Ansiedade e beliscar o dia todo'],
      ['alcool', 'Bebida e vida social'],
    ],
  },
  {
    id: 'rotina',
    titulo: 'Como é a sua rotina?',
    opcoes: [
      ['comercial', 'Trabalho em horário comercial'],
      ['turnos', 'Trabalho em turnos ou plantões'],
      ['rua', 'Rotina corrida, como muito na rua'],
      ['flexivel', 'Rotina flexível ou trabalho em casa'],
    ],
  },
  {
    id: 'cozinha',
    titulo: 'Quanto tempo você tem para preparar comida?',
    opcoes: [
      ['nada', 'Quase nenhum'],
      ['marmita', 'Dá para fazer marmita alguns dias'],
      ['todo', 'Cozinho todo dia'],
    ],
  },
  {
    id: 'espelho',
    titulo: 'Como você se sente com o seu corpo hoje?',
    apoio: 'Seja sincero. Ninguém vê isso além do Fred.',
    opcoes: [
      ['evita', 'Evito foto e espelho'],
      ['incomoda', 'Me incomoda, mas vou levando'],
      ['evoluir', 'Gosto, mas quero evoluir'],
      ['performance', 'Estou bem, meu foco é performance'],
    ],
  },
  {
    id: 'modalidade',
    titulo: 'Onde você prefere ser atendido?',
    opcoes: [
      ['cordeiro', 'Presencial em Cordeiro (RJ)'],
      ['friburgo', 'Presencial em Nova Friburgo (RJ)'],
      ['online', 'Online, moro em outra cidade'],
      ['tantofaz', 'Tanto faz, quero entender melhor'],
    ],
  },
  {
    id: 'quando',
    titulo: 'Quando você quer começar?',
    opcoes: [
      ['semana', 'Essa semana'],
      ['mes', 'Ainda este mês'],
      ['3meses', 'Nos próximos 3 meses'],
      ['pesquisando', 'Ainda estou pesquisando'],
    ],
  },
];

/* =========================================================
   TEXTOS DO RESULTADO
   ========================================================= */
const PERFIS = {
  nunca: {
    titulo: 'Perfil: o primeiro passo',
    resumo: 'Você está no melhor momento para começar certo: sem vício de dieta maluca e sem trauma de restrição. O risco aqui é começar pelo caminho errado e achar que "dieta não é pra você".',
  },
  larga: {
    titulo: 'Perfil: o recomeço eterno',
    resumo: 'Segunda você começa, quarta já era. Isso não é falta de força de vontade: é sinal de um plano que não cabe na sua vida. Dieta que você não consegue manter tem prazo de validade.',
  },
  semresultado: {
    titulo: 'Perfil: esforço sem estratégia',
    resumo: 'Você já faz a parte difícil, que é treinar e se esforçar. O que falta é estratégia: saber quanto, quando e por quê. Sem isso, o resultado não aparece e a frustração aparece no lugar.',
  },
  tentou: {
    titulo: 'Perfil: cansado de tentar',
    resumo: 'Você já tentou de tudo, e é justamente esse "tudo" que confunde. Cada método puxa para um lado. O que você precisa agora é de um caminho só, feito para você, e de alguém para te acompanhar nele.',
  },
};

const PONTOS = {
  // travas
  fome: ['Fome e vontade de doce', 'Normalmente é sinal de um plano restritivo demais ou mal distribuído ao longo do dia. Dá para emagrecer sem passar fome e sem cortar tudo o que você gosta.'],
  fds: ['O fim de semana desfaz a semana', 'Proibir o fim de semana não funciona. O que funciona é ter uma estratégia para ele, que conte com a pizza, o churrasco e a vida social.'],
  tempo: ['Falta de tempo', 'A alimentação tem que se adaptar à sua rotina, e não o contrário. Existem estratégias simples para quem não tem tempo nem para pensar no que vai comer.'],
  naosei: ['Não saber o que nem quanto comer', 'Sem saber quantidade e distribuição, a dieta vira chute. E chute às vezes acerta, mas quase nunca se mantém.'],
  info: ['Informação demais, direção de menos', 'Informação genérica não substitui uma avaliação do seu caso. O que serve para o influenciador pode não servir para você.'],
  ansiedade: ['Beliscar o dia todo', 'Beliscar costuma vir de refeições mal montadas, horários bagunçados ou ansiedade. Entender o gatilho é mais eficiente do que só "ter força de vontade".'],
  alcool: ['Bebida e vida social', 'Ninguém precisa virar ermitão. Mas álcool tem bastante caloria, não sacia e atrapalha o sono e a recuperação. Dá para encaixar com estratégia, sabendo o custo.'],
  // treino x objetivo
  massa_semtreino: ['Massa muscular começa no treino', 'Para ganhar massa, a alimentação precisa andar junto com um treino de força. Sem esse estímulo, a comida a mais tende a virar gordura, não músculo.'],
  emagrecer_semtreino: ['Emagrecer sem perder músculo', 'Cortar comida sem treinar pode baixar o peso, mas parte do que vai embora é músculo. Alimentação certa somada a algum treino de força muda o desenho do corpo.'],
  avancado: ['Quem treina há anos precisa de ajuste fino', 'Para quem já treina pesado, o que trava o resultado é o detalhe: distribuição de proteína, carboidrato em volta do treino, recuperação e periodização da dieta.'],
  iniciante: ['Começo de treino é janela de ouro', 'Quem está começando costuma responder rápido quando treino e alimentação andam juntos. É a hora de construir o hábito certo desde o início.'],
  // rotina
  turnos: ['Rotina em turnos', 'Plantão e turno bagunçam fome, sono e horário. O plano precisa ser montado em cima da sua escala, e não de um horário "padrão" que você não tem.'],
  rua: ['Comer na rua', 'Comer fora não é o problema. O problema é não saber escolher. Dá para montar um plano que funciona no restaurante, na padaria e no lanche rápido.'],
  nada: ['Pouco tempo para cozinhar', 'Dá para ter uma alimentação boa com o mínimo de preparo: opções práticas, compras inteligentes e um plano que não exige que você vire chef.'],
  // autoestima
  evita: ['A relação com o espelho', 'Quando a pessoa evita foto e espelho, o objetivo não é só estético. É voltar a se sentir bem consigo. Por isso o processo precisa ser possível, e não um castigo.'],
};

/* =========================================================
   LÓGICA (não precisa mexer daqui pra baixo)
   ========================================================= */
(function () {
  const $ = (s) => document.querySelector(s);
  const telas = ['#tela-intro', '#tela-quiz', '#tela-dados', '#tela-resultado'];
  const respostas = {};
  let atual = 0;
  let dados = { nome: '', whatsapp: '' };

  const mostrar = (id) => {
    telas.forEach((t) => ($(t).hidden = t !== id));
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  const letras = 'ABCDEFGHIJ';

  function progresso(i) {
    const pct = Math.round((i / (PERGUNTAS.length + 1)) * 100);
    $('#rota-feito').style.width = pct + '%';
    $('#rota-marcador').style.left = pct + '%';
    $('#tela-quiz .rota').setAttribute('aria-valuenow', pct);
  }

  function renderPergunta() {
    const q = PERGUNTAS[atual];
    const sel = respostas[q.id] || (q.multi ? [] : null);
    progresso(atual);

    const box = $('#pergunta');
    box.innerHTML = `
      <div class="entra">
        <p class="contador">${atual + 1} DE ${PERGUNTAS.length}</p>
        <h2 class="titulo-pergunta">${q.titulo}</h2>
        ${q.apoio ? `<p class="pergunta-apoio">${q.apoio}</p>` : ''}
        <ul class="opcoes">
          ${q.opcoes.map(([v, txt], k) => {
            const on = q.multi ? sel.includes(v) : sel === v;
            return `<li><button type="button" class="opcao" data-v="${v}" aria-pressed="${on}">
                      <span class="letra">${letras[k]}</span><span>${txt}</span></button></li>`;
          }).join('')}
        </ul>
        <div class="acoes">
          <button type="button" class="voltar" id="voltar-q">Voltar</button>
          ${q.multi ? `<button type="button" class="cta" id="continuar" ${sel.length ? '' : 'disabled'}>Continuar
            <svg viewBox="0 0 20 20" width="18" height="18" aria-hidden="true"><path d="M4 10h11m-4-5 5 5-5 5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></button>` : ''}
        </div>
      </div>`;

    box.querySelectorAll('.opcao').forEach((b) =>
      b.addEventListener('click', () => {
        const v = b.dataset.v;
        if (q.multi) {
          const arr = respostas[q.id] || [];
          respostas[q.id] = arr.includes(v) ? arr.filter((x) => x !== v) : [...arr, v];
          b.setAttribute('aria-pressed', respostas[q.id].includes(v));
          $('#continuar').disabled = !respostas[q.id].length;
        } else {
          respostas[q.id] = v;
          box.querySelectorAll('.opcao').forEach((o) => o.setAttribute('aria-pressed', o === b));
          setTimeout(avancar, 220);
        }
      })
    );
    $('#voltar-q').addEventListener('click', voltar);
    if (q.multi) $('#continuar').addEventListener('click', avancar);
  }

  function avancar() {
    if (atual < PERGUNTAS.length - 1) { atual++; renderPergunta(); }
    else { mostrar('#tela-dados'); setTimeout(() => $('#form-dados input').focus({ preventScroll: true }), 300); }
  }
  function voltar() {
    if (atual > 0) { atual--; renderPergunta(); }
    else mostrar('#tela-intro');
  }

  // ---------- resultado ----------
  function montarPontos(r) {
    const lista = [];
    const add = (k) => { if (PONTOS[k] && !lista.includes(k)) lista.push(k); };

    (r.trava || []).slice(0, 2).forEach(add);
    if (r.treino === 'nao' && r.objetivo === 'massa') add('massa_semtreino');
    if (r.treino === 'nao' && r.objetivo === 'emagrecer') add('emagrecer_semtreino');
    if (r.treino === 'avancado') add('avancado');
    if (r.treino === 'iniciante') add('iniciante');
    if (r.rotina === 'turnos') add('turnos');
    if (r.rotina === 'rua') add('rua');
    if (r.cozinha === 'nada') add('nada');
    if (r.espelho === 'evita') add('evita');
    (r.trava || []).slice(2).forEach(add);
    return lista.slice(0, 4);
  }

  const textoDe = (id, v) => {
    const q = PERGUNTAS.find((x) => x.id === id);
    const pega = (val) => (q.opcoes.find(([k]) => k === val) || [, val])[1];
    return Array.isArray(v) ? v.map(pega).join(', ') : pega(v);
  };

  function renderResultado() {
    const r = respostas;
    const perfil = PERFIS[r.historico] || PERFIS.semresultado;
    const primeiro = dados.nome.trim().split(/\s+/)[0];

    $('#res-titulo').textContent = perfil.titulo;
    $('#res-resumo').textContent = `${primeiro}, ${perfil.resumo.charAt(0).toLowerCase()}${perfil.resumo.slice(1)}`;

    const pontos = montarPontos(r);
    $('#res-pontos').innerHTML = pontos
      .map((k) => `<li><b>${PONTOS[k][0]}</b><span>${PONTOS[k][1]}</span></li>`)
      .join('');

    const mod = {
      cordeiro: 'No presencial em Cordeiro você ainda faz avaliação de composição corporal por bioimpedância e ganha uma garrafa de água de cortesia na primeira consulta.',
      friburgo: 'No presencial em Nova Friburgo você ainda faz avaliação de composição corporal por bioimpedância e ganha uma garrafa de água de cortesia na primeira consulta.',
      online: 'No online a consulta é por vídeo, ao vivo, com a dieta montada na hora, e a evolução é acompanhada por fotos e informações que você envia.',
      tantofaz: 'Você pode fazer presencial (Cordeiro ou Nova Friburgo, com bioimpedância) ou online, por vídeo, de qualquer lugar do Brasil.',
    };
    $('#res-modalidade').textContent = mod[r.modalidade] || mod.tantofaz;

    const msg =
`Oi Fred! Fiz o Diagnóstico do Shape.
Nome: ${dados.nome.trim()}
Resultado: ${perfil.titulo.replace('Perfil: ', '')}
Objetivo: ${textoDe('objetivo', r.objetivo)}
Treino: ${textoDe('treino', r.treino)}
O que me atrapalha: ${textoDe('trava', r.trava || [])}
Atendimento: ${textoDe('modalidade', r.modalidade)}
Quero começar: ${textoDe('quando', r.quando)}

Quero entender como funciona o acompanhamento.`;
    $('#res-whats').href = `https://wa.me/${CONFIG.whatsapp}?text=${encodeURIComponent(msg)}`;

    mostrar('#tela-resultado');
  }

  function enviarLead() {
    if (!CONFIG.webhook) return;
    const corpo = {
      data: new Date().toISOString(),
      nome: dados.nome.trim(),
      whatsapp: dados.whatsapp,
      ...Object.fromEntries(PERGUNTAS.map((q) => [q.id, textoDe(q.id, respostas[q.id] ?? '')])),
      perfil: (PERFIS[respostas.historico] || {}).titulo || '',
    };
    try {
      fetch(CONFIG.webhook, { method: 'POST', mode: 'no-cors', headers: { 'Content-Type': 'text/plain' }, body: JSON.stringify(corpo) });
    } catch (e) { /* não bloqueia o resultado */ }
  }

  // ---------- eventos ----------
  $('#btn-comecar').addEventListener('click', () => { atual = 0; renderPergunta(); mostrar('#tela-quiz'); });
  $('#voltar-dados').addEventListener('click', () => { atual = PERGUNTAS.length - 1; renderPergunta(); mostrar('#tela-quiz'); });
  $('#refazer').addEventListener('click', () => {
    Object.keys(respostas).forEach((k) => delete respostas[k]);
    mostrar('#tela-intro');
  });

  $('#form-dados').addEventListener('submit', (e) => {
    e.preventDefault();
    const f = e.target;
    const nome = f.nome.value.trim();
    const fone = f.whatsapp.value.replace(/\D/g, '');
    const erro = $('#erro-dados');
    if (nome.length < 2) { erro.textContent = 'Digite o seu nome.'; erro.hidden = false; f.nome.focus(); return; }
    if (fone.length < 10 || fone.length > 13) { erro.textContent = 'Digite um WhatsApp válido, com DDD.'; erro.hidden = false; f.whatsapp.focus(); return; }
    erro.hidden = true;
    dados = { nome, whatsapp: fone };
    enviarLead();
    renderResultado();
  });

  // máscara simples de telefone
  $('#form-dados [name=whatsapp]').addEventListener('input', (e) => {
    const d = e.target.value.replace(/\D/g, '').slice(0, 11);
    e.target.value = d.length > 6
      ? `(${d.slice(0, 2)}) ${d.slice(2, d.length - 4)}-${d.slice(-4)}`
      : d.length > 2 ? `(${d.slice(0, 2)}) ${d.slice(2)}` : d;
  });

  document.querySelectorAll('.js-crn').forEach((el) => (el.textContent = CONFIG.crn));
})();
