/* =========================================================
   CONFIGURAÇÃO: edite só este bloco
   ========================================================= */
const CONFIG = {
  // WhatsApp do Fred (quem conduz a conversa de vendas), só números,
  // com código do país e DDD. Ex.: 5522999999999
  whatsapp: '5522000000000',

  // Usuário do Instagram, sem @
  instagram: 'usuario_do_fred',

  // Número do registro no CRN
  crn: '00000',

  // Mensagens que já chegam escritas no WhatsApp, de acordo com o botão clicado.
  // Ajudam o Fred a saber de onde o contato veio e qual modalidade interessa.
  mensagens: {
    geral: 'Oi Fred! Vi sua página e quero saber como funciona o acompanhamento.',
    planos: 'Oi Fred! Vi sua página e quero conhecer os planos de acompanhamento.',
    presencial: 'Oi Fred! Vi sua página e quero saber sobre o atendimento PRESENCIAL (Cordeiro/Nova Friburgo).',
    online: 'Oi Fred! Vi sua página e quero saber sobre o atendimento ONLINE.',
  },
};

/* ========================================================= */

(function () {
  const waLink = (key) =>
    `https://wa.me/${CONFIG.whatsapp}?text=${encodeURIComponent(CONFIG.mensagens[key] || CONFIG.mensagens.geral)}`;

  document.querySelectorAll('.js-whats').forEach((el) => {
    el.href = waLink(el.dataset.msg);
    el.target = '_blank';
    el.rel = 'noopener';
  });

  document.querySelectorAll('.js-insta').forEach((el) => {
    el.href = `https://ig.me/m/${CONFIG.instagram}`;
  });

  document.querySelectorAll('.js-crn').forEach((el) => {
    el.textContent = CONFIG.crn;
  });

  // Animação de entrada suave nas seções
  if ('IntersectionObserver' in window && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
    const items = document.querySelectorAll('.step, .goal, .mode, .pain, .faq, .checklist li');
    items.forEach((el) => el.classList.add('reveal'));
    const io = new IntersectionObserver(
      (entries) => entries.forEach((e) => {
        if (e.isIntersecting) { e.target.classList.add('reveal--in'); io.unobserve(e.target); }
      }),
      { threshold: 0.12 }
    );
    items.forEach((el) => io.observe(el));
  }
})();
