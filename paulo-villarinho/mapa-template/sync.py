import json,re,sys
W=[w for w in json.load(open(sys.argv[1]))['words'] if w['type']=='word']
norm=lambda s:re.sub(r'[^\w$%]','',s.lower())
toks=[norm(w['text']) for w in W]; pos=0
def t(phrase):
    global pos
    p=[norm(x) for x in phrase.split()]
    for i in range(pos,len(toks)):
        if toks[i:i+len(p)]==p: pos=i+1; return W[i]['start']
    raise SystemExit('não achei: '+phrase)
A={}
for k in ['Em abril','custava','Era o menor','uma queda','Aí veio','O mercado','O dólar subiu','Motivo número dois','O pacote','e o Banco','E o pano','Tarifa','Menos venda','Resultado','17','Não foi','E ele chega','Viagem','O mesmo','Ninguém','Quer entender']:
    A[k]=round(t(k),2)
END=round(W[-1]['end']+0.9,2)
e=lambda k,d=0.05:round(A[k]-d,2)
WARP=[[0,0],[3.0,3.5],[A['Aí veio'],11],[A['Motivo número dois'],19.8],[A['E o pano'],26.8],[A['Resultado'],35.6],[A['Não foi'],41.6],[A['Viagem'],44.6],[A['Ninguém'],50.4],[END,53]]
LBL=[[3.0,e('Aí veio'),'SÃO PAULO · ABRIL/2026'],[A['Aí veio']+.15,e('E o pano'),'BRASÍLIA · OUT–NOV/2026'],[A['E o pano']+.45,e('Resultado',.15),'WASHINGTON · DESDE AGO/2025'],[A['17']+.6,e('Não foi'),'SÃO PAULO · 17/11/2026']]
NUM=[[A['custava'],e('Aí veio'),'fechamento de abril/2026','R$ 4,97','menor valor do ano · Forbes/B3'],
 [A['O dólar subiu'],e('Motivo número dois'),'em um único pregão','+8%','dólar em 26/10 · Nomad, Remessa Online'],
 [A['e o Banco'],e('E o pano'),'leilões do Banco Central','US$ 1 bi','linha de dólar · nov/2026 · IstoÉ Dinheiro'],
 [A['Tarifa'],e('Resultado',.15),'tarifa dos EUA','50%','sobre produtos brasileiros · desde 06/08/2025'],
 [A['17']+.6,e('Não foi'),'máxima do dia 17/11','R$ 5,81','maior nível desde abril/2025 · B3']]
C=[('Em abril','Era o menor','Em abril de 2026, um dólar custava <b>R$&nbsp;4,97</b>.'),('Era o menor','uma queda','Era o menor valor do ano.'),('uma queda','Aí veio','Uma queda de mais de <b>9%</b> no ano.'),
 ('Aí veio','O mercado','Aí veio o <b>motivo 1</b>: a eleição.'),('O mercado','O dólar subiu','O mercado apostou num resultado. Veio o outro.'),('O dólar subiu','Motivo número dois','Mais de <b>8%</b> num dia só.'),
 ('Motivo número dois','O pacote','<b>Motivo 2</b>: as contas do governo.'),('O pacote','e o Banco','Pacote fiscal travado no Senado.'),('e o Banco','E o pano','O BC já foi a campo: <b>US$&nbsp;1&nbsp;bi</b> em leilões.'),
 ('E o pano','Tarifa','E o pano de fundo fica em <b>Washington</b>.'),('Tarifa','Menos venda','Tarifa de <b>50%</b> sobre produtos brasileiros.'),('Menos venda','Resultado','Menos venda, menos dólar entrando.'),
 ('Resultado','17','Resultado?'),('17','Não foi','17 de novembro: <b>R$&nbsp;5,81</b>.'),
 ('Viagem','O mesmo','Viagem de fim de ano?'),('O mesmo','Ninguém','O mesmo dólar custa <b>quase 17% a mais</b> que em abril.'),('Ninguém','Quer entender','Ninguém sabe a cotação de amanhã. Dá para entender o que move ela.'),('Quer entender',None,'Quer entender mais? O link está na bio.')]
CAP=[[A[a],(e(b) if b else END),txt] for a,b,txt in C]
FULL=[A['Não foi'],e('Viagem'),'Não foi um motivo só.','E ele chega no seu bolso.',A['E ele chega']]
CTA=[A['Quer entender'],END]
r=lambda x:json.dumps(x,ensure_ascii=False)
js=f"""// tempos em segundos do ÁUDIO final (gerado por sync.py)
const WARP={r(WARP)};
function warp(t){{for(let i=0;i<WARP.length-1;i++){{const [a0,d0]=WARP[i],[a1,d1]=WARP[i+1];if(t<=a1)return d0+(d1-d0)*clamp((t-a0)/(a1-a0));}}return 53;}}
const LBL={r(LBL)};
const NUM={r(NUM)};
const CAP={r(CAP)};
const FULL={r(FULL)};
const CTA={r(CTA)};

"""
p=sys.argv[2];s=open(p).read()
a=s.index('// tempos em segundos');b=s.index('const $=id=>')
s=s[:a]+js+s[b:]
s=re.sub(r"const KEEP=.*?\n","",s);s=re.sub(r"function toOld\(t\)\{.*?\n","",s)
s=s.replace("const t=toOld(nt);","const t=nt;")
s=re.sub(r"window\.DUR=[\d.]+;",f"window.DUR={END};",s)
open(p,'w').write(s);print('DUR',END,A)
