# K6


### Notas para a atividade:
 - Ja Implementei diretamente no projeto, logo o relatorio esta extenso pois ele testa todos os endpoints do nosso projeto. 

## Instalação e Uso

### Passo a Passo
1. Instalar o k6:

`npm install -g k6`

2. Criar um novo projeto k6:

`k6 new load_test`

3. Uso:

**Imports**
```javascript
import http from 'k6/http';
import { sleep, group } from 'k6';
```
**Definição de carga**

```javascript
export const options = {
    vus: 10, // 10 virtual users
    duration: '5m', // Test duration of 5 minutes
};
```
**Def Teste de Carga**
```javascript
export default function () {
    group('Load Test', () => {
        http.get('http://localhost:3000');
    });

    sleep(1); // Add a small delay between requests
}
```

JavaScript
4. Executar o teste de carga:

``k6 run load_test.js``


5. Gerar um relatório:

k6 report > ``load_test_report.html``

## Tecnologia e Conceitos Aprendidos
**k6:** é uma ferramenta de teste de carga e estresse de código aberto que permite simular cargas de usuários em um sistema para avaliar seu desempenho. O k6 usa JavaScript como linguagem de script, o que o torna fácil de aprender e usar.

**Teste de Carga:** mede o desempenho de um sistema sob uma carga normal ou esperada. O objetivo do teste de carga é garantir que o sistema possa lidar com o número esperado de usuários e solicitações.

**Teste de Estresse:** mede o desempenho de um sistema sob uma carga pesada ou inesperada. O objetivo do teste de estresse é identificar os limites do sistema e garantir que ele possa lidar com picos de tráfego ou outras condições adversas.

## Relatório

```txt

          /\      |‾‾| /‾‾/   /‾‾/   
     /\  /  \     |  |/  /   /  /    
    /  \/    \    |     (   /   ‾‾\  
   /          \   |  |\  \ |  (‾)  | 
  / __________ \  |__| \__\ \_____/ .io

     execution: local
        script: load_test.js
        output: -

     scenarios: (100.00%) 1 scenario, 10 max VUs, 1m30s max duration (incl. graceful stop):
              * default: 10 looping VUs for 1m0s (gracefulStop: 30s)


running (0m01.0s), 10/10 VUs, 0 complete and 0 interrupted iterations
default   [   2% ] 10 VUs  0m01.0s/1m0s

running (0m02.0s), 10/10 VUs, 10 complete and 0 interrupted iterations
default   [   3% ] 10 VUs  0m02.0s/1m0s

running (0m03.0s), 10/10 VUs, 20 complete and 0 interrupted iterations
default   [   5% ] 10 VUs  0m03.0s/1m0s

running (0m04.0s), 10/10 VUs, 30 complete and 0 interrupted iterations
default   [   7% ] 10 VUs  0m04.0s/1m0s

running (0m05.0s), 10/10 VUs, 40 complete and 0 interrupted iterations
default   [   8% ] 10 VUs  0m05.0s/1m0s

running (0m06.0s), 10/10 VUs, 50 complete and 0 interrupted iterations
default   [  10% ] 10 VUs  0m06.0s/1m0s

running (0m07.0s), 10/10 VUs, 60 complete and 0 interrupted iterations
default   [  12% ] 10 VUs  0m07.0s/1m0s

running (0m08.0s), 10/10 VUs, 70 complete and 0 interrupted iterations
default   [  13% ] 10 VUs  0m08.0s/1m0s

running (0m09.0s), 10/10 VUs, 80 complete and 0 interrupted iterations
default   [  15% ] 10 VUs  0m09.0s/1m0s

running (0m10.0s), 10/10 VUs, 90 complete and 0 interrupted iterations
default   [  17% ] 10 VUs  0m10.0s/1m0s

running (0m11.0s), 10/10 VUs, 100 complete and 0 interrupted iterations
default   [  18% ] 10 VUs  0m11.0s/1m0s

running (0m12.0s), 10/10 VUs, 110 complete and 0 interrupted iterations
default   [  20% ] 10 VUs  0m12.0s/1m0s

running (0m13.0s), 10/10 VUs, 120 complete and 0 interrupted iterations
default   [  22% ] 10 VUs  0m13.0s/1m0s

running (0m14.0s), 10/10 VUs, 130 complete and 0 interrupted iterations
default   [  23% ] 10 VUs  0m14.0s/1m0s

running (0m15.0s), 10/10 VUs, 140 complete and 0 interrupted iterations
default   [  25% ] 10 VUs  0m15.0s/1m0s

running (0m16.0s), 10/10 VUs, 150 complete and 0 interrupted iterations
default   [  27% ] 10 VUs  0m16.0s/1m0s

running (0m17.0s), 10/10 VUs, 160 complete and 0 interrupted iterations
default   [  28% ] 10 VUs  0m17.0s/1m0s

running (0m18.0s), 10/10 VUs, 170 complete and 0 interrupted iterations
default   [  30% ] 10 VUs  0m18.0s/1m0s

running (0m19.0s), 10/10 VUs, 180 complete and 0 interrupted iterations
default   [  32% ] 10 VUs  0m19.0s/1m0s

running (0m20.0s), 10/10 VUs, 190 complete and 0 interrupted iterations
default   [  33% ] 10 VUs  0m20.0s/1m0s

running (0m21.0s), 10/10 VUs, 200 complete and 0 interrupted iterations
default   [  35% ] 10 VUs  0m21.0s/1m0s

running (0m22.0s), 10/10 VUs, 210 complete and 0 interrupted iterations
default   [  37% ] 10 VUs  0m22.0s/1m0s

running (0m23.0s), 10/10 VUs, 210 complete and 0 interrupted iterations
default   [  38% ] 10 VUs  0m23.0s/1m0s

running (0m24.0s), 10/10 VUs, 220 complete and 0 interrupted iterations
default   [  40% ] 10 VUs  0m24.0s/1m0s

running (0m25.0s), 10/10 VUs, 230 complete and 0 interrupted iterations
default   [  42% ] 10 VUs  0m25.0s/1m0s

running (0m26.0s), 10/10 VUs, 240 complete and 0 interrupted iterations
default   [  43% ] 10 VUs  0m26.0s/1m0s

running (0m27.0s), 10/10 VUs, 250 complete and 0 interrupted iterations
default   [  45% ] 10 VUs  0m27.0s/1m0s

running (0m28.0s), 10/10 VUs, 260 complete and 0 interrupted iterations
default   [  47% ] 10 VUs  0m28.0s/1m0s

running (0m29.0s), 10/10 VUs, 270 complete and 0 interrupted iterations
default   [  48% ] 10 VUs  0m29.0s/1m0s

running (0m30.0s), 10/10 VUs, 280 complete and 0 interrupted iterations
default   [  50% ] 10 VUs  0m30.0s/1m0s

running (0m31.0s), 10/10 VUs, 290 complete and 0 interrupted iterations
default   [  52% ] 10 VUs  0m31.0s/1m0s

running (0m32.0s), 10/10 VUs, 300 complete and 0 interrupted iterations
default   [  53% ] 10 VUs  0m32.0s/1m0s

running (0m33.0s), 10/10 VUs, 310 complete and 0 interrupted iterations
default   [  55% ] 10 VUs  0m33.0s/1m0s

running (0m34.0s), 10/10 VUs, 320 complete and 0 interrupted iterations
default   [  57% ] 10 VUs  0m34.0s/1m0s

running (0m35.0s), 10/10 VUs, 330 complete and 0 interrupted iterations
default   [  58% ] 10 VUs  0m35.0s/1m0s

running (0m36.0s), 10/10 VUs, 340 complete and 0 interrupted iterations
default   [  60% ] 10 VUs  0m36.0s/1m0s

running (0m37.0s), 10/10 VUs, 350 complete and 0 interrupted iterations
default   [  62% ] 10 VUs  0m37.0s/1m0s

running (0m38.0s), 10/10 VUs, 360 complete and 0 interrupted iterations
default   [  63% ] 10 VUs  0m38.0s/1m0s

running (0m39.0s), 10/10 VUs, 370 complete and 0 interrupted iterations
default   [  65% ] 10 VUs  0m39.0s/1m0s

running (0m40.0s), 10/10 VUs, 380 complete and 0 interrupted iterations
default   [  67% ] 10 VUs  0m40.0s/1m0s

running (0m41.0s), 10/10 VUs, 390 complete and 0 interrupted iterations
default   [  68% ] 10 VUs  0m41.0s/1m0s

running (0m42.0s), 10/10 VUs, 400 complete and 0 interrupted iterations
default   [  70% ] 10 VUs  0m42.0s/1m0s

running (0m43.0s), 10/10 VUs, 410 complete and 0 interrupted iterations
default   [  72% ] 10 VUs  0m43.0s/1m0s

running (0m44.0s), 10/10 VUs, 420 complete and 0 interrupted iterations
default   [  73% ] 10 VUs  0m44.0s/1m0s

running (0m45.0s), 10/10 VUs, 430 complete and 0 interrupted iterations
default   [  75% ] 10 VUs  0m45.0s/1m0s

running (0m46.0s), 10/10 VUs, 440 complete and 0 interrupted iterations
default   [  77% ] 10 VUs  0m46.0s/1m0s

running (0m47.0s), 10/10 VUs, 440 complete and 0 interrupted iterations
default   [  78% ] 10 VUs  0m47.0s/1m0s

running (0m48.0s), 10/10 VUs, 450 complete and 0 interrupted iterations
default   [  80% ] 10 VUs  0m48.0s/1m0s

running (0m49.0s), 10/10 VUs, 460 complete and 0 interrupted iterations
default   [  82% ] 10 VUs  0m49.0s/1m0s

running (0m50.0s), 10/10 VUs, 470 complete and 0 interrupted iterations
default   [  83% ] 10 VUs  0m50.0s/1m0s

running (0m51.0s), 10/10 VUs, 480 complete and 0 interrupted iterations
default   [  85% ] 10 VUs  0m51.0s/1m0s

running (0m52.0s), 10/10 VUs, 490 complete and 0 interrupted iterations
default   [  87% ] 10 VUs  0m52.0s/1m0s

running (0m53.0s), 10/10 VUs, 500 complete and 0 interrupted iterations
default   [  88% ] 10 VUs  0m53.0s/1m0s

running (0m54.0s), 10/10 VUs, 510 complete and 0 interrupted iterations
default   [  90% ] 10 VUs  0m54.0s/1m0s

running (0m55.0s), 10/10 VUs, 520 complete and 0 interrupted iterations
default   [  92% ] 10 VUs  0m55.0s/1m0s

running (0m56.0s), 10/10 VUs, 530 complete and 0 interrupted iterations
default   [  93% ] 10 VUs  0m56.0s/1m0s

running (0m57.0s), 10/10 VUs, 540 complete and 0 interrupted iterations
default   [  95% ] 10 VUs  0m57.0s/1m0s

running (0m58.0s), 10/10 VUs, 550 complete and 0 interrupted iterations
default   [  97% ] 10 VUs  0m58.0s/1m0s

running (0m59.0s), 10/10 VUs, 560 complete and 0 interrupted iterations
default   [  98% ] 10 VUs  0m59.0s/1m0s

running (1m00.0s), 10/10 VUs, 570 complete and 0 interrupted iterations
default   [ 100% ] 10 VUs  1m00.0s/1m0s

     █ Upload Research

     █ Get Research Status

     █ Delete Research

     █ Update Research

     █ Vote Research

     █ Get All Researches

     █ Distribute Research

     data_received..................: 4.4 MB 72 kB/s
     data_sent......................: 816 kB 14 kB/s
     group_duration.................: avg=6.34ms  min=379.75µs med=6.07ms max=27.07ms p(90)=10.59ms p(95)=13.06ms
     http_req_blocked...............: avg=6.24µs  min=0s       med=1µs    max=1.79ms  p(90)=4µs     p(95)=6µs    
     http_req_connecting............: avg=1.32µs  min=0s       med=0s     max=606µs   p(90)=0s      p(95)=0s     
     http_req_duration..............: avg=6.1ms   min=323µs    med=5.8ms  max=26.89ms p(90)=10.47ms p(95)=12.96ms
       { expected_response:true }...: avg=4.97ms  min=610µs    med=4.7ms  max=20.08ms p(90)=8.9ms   p(95)=10.06ms
     http_req_failed................: 57.14% ✓ 2320      ✗ 1740
     http_req_receiving.............: avg=22.38µs min=5µs      med=17µs   max=1.64ms  p(90)=37µs    p(95)=52µs   
     http_req_sending...............: avg=13.51µs min=1µs      med=6µs    max=1.03ms  p(90)=19µs    p(95)=27µs   
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s     max=0s      p(90)=0s      p(95)=0s     
     http_req_waiting...............: avg=6.07ms  min=272µs    med=5.78ms max=26.83ms p(90)=10.43ms p(95)=12.9ms 
     http_reqs......................: 4060   66.963058/s
     iteration_duration.............: avg=1.04s   min=1.02s    med=1.04s  max=1.07s   p(90)=1.05s   p(95)=1.06s  
     iterations.....................: 580    9.566151/s
     vus............................: 10     min=10      max=10
     vus_max........................: 10     min=10      max=10


running (1m00.6s), 00/10 VUs, 580 complete and 0 interrupted iterations
default ✓ [ 100% ] 10 VUs  1m0s

```

O relatório gerado pelo k6 contém uma variedade de métricas, incluindo:
 - Tempo de resposta
 - Taxa de transferência
 - Taxa de erro
 - Utilização de recursos

Estas métricas podem ser usadas para avaliar o desempenho do sistema e identificar quaisquer gargalos ou problemas.

## Conclusão
Neste exercício, aprendemos como usar o k6 para realizar testes de carga em um sistema. Também aprendemos sobre os conceitos de teste de carga e teste de estresse.

O k6 é uma ferramenta poderosa que pode ser usada para avaliar o desempenho de um sistema e identificar quaisquer gargalos ou problemas. Os testes de carga e estresse são essenciais para garantir o desempenho e a confiabilidade de um sistema.
