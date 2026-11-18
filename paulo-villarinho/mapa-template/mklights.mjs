import * as d3 from 'd3'; import * as topo from 'topojson-client'; import fs from 'fs';
const land=topo.feature(JSON.parse(fs.readFileSync('node_modules/world-atlas/land-110m.json')),'land');
let seed=7;const rnd=()=>(seed=(seed*16807)%2147483647)/2147483647;const L=[];
while(L.length<2600){const p=[rnd()*360-180,Math.asin(rnd()*2-1)*180/Math.PI];if(Math.abs(p[1])>62)continue;if(d3.geoContains(land,p))L.push([+p[0].toFixed(2),+p[1].toFixed(2),+rnd().toFixed(2)]);}
fs.writeFileSync('lights.js','window.LIGHTS='+JSON.stringify(L)+';');
