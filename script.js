/* =========================================================
   CONFIGURAÇÃO: edite só este bloco
   ========================================================= */
const CONFIG = {
  // WhatsApp do Fred (quem conduz a conversa), só números, com 55 + DDD
  whatsapp: '5522981173962',

  // Número do registro no CRN
  crn: '00000',

  // Mostrar os preços dos planos na página? O briefing pede valores só na conversa privada,
  // por isso começa desligado. Para mostrar, troque para true.
  mostrarPrecos: false,

  // OPCIONAL: endereço que recebe os contatos do diagnóstico (Google Planilhas via Apps Script, Make, Zapier...).
  webhook: '',
};

/* =========================================================
   PLANOS
   ========================================================= */
const PLANOS = {
  semestral: {
    nome: 'Semestral',
    cta: 'Quero o semestral',
    duracao: '6 meses · 6 consultas',
    preco: '6x R$165',
    total: 'R$990 no total',
    selo: 'Mais escolhido',
    destaque: true,
    pra: 'Para quem quer mudar de vez, construir hábito e ter tempo de ver o resultado aparecer.',
    itens: [
      '6 consultas (inicial + 5 retornos)',
      'Retornos a cada 30 a 40 dias',
      'Dieta ajustada a cada retorno e entre consultas',
      'WhatsApp direto com o Fred por 6 meses',
      'Bioimpedância no atendimento presencial',
      'Melhor valor por consulta',
    ],
  },
  trimestral: {
    nome: 'Trimestral',
    cta: 'Quero o trimestral',
    duracao: '3 meses · 3 consultas',
    preco: '3x R$194',
    total: 'R$582 no total',
    pra: 'Para quem quer um empurrão de alguns meses para organizar a alimentação e pegar o ritmo.',
    itens: [
      '3 consultas (inicial + 2 retornos)',
      'Retornos a cada 30 a 40 dias',
      'Dieta ajustada a cada retorno e entre consultas',
      'WhatsApp direto com o Fred por 3 meses',
      'Bioimpedância no atendimento presencial',
    ],
  },
  avulsa: {
    nome: 'Consulta avulsa',
    cta: 'Quero uma consulta',
    duracao: 'Uma consulta, sem plano',
    preco: 'R$250',
    total: 'Retorno avulso: R$200',
    pra: 'Para quem quer uma orientação pontual e prefere decidir os próximos passos depois.',
    itens: [
      'Consulta completa de 45 a 90 min',
      'Dieta montada durante a consulta, com você',
      'Avaliação de suplementação, se fizer sentido',
      'Retornos podem ser marcados avulsos',
    ],
  },
};

/* =========================================================
   PERGUNTAS DO DIAGNÓSTICO (multi: true → marque quantas quiser)
   ========================================================= */
const PERGUNTAS = [
  { id: 'objetivo', titulo: 'Qual é o seu objetivo principal?', opcoes: [
    ['emagrecer', 'Emagrecer e reduzir gordura'],
    ['massa', 'Ganhar massa muscular'],
    ['definicao', 'Definição e desempenho no treino'],
    ['saude', 'Melhorar a saúde e a autoestima'],
    ['comer', 'Aprender a comer melhor, sem neura'],
  ] },
  { id: 'treino', titulo: 'Como está o seu treino hoje?', opcoes: [
    ['nao', 'Não treino'],
    ['iniciante', 'Comecei há pouco (menos de 6 meses)'],
    ['regular', 'Treino com regularidade há mais de 6 meses'],
    ['avancado', 'Treino pesado há anos'],
  ] },
  { id: 'historico', titulo: 'Qual frase mais parece com você?', opcoes: [
    ['nunca', 'Nunca fiz dieta de verdade'],
    ['larga', 'Começo a dieta, mas não consigo manter'],
    ['semresultado', 'Treino, faço dieta e não vejo resultado'],
    ['tentou', 'Já tentei de tudo e não sei mais o que fazer'],
  ] },
  { id: 'trava', titulo: 'O que mais te atrapalha hoje?', apoio: 'Marque quantas quiser.', multi: true, opcoes: [
    ['fome', 'Fome e vontade de doce'],
    ['fds', 'O fim de semana desfaz a semana'],
    ['tempo', 'Falta de tempo'],
    ['naosei', 'Não sei o que nem quanto comer'],
    ['info', 'Cada lugar da internet fala uma coisa'],
    ['ansiedade', 'Ansiedade e beliscar o dia todo'],
    ['alcool', 'Bebida e vida social'],
  ] },
  { id: 'rotina', titulo: 'Como é a sua rotina?', opcoes: [
    ['comercial', 'Trabalho em horário comercial'],
    ['turnos', 'Trabalho em turnos ou plantões'],
    ['rua', 'Rotina corrida, como muito na rua'],
    ['flexivel', 'Rotina flexível ou trabalho em casa'],
  ] },
  { id: 'espelho', titulo: 'Como você se sente com o seu corpo hoje?', apoio: 'Seja sincero. Ninguém vê isso além do Fred.', opcoes: [
    ['evita', 'Evito foto e espelho'],
    ['incomoda', 'Me incomoda, mas vou levando'],
    ['evoluir', 'Gosto, mas quero evoluir'],
    ['performance', 'Estou bem, meu foco é performance'],
  ] },
  { id: 'acompanhamento', titulo: 'Que tipo de acompanhamento você procura?', opcoes: [
    ['continuo', 'Quero alguém comigo até o resultado aparecer'],
    ['meses', 'Quero um empurrão de alguns meses'],
    ['pontual', 'Só quero uma orientação pontual'],
    ['naosei', 'Ainda não sei, quero entender melhor'],
  ] },
  { id: 'modalidade', titulo: 'Onde você prefere ser atendido?', opcoes: [
    ['cordeiro', 'Presencial em Cordeiro (RJ)'],
    ['friburgo', 'Presencial em Nova Friburgo (RJ)'],
    ['online', 'Online, moro em outra cidade'],
    ['tantofaz', 'Tanto faz, quero entender melhor'],
  ] },
  { id: 'quando', titulo: 'Quando você quer começar?', opcoes: [
    ['semana', 'Essa semana'],
    ['mes', 'Ainda este mês'],
    ['3meses', 'Nos próximos 3 meses'],
    ['pesquisando', 'Ainda estou pesquisando'],
  ] },
];

const PERFIS = {
  nunca: { titulo: 'Perfil: o primeiro passo', resumo: 'você está no melhor momento para começar certo: sem vício de dieta maluca e sem trauma de restrição. O risco aqui é começar pelo caminho errado e achar que "dieta não é pra você".' },
  larga: { titulo: 'Perfil: o recomeço eterno', resumo: 'segunda você começa, quarta já era. Isso não é falta de força de vontade: é sinal de um plano que não cabe na sua vida. Dieta que você não consegue manter tem prazo de validade.' },
  semresultado: { titulo: 'Perfil: esforço sem estratégia', resumo: 'você já faz a parte difícil, que é treinar e se esforçar. O que falta é estratégia: saber quanto, quando e por quê. Sem isso, o resultado não aparece e a frustração aparece no lugar.' },
  tentou: { titulo: 'Perfil: cansado de tentar', resumo: 'você já tentou de tudo, e é justamente esse "tudo" que confunde. Cada método puxa para um lado. O que você precisa agora é de um caminho só, feito para você, e de alguém para te acompanhar nele.' },
};

const PONTOS = {
  fome: ['Fome e vontade de doce', 'Normalmente é sinal de um plano restritivo demais ou mal distribuído ao longo do dia. Dá para emagrecer sem passar fome e sem cortar tudo o que você gosta.'],
  fds: ['O fim de semana desfaz a semana', 'Proibir o fim de semana não funciona. O que funciona é ter uma estratégia para ele, que conte com a pizza, o churrasco e a vida social.'],
  tempo: ['Falta de tempo', 'A alimentação tem que se adaptar à sua rotina, e não o contrário. Existem estratégias simples para quem não tem tempo nem para pensar no que vai comer.'],
  naosei: ['Não saber o que nem quanto comer', 'Sem saber quantidade e distribuição, a dieta vira chute. E chute às vezes acerta, mas quase nunca se mantém.'],
  info: ['Informação demais, direção de menos', 'Informação genérica não substitui uma avaliação do seu caso. O que serve para o influenciador pode não servir para você.'],
  ansiedade: ['Beliscar o dia todo', 'Beliscar costuma vir de refeições mal montadas, horários bagunçados ou ansiedade. Entender o gatilho é mais eficiente do que só "ter força de vontade".'],
  alcool: ['Bebida e vida social', 'Ninguém precisa virar ermitão. Mas álcool tem bastante caloria, não sacia e atrapalha o sono e a recuperação. Dá para encaixar com estratégia, sabendo o custo.'],
  massa_semtreino: ['Massa muscular começa no treino', 'Para ganhar massa, a alimentação precisa andar junto com um treino de força. Sem esse estímulo, a comida a mais tende a virar gordura, não músculo.'],
  emagrecer_semtreino: ['Emagrecer sem perder músculo', 'Cortar comida sem treinar pode baixar o peso, mas parte do que vai embora é músculo. Alimentação certa somada a algum treino de força muda o desenho do corpo.'],
  avancado: ['Quem treina há anos precisa de ajuste fino', 'Para quem já treina pesado, o que trava o resultado é o detalhe: distribuição de proteína, carboidrato em volta do treino, recuperação e periodização da dieta.'],
  iniciante: ['Começo de treino é janela de ouro', 'Quem está começando costuma responder rápido quando treino e alimentação andam juntos. É a hora de construir o hábito certo desde o início.'],
  turnos: ['Rotina em turnos', 'Plantão e turno bagunçam fome, sono e horário. O plano precisa ser montado em cima da sua escala, e não de um horário "padrão" que você não tem.'],
  rua: ['Comer na rua', 'Comer fora não é o problema. O problema é não saber escolher. Dá para montar um plano que funciona no restaurante, na padaria e no lanche rápido.'],
  evita: ['A relação com o espelho', 'Quando a pessoa evita foto e espelho, o objetivo não é só estético. É voltar a se sentir bem consigo. Por isso o processo precisa ser possível, e não um castigo.'],
};

/* =========================================================
   LÓGICA (não precisa mexer daqui pra baixo)
   ========================================================= */
(function () {
  const $ = (s) => document.querySelector(s);
  const $$ = (s) => document.querySelectorAll(s);
  const wa = (msg) => `https://wa.me/${CONFIG.whatsapp}?text=${encodeURIComponent(msg)}`;

  /* ---------- links de WhatsApp fixos ---------- */
  const MSGS = {
    paciente: 'Oi Fred! Já sou paciente e queria falar com você.',
    presencial: 'Oi Fred! Vi sua página e quero saber sobre o atendimento PRESENCIAL (Cordeiro/Nova Friburgo).',
    online: 'Oi Fred! Vi sua página e quero saber sobre o atendimento ONLINE.',
    semestral: 'Oi Fred! Vi sua página e quero saber mais sobre o plano SEMESTRAL.',
    trimestral: 'Oi Fred! Vi sua página e quero saber mais sobre o plano TRIMESTRAL.',
    avulsa: 'Oi Fred! Vi sua página e quero saber mais sobre a CONSULTA AVULSA.',
  };
  const ligarWhats = () => $$('.js-whats').forEach((a) => {
    a.href = wa(MSGS[a.dataset.msg] || MSGS.presencial);
    a.target = '_blank'; a.rel = 'noopener';
  });
  $$('.js-crn').forEach((el) => (el.textContent = CONFIG.crn));

  /* ---------- planos ---------- */
  function renderPlanos() {
    $('#planos-lista').innerHTML = Object.entries(PLANOS).map(([id, p]) => `
      <article class="plano ${p.destaque ? 'destaque' : ''}" id="plano-${id}">
        ${p.selo ? `<span class="plano-selo">${p.selo}</span>` : ''}
        <h3>${p.nome}</h3>
        <p class="plano-dur">${p.duracao}</p>
        ${CONFIG.mostrarPrecos
          ? `<p class="plano-preco">${p.preco} <small>${p.total}</small></p>`
          : `<p class="plano-sem-preco">Valor e condições direto com o Fred</p>`}
        <p class="plano-pra">${p.pra}</p>
        <ul>${p.itens.map((i) => `<li>${i}</li>`).join('')}</ul>
        <a href="#" class="btn js-whats" data-msg="${id}">${p.cta}</a>
      </article>`).join('');
    $('#planos-nota').textContent = CONFIG.mostrarPrecos
      ? 'Pagamento no PIX, cartão de crédito, cartão de débito ou dinheiro. Condições de parcelamento confirmadas no fechamento.'
      : 'Os valores e as condições de pagamento o Fred te passa na conversa pelo WhatsApp. Aceita PIX, cartão de crédito, débito e dinheiro.';
    if (CONFIG.mostrarPrecos) {
      $('#conta-destaque').textContent = 'E é o plano em que cada consulta sai mais em conta: R$165 por consulta, menos de R$5,50 por dia.';
      $('#carimbo-recibo').textContent = '6x R$165';
    }
    ligarWhats();
  }

  /* ---------- recursos (contador fixo) ---------- */
  function iniciarRecursos() {
    const itens = [...$$('.recurso')];
    if (!('IntersectionObserver' in window)) return;
    const io = new IntersectionObserver((ents) => ents.forEach((e) => {
      if (!e.isIntersecting) return;
      const i = itens.indexOf(e.target);
      itens.forEach((x) => x.classList.toggle('ativo', x === e.target));
      $('#vc-n').textContent = i + 1;
      $('#vc-num').textContent = String(i + 1).padStart(2, '0');
      $('#vc-tit').textContent = e.target.dataset.tit;
    }), { rootMargin: '-45% 0px -45% 0px' });
    itens.forEach((x) => io.observe(x));
  }

  /* ---------- animação de entrada ---------- */
  function iniciarRevela() {
    if (!('IntersectionObserver' in window) || matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    const alvos = $$('.aspas, .flutua, .passo, .modo, .plano, .recurso, .no, .print');
    alvos.forEach((el) => el.classList.add('revela'));
    const io = new IntersectionObserver((ents) => ents.forEach((e) => {
      if (e.isIntersecting) { e.target.classList.add('dentro'); io.unobserve(e.target); }
    }), { threshold: 0.12 });
    alvos.forEach((el) => io.observe(el));
  }

  /* ---------- diagnóstico ---------- */
  const telas = ['#q-inicio', '#q-perguntas', '#q-dados', '#q-resultado'];
  const respostas = {};
  let atual = 0;
  let dados = { nome: '', whatsapp: '' };
  const letras = 'ABCDEFGHIJ';

  const mostrar = (id) => {
    telas.forEach((t) => ($(t).hidden = t !== id));
    const topo = $('#quiz').getBoundingClientRect().top;
    if (topo < 0 || topo > innerHeight * 0.5) $('#quiz').scrollIntoView({ behavior: 'smooth', block: 'start' });
  };

  function renderPergunta() {
    const q = PERGUNTAS[atual];
    const sel = respostas[q.id] || (q.multi ? [] : null);
    const pct = Math.round((atual / (PERGUNTAS.length + 1)) * 100);
    $('#q-feito').style.width = pct + '%';
    $('#q-marcador').style.left = pct + '%';

    const box = $('#q-pergunta');
    box.innerHTML = `
      <p class="q-contador">${atual + 1} DE ${PERGUNTAS.length}</p>
      <h3 class="q-titulo">${q.titulo}</h3>
      ${q.apoio ? `<p class="q-apoio">${q.apoio}</p>` : ''}
      <ul class="q-opcoes">
        ${q.opcoes.map(([v, txt], k) => {
          const on = q.multi ? sel.includes(v) : sel === v;
          return `<li><button type="button" class="q-opcao" data-v="${v}" aria-pressed="${on}"><span class="q-letra">${letras[k]}</span><span>${txt}</span></button></li>`;
        }).join('')}
      </ul>
      <div class="q-acoes">
        <button type="button" class="link-voltar" id="q-voltar">Voltar</button>
        ${q.multi ? `<button type="button" class="btn" id="q-continuar" ${sel.length ? '' : 'disabled'}>Continuar →</button>` : ''}
      </div>`;

    box.querySelectorAll('.q-opcao').forEach((b) => b.addEventListener('click', () => {
      const v = b.dataset.v;
      if (q.multi) {
        const arr = respostas[q.id] || [];
        respostas[q.id] = arr.includes(v) ? arr.filter((x) => x !== v) : [...arr, v];
        b.setAttribute('aria-pressed', respostas[q.id].includes(v));
        $('#q-continuar').disabled = !respostas[q.id].length;
      } else {
        respostas[q.id] = v;
        box.querySelectorAll('.q-opcao').forEach((o) => o.setAttribute('aria-pressed', o === b));
        setTimeout(avancar, 220);
      }
    }));
    $('#q-voltar').addEventListener('click', voltar);
    if (q.multi) $('#q-continuar').addEventListener('click', avancar);
  }

  function avancar() {
    if (atual < PERGUNTAS.length - 1) { atual++; renderPergunta(); }
    else { mostrar('#q-dados'); setTimeout(() => $('#q-dados input').focus({ preventScroll: true }), 300); }
  }
  function voltar() {
    if (atual > 0) { atual--; renderPergunta(); } else mostrar('#q-inicio');
  }

  const textoDe = (id, v) => {
    const q = PERGUNTAS.find((x) => x.id === id);
    const pega = (val) => (q.opcoes.find(([k]) => k === val) || [, val])[1];
    return Array.isArray(v) ? v.map(pega).join(', ') : pega(v);
  };

  // Qual plano indicar
  function indicarPlano(r) {
    const precisaTempo = ['larga', 'tentou', 'semresultado'].includes(r.historico);
    const objetivoLongo = ['emagrecer', 'massa', 'definicao'].includes(r.objetivo);
    let plano, porque = [];

    if (r.acompanhamento === 'continuo') {
      plano = 'semestral';
      porque.push('Você quer alguém do seu lado até o resultado aparecer, e é exatamente para isso que o semestral existe.');
    } else if (r.acompanhamento === 'meses') {
      plano = precisaTempo ? 'semestral' : 'trimestral';
      porque.push(plano === 'trimestral'
        ? 'Três meses dão tempo de organizar a alimentação, ajustar o plano duas vezes e pegar o ritmo.'
        : 'Você pediu alguns meses, mas pelo seu histórico, três meses costumam ser pouco para o hábito firmar.');
    } else if (r.acompanhamento === 'pontual') {
      plano = 'avulsa';
      porque.push('Você quer uma orientação pontual: a consulta avulsa entrega a avaliação completa e a dieta montada com você.');
    } else {
      plano = (precisaTempo || objetivoLongo) ? 'semestral' : 'trimestral';
      porque.push('Pelo seu objetivo e pelo seu histórico, faz sentido um acompanhamento com retornos e ajustes ao longo do caminho.');
    }

    if (plano === 'semestral') {
      if (precisaTempo) porque.push('O que te trava hoje é manter, e não começar. Seis retornos e WhatsApp direto deixam bem mais difícil largar no meio.');
      if (objetivoLongo) porque.push(`${textoDe('objetivo', r.objetivo)} é resultado de meses, e não de semanas. Seis meses dão tempo de ajustar o plano a cada fase.`);
      porque.push('É o plano em que cada consulta sai mais em conta.');
    }
    if (plano === 'trimestral') porque.push('Se depois de três meses você quiser seguir, dá para continuar o acompanhamento.');
    if (plano === 'avulsa' && precisaTempo) porque.push('Atenção: pelo seu histórico, um plano com retornos (trimestral ou semestral) costuma funcionar melhor. Vale conversar com o Fred sobre isso.');

    return { plano, porque: porque.slice(0, 3) };
  }

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
    if (r.espelho === 'evita') add('evita');
    (r.trava || []).slice(2).forEach(add);
    return lista.slice(0, 3);
  }

  function renderResultado() {
    const r = respostas;
    const perfil = PERFIS[r.historico] || PERFIS.semresultado;
    const primeiro = dados.nome.trim().split(/\s+/)[0];
    const { plano, porque } = indicarPlano(r);
    const P = PLANOS[plano];

    $('#r-titulo').textContent = perfil.titulo;
    $('#r-resumo').textContent = `${primeiro}, ${perfil.resumo}`;
    $('#r-plano-nome').textContent = P.nome;
    $('#r-plano-preco').textContent = CONFIG.mostrarPrecos ? `${P.duracao} · ${P.preco}` : `${P.duracao} · valor direto com o Fred`;
    $('#r-porque').innerHTML = porque.map((t) => `<li>${t}</li>`).join('');
    $('#r-pontos').innerHTML = montarPontos(r).map((k) => `<li><b>${PONTOS[k][0]}</b><span>${PONTOS[k][1]}</span></li>`).join('');

    const mod = {
      cordeiro: 'No presencial em Cordeiro você ainda faz bioimpedância e ganha uma garrafa de água de cortesia na primeira consulta.',
      friburgo: 'No presencial em Nova Friburgo você ainda faz bioimpedância e ganha uma garrafa de água de cortesia na primeira consulta.',
      online: 'No online a consulta é por vídeo, ao vivo, com a dieta montada na hora, e a evolução é acompanhada por fotos e informações que você envia.',
      tantofaz: 'Você pode fazer presencial (Cordeiro ou Nova Friburgo, com bioimpedância) ou online, por vídeo, de qualquer lugar do Brasil.',
    };
    $('#r-modalidade').textContent = mod[r.modalidade] || mod.tantofaz;

    const msg =
`Oi Fred! Fiz o Diagnóstico do Shape.
Nome: ${dados.nome.trim()}
Resultado: ${perfil.titulo.replace('Perfil: ', '')}
Plano indicado: ${P.nome}
Objetivo: ${textoDe('objetivo', r.objetivo)}
Treino: ${textoDe('treino', r.treino)}
O que me atrapalha: ${textoDe('trava', r.trava || [])}
Atendimento: ${textoDe('modalidade', r.modalidade)}
Quero começar: ${textoDe('quando', r.quando)}

Quero entender como funciona o acompanhamento.`;
    $('#r-whats').href = wa(msg);

    $$('.plano').forEach((el) => el.classList.toggle('indicado', el.id === `plano-${plano}`));
    $$('.plano-selo.preto').forEach((el) => el.remove());
    const card = $(`#plano-${plano}`);
    if (card && !P.destaque) card.insertAdjacentHTML('afterbegin', '<span class="plano-selo preto">Indicado pra você</span>');
    if (card && P.destaque) card.querySelector('.plano-selo').textContent = 'Indicado pra você';
    $('#r-ver-planos').href = `#plano-${plano}`;

    mostrar('#q-resultado');
  }

  function enviarLead() {
    if (!CONFIG.webhook) return;
    const corpo = {
      data: new Date().toISOString(), nome: dados.nome, whatsapp: dados.whatsapp,
      ...Object.fromEntries(PERGUNTAS.map((q) => [q.id, textoDe(q.id, respostas[q.id] ?? '')])),
      plano_indicado: PLANOS[indicarPlano(respostas).plano].nome,
    };
    try { fetch(CONFIG.webhook, { method: 'POST', mode: 'no-cors', headers: { 'Content-Type': 'text/plain' }, body: JSON.stringify(corpo) }); } catch (e) {}
  }

  $('#q-comecar').addEventListener('click', () => { atual = 0; renderPergunta(); mostrar('#q-perguntas'); });
  $('#q-voltar-dados').addEventListener('click', () => { atual = PERGUNTAS.length - 1; renderPergunta(); mostrar('#q-perguntas'); });
  $('#q-refazer').addEventListener('click', () => {
    Object.keys(respostas).forEach((k) => delete respostas[k]);
    $$('.plano').forEach((el) => el.classList.remove('indicado'));
    renderPlanos();
    mostrar('#q-inicio');
  });

  $('#q-dados').addEventListener('submit', (e) => {
    e.preventDefault();
    const f = e.target;
    const nome = f.nome.value.trim();
    const fone = f.whatsapp.value.replace(/\D/g, '');
    const erro = $('#q-erro');
    if (nome.length < 2) { erro.textContent = 'Digite o seu nome.'; erro.hidden = false; f.nome.focus(); return; }
    if (fone.length < 10 || fone.length > 13) { erro.textContent = 'Digite um WhatsApp válido, com DDD.'; erro.hidden = false; f.whatsapp.focus(); return; }
    erro.hidden = true;
    dados = { nome, whatsapp: fone };
    enviarLead();
    renderResultado();
  });

  $('#q-dados [name=whatsapp]').addEventListener('input', (e) => {
    const d = e.target.value.replace(/\D/g, '').slice(0, 11);
    e.target.value = d.length > 6 ? `(${d.slice(0, 2)}) ${d.slice(2, d.length - 4)}-${d.slice(-4)}` : d.length > 2 ? `(${d.slice(0, 2)}) ${d.slice(2)}` : d;
  });

  renderPlanos();
  iniciarRecursos();
  iniciarRevela();
})();
