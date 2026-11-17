/* Página principal. Os dados (WhatsApp, CRN, planos, resultados) ficam em config.js. */

// Texto das abas "Qual plano é pro seu objetivo"
const OBJETIVOS = {
  emagrecer: {
    frase: 'Perder gordura sem perder músculo, sem passar fome e sem abrir mão de tudo o que você gosta.',
    plano: 'semestral',
    obs: 'Emagrecer de verdade leva alguns meses. Com seis retornos, dá tempo de ajustar o plano a cada fase e atravessar os fins de semana sem largar tudo.',
  },
  massa: {
    frase: 'Comer de acordo com o seu treino pra construir músculo, e não só ganhar peso.',
    plano: 'semestral',
    obs: 'Músculo gosta de constância. O plano vai mudando conforme o seu treino evolui.',
  },
  definicao: {
    frase: 'Lapidar o shape e render mais no treino com um ajuste fino na alimentação.',
    plano: 'trimestral',
    obs: 'Pra quem já treina e quer uma fase mais focada. Se quiser seguir depois, é só continuar.',
  },
  saude: {
    frase: 'Voltar a gostar do espelho, vestir aquela roupa com confiança e comer melhor sem neura.',
    plano: 'semestral',
    obs: 'Autoestima se constrói com hábito. E hábito pede tempo e alguém do seu lado.',
  },
};

const MSGS = {
  geral: 'Oi Fred! Vi sua página e queria entender como funciona o acompanhamento.',
  semestral: 'Oi Fred! Vi sua página e quero saber mais sobre o plano SEMESTRAL.',
  trimestral: 'Oi Fred! Vi sua página e quero saber mais sobre o plano TRIMESTRAL.',
  avulsa: 'Oi Fred! Vi sua página e quero saber mais sobre a CONSULTA AVULSA.',
};

(function () {
  const $ = (s) => document.querySelector(s);
  const $$ = (s) => document.querySelectorAll(s);
  const rotObj = { emagrecer: 'Emagrecer', massa: 'Ganhar massa', definicao: 'Definição', saude: 'Saúde e autoestima' };
  const ctaObj = { emagrecer: 'Quero emagrecer', massa: 'Quero ganhar massa', definicao: 'Quero mais definição', saude: 'Quero me sentir melhor' };

  /* formatos (planos) */
  function renderFormatos(objetivo) {
    $('#formatos').innerHTML = Object.entries(PLANOS).map(([id, p]) => {
      const indicado = OBJETIVOS[objetivo].plano === id;
      return `
      <article class="formato ${p.destaque ? 'destaque' : ''}">
        <div>
          <span class="f-rot">${p.rotulo} · ${p.duracao}${indicado ? ` <span class="f-pill">Indicado para ${rotObj[objetivo]}</span>` : ''}</span>
          <b class="f-nome">${p.nome}</b>
          ${CONFIG.mostrarPrecos ? `<span class="f-preco">${p.preco}</span>` : ''}
          <p class="f-desc">${p.desc}</p>
        </div>
        <ul class="f-itens">${p.itens.map((i) => `<li>${i}</li>`).join('')}</ul>
        <a href="#" class="f-btn js-whats" data-msg="${id}">Começar <span>→</span></a>
      </article>`;
    }).join('');
    ligarWhats();
  }

  /* abas */
  function mostrarObjetivo(obj) {
    const o = OBJETIVOS[obj];
    const p = PLANOS[o.plano];
    $$('.aba').forEach((a) => a.setAttribute('aria-selected', a.dataset.aba === obj));
    $('#ap-frase').textContent = o.frase;
    $('#ap-indica').textContent = `${p.nome} (${p.duracao}, ${p.consultas})`;
    $('#ap-obs').textContent = o.obs;
    $('#ap-tempo').textContent = CONFIG.mostrarPrecos ? p.preco : p.duracao;
    $('#ap-sub').textContent = CONFIG.mostrarPrecos ? `${p.nome} · ${p.duracao}` : `de acompanhamento · ${p.consultas}`;
    $('#ap-cta').href = `diagnostico/?objetivo=${obj}`;
    $('#ap-cta').innerHTML = `${ctaObj[obj]}: fazer o diagnóstico <i>→</i>`;
    renderFormatos(obj);
  }
  $$('.aba').forEach((a) => a.addEventListener('click', () => mostrarObjetivo(a.dataset.aba)));

  /* WhatsApp e CRN */
  function ligarWhats() {
    $$('.js-whats').forEach((a) => {
      a.href = waLink(MSGS[a.dataset.msg] || MSGS.geral);
      a.target = '_blank'; a.rel = 'noopener';
    });
  }
  $$('.js-crn').forEach((el) => (el.textContent = CONFIG.crn));

  /* resultados de pacientes */
  if (RESULTADOS.length) {
    $('#resultados-grade').innerHTML = RESULTADOS.map((r) => `
      <figure class="resultado-card">
        <img src="${r.foto}" alt="Evolução de ${r.nome}, paciente do Fred" loading="lazy">
        <figcaption><b>${r.nome}</b>${r.texto ? `<span>${r.texto}</span>` : ''}</figcaption>
      </figure>`).join('');
    $('#resultados').hidden = false;
  }

  /* entrada suave das seções */
  if ('IntersectionObserver' in window && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
    const alvos = $$('.quem-texto, .quem-visual, .verdade, .aba-painel, .formato, .linha li, .faq details, .final-grid > *');
    alvos.forEach((el) => el.classList.add('revela'));
    const io = new IntersectionObserver((ents) => ents.forEach((e) => {
      if (e.isIntersecting) { e.target.classList.add('dentro'); io.unobserve(e.target); }
    }), { threshold: 0.1 });
    alvos.forEach((el) => io.observe(el));
  }

  mostrarObjetivo('emagrecer');
})();
