/* =========================================================
   CONFIGURAÇÃO COMPARTILHADA (página principal e diagnóstico)
   Edite só este arquivo para trocar WhatsApp, CRN, planos e resultados.
   ========================================================= */
const CONFIG = {
  // WhatsApp do Fred (quem conduz a conversa), só números, com 55 + DDD
  whatsapp: '5522981173962',

  // Número do registro no CRN
  crn: '00000',

  // Mostrar preços na página e no diagnóstico? O briefing pede valores só na conversa privada,
  // por isso começa desligado. Para mostrar, troque para true.
  mostrarPrecos: false,

  // OPCIONAL: endereço que recebe os contatos do diagnóstico (Google Planilhas via Apps Script, Make, Zapier...)
  webhook: '',
};

const PLANOS = {
  semestral: {
    nome: 'Semestral',
    rotulo: 'O preferido',
    duracao: '6 meses',
    consultas: '6 consultas',
    preco: '6x R$165',
    destaque: true,
    desc: 'Tempo de sobra pra virar hábito, com alguém do seu lado do começo ao fim.',
    itens: ['6 consultas (inicial + 5 retornos)', 'Ajustes também entre as consultas', 'WhatsApp direto por 6 meses', 'Melhor valor por consulta'],
  },
  trimestral: {
    nome: 'Trimestral',
    rotulo: 'Formato',
    duracao: '3 meses',
    consultas: '3 consultas',
    preco: '3x R$194',
    desc: 'Pra quem quer um empurrão de alguns meses pra organizar a casa e pegar o ritmo.',
    itens: ['3 consultas (inicial + 2 retornos)', 'Ajustes também entre as consultas', 'WhatsApp direto por 3 meses'],
  },
  avulsa: {
    nome: 'Avulsa',
    rotulo: 'Formato',
    duracao: '1 consulta',
    consultas: 'consulta completa',
    preco: 'R$250',
    desc: 'Pra quem quer uma orientação pontual e prefere decidir os próximos passos com calma.',
    itens: ['Consulta de 45 a 90 min', 'Dieta montada durante a consulta', 'Retornos avulsos, se quiser'],
  },
};

/* RESULTADOS DE PACIENTES (só com autorização por escrito e normas do CRN conferidas)
   Coloque a imagem em assets/resultados/ e acrescente uma linha:
   { foto: 'assets/resultados/arquivo.jpg', nome: 'J. S.', texto: 'Frase curta' },
   Enquanto a lista estiver vazia, a seção fica escondida. */
const RESULTADOS = [
];

const waLink = (msg) => `https://wa.me/${CONFIG.whatsapp}?text=${encodeURIComponent(msg)}`;
