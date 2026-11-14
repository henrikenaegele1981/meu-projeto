// Na nuvem, o vídeo/foto vai direto do navegador para o Supabase (a Vercel não aceita arquivos grandes).
document.querySelectorAll('form[data-nuvem]').forEach((form) => {
  form.addEventListener('submit', async (ev) => {
    const campo = form.querySelector('input[type=file][name=arquivo]');
    const botao = form.querySelector('button');
    if (!campo || !campo.files.length || form.dataset.pronto) {
      if (botao) { botao.disabled = true; botao.textContent = 'Salvando…'; }
      return;
    }
    ev.preventDefault();
    const arquivo = campo.files[0];
    const limite = Number(form.dataset.limiteMb || 50);
    if (arquivo.size > limite * 1024 * 1024) {
      alert(`O arquivo tem ${(arquivo.size / 1048576).toFixed(0)} MB. O limite é ${limite} MB: exporte o vídeo com um pouco menos de qualidade e tente de novo.`);
      return;
    }
    botao.disabled = true;
    const texto = botao.textContent;
    try {
      botao.textContent = 'Preparando o envio…';
      const corpo = new FormData();
      corpo.append('nome', arquivo.name);
      const resp = await fetch(form.dataset.linkEnvio, { method: 'POST', body: corpo });
      const info = await resp.json();
      if (!resp.ok) throw new Error(info.erro || 'Não consegui preparar o envio.');
      await new Promise((ok, falha) => {
        const xhr = new XMLHttpRequest();
        xhr.open('PUT', info.url);
        xhr.setRequestHeader('Content-Type', arquivo.type || 'application/octet-stream');
        xhr.setRequestHeader('x-upsert', 'true');
        xhr.upload.onprogress = (e) => {
          if (e.lengthComputable) botao.textContent = `Enviando o arquivo… ${Math.round(100 * e.loaded / e.total)}%`;
        };
        xhr.onload = () => (xhr.status < 300 ? ok() : falha(new Error(`O Supabase recusou o arquivo (HTTP ${xhr.status}): ${xhr.responseText.slice(0, 200)}`)));
        xhr.onerror = () => falha(new Error('A conexão caiu durante o envio. Tente de novo.'));
        xhr.send(arquivo);
      });
      const extra = (n, v) => { const i = document.createElement('input'); i.type = 'hidden'; i.name = n; i.value = v; form.appendChild(i); };
      extra('enviado', info.nome);
      extra('nome_original', arquivo.name);
      campo.removeAttribute('name');
      campo.required = false;
      form.dataset.pronto = '1';
      botao.textContent = 'Agendando…';
      form.submit();
    } catch (erro) {
      alert(erro.message);
      botao.disabled = false;
      botao.textContent = texto;
    }
  });
});
