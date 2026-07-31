# Project Cover Zero — Backlog

Registro de funcionalidades, decisões, ideias futuras e questões em aberto.

## Objetivo central

Desenvolver um sistema capaz de analisar e representar a mudança de identidade de cada time da NFL ao longo da temporada, semana após semana.

O sistema deve identificar como o comportamento de uma equipe evolui com base em aspectos como:

* estilo de jogo;
* distribuição das chamadas;
* eficiência ofensiva e defensiva;
* uso dos jogadores;
* escolhas táticas;
* contexto das partidas.

Toda funcionalidade, métrica ou análise adicionada ao projeto deve contribuir, direta ou indiretamente, para responder à seguinte pergunta:

> **Como a identidade deste time mudou em relação às semanas anteriores?**

O objetivo do projeto não é apenas apresentar estatísticas da NFL. As estatísticas, métricas e visualizações são ferramentas para identificar mudanças no comportamento e na identidade das equipes.

## Concluído

* [x] Configurar Python e ambiente virtual.
* [x] Configurar Git.
* [x] Carregar play-by-play com `nflreadpy`.
* [x] Converter os dados para pandas.
* [x] Filtrar jogadas ofensivas por equipe.
* [x] Analisar corridas e passes por descida.
* [x] Calcular número e percentual de chamadas.
* [x] Calcular média de jardas por jogada.
* [x] Identificar jogadas que produziram first down ou touchdown.
* [x] Calcular taxa de conversão.
* [x] Calcular média de `ydstogo`.
* [x] Analisar terceiras e quartas descidas por distância.

## Definições atuais

### Primeiro time analisado

Baltimore Ravens (`BAL`).

### Conversão

Uma jogada é considerada convertida quando produz:

* first down; ou
* touchdown.

Em terceiras e quartas descidas, a métrica representa diretamente uma conversão.

Em primeiras e segundas descidas, representa a produção imediata de um novo first down ou touchdown.

### Grupos de distância

* Short: 1–3 jardas.
* Medium: 4–6 jardas.
* Long: 7 ou mais jardas.

## Próximas análises

* [ ] Investigar individualmente as corridas em terceira descida média.
* [ ] Investigar individualmente as corridas em terceira descida longa.
* [ ] Calcular a mediana de `ydstogo`.
* [ ] Comparar média e mediana de `ydstogo`.
* [ ] Validar a conversão usando campos específicos de terceira e quarta descidas.
* [ ] Investigar o impacto do tamanho da amostra.
* [ ] Separar temporada regular e playoffs.
* [ ] Adicionar EPA e success rate.
* [ ] Analisar personnel packages e formações.
* [ ] Separar as análises por semana.
* [ ] Comparar cada semana com as semanas anteriores.
* [ ] Definir critérios para identificar mudanças reais de identidade.
* [ ] Diferenciar mudanças estruturais de ajustes específicos para um adversário.

## Debates metodológicos

### Classificação das jogadas

* [ ] Definir o que será considerado uma corrida.
* [ ] Definir como as RPOs serão classificadas.
* [ ] Decidir se a classificação considerará:

  * a jogada chamada;
  * a decisão tomada pelo quarterback;
  * o resultado registrado no play-by-play.
* [ ] Definir como identificar screens.
* [ ] Diferenciar screens de passes curtos convencionais.
* [ ] Avaliar se passes atrás da linha de scrimmage devem formar uma categoria própria.

### Corridas de quarterback

* [ ] Separar corridas desenhadas de scrambles.
* [ ] Identificar zone reads e option plays.
* [ ] Identificar quarterback sneaks.
* [ ] Identificar corridas causadas por pressão ou quebra da jogada.
* [ ] Definir como avaliar scrambles.
* [ ] Definir como avaliar corridas desenhadas de quarterback.
* [ ] Decidir se os diferentes tipos de corrida de quarterback devem possuir métricas ou pesos diferentes.
* [ ] Avaliar como representar times nos quais a mobilidade do quarterback é parte central da identidade ofensiva.

### Jogo aéreo e distribuição de passes

* [ ] Identificar para qual posição cada passe foi direcionado.
* [ ] Separar targets para:

  * wide receivers;
  * tight ends;
  * running backs;
  * outros jogadores elegíveis.
* [ ] Analisar a distribuição de targets por posição.
* [ ] Analisar a distribuição de targets por jogador.
* [ ] Considerar targets sem recepção.
* [ ] Separar passes por profundidade.
* [ ] Analisar passes atrás da linha de scrimmage.
* [ ] Analisar passes curtos, intermediários e profundos.
* [ ] Separar air yards de YAC.
* [ ] Avaliar a importância de YAC para a identidade ofensiva.
* [ ] Diferenciar produção do quarterback de produção do recebedor após a recepção.

### Avaliação dos drives

* [ ] Definir como avaliar drives que terminam em touchdown.
* [ ] Definir como avaliar drives que terminam em field goal.
* [ ] Definir como avaliar drives que terminam em punt.
* [ ] Definir como avaliar drives que terminam em turnover.
* [ ] Definir como avaliar drives que terminam em turnover on downs.
* [ ] Definir como avaliar drives encerrados pelo fim do primeiro tempo.
* [ ] Definir como avaliar drives encerrados pelo fim da partida.
* [ ] Separar resultado do drive e qualidade das jogadas do drive.
* [ ] Considerar posição inicial e posição final de campo.
* [ ] Considerar número de jogadas.
* [ ] Considerar jardas conquistadas.
* [ ] Considerar tempo consumido.
* [ ] Avaliar se um drive terminado em punt pode ser considerado positivo.
* [ ] Avaliar drives que melhoram significativamente a posição de campo.
* [ ] Avaliar drives iniciados em condições desfavoráveis.

### Sacks e pressões

* [ ] Definir como os sacks serão tratados nas análises de passe.
* [ ] Definir como avaliar sacks sofridos.
* [ ] Definir como avaliar sacks produzidos pela defesa.
* [ ] Avaliar a responsabilidade do quarterback.
* [ ] Avaliar a responsabilidade da linha ofensiva.
* [ ] Avaliar sacks causados pela cobertura defensiva.
* [ ] Diferenciar pressão rápida de quarterback segurando a bola.
* [ ] Diferenciar sack de scramble que termina atrás da linha de scrimmage.
* [ ] Avaliar o impacto dos sacks sobre os drives.
* [ ] Avaliar o impacto dos sacks sobre EPA e success rate.
* [ ] Investigar a disponibilidade de dados de pressão no conjunto utilizado.

### Faltas

* [ ] Definir como incorporar faltas às análises.
* [ ] Identificar a equipe penalizada.
* [ ] Identificar o jogador penalizado, quando disponível.
* [ ] Identificar o tipo de falta.
* [ ] Separar faltas aceitas e recusadas.
* [ ] Identificar jogadas anuladas.
* [ ] Considerar jardas da penalidade.
* [ ] Considerar first downs automáticos.
* [ ] Avaliar jogadas positivas anuladas por faltas.
* [ ] Avaliar faltas que evitam touchdowns ou grandes ganhos.
* [ ] Avaliar faltas defensivas que evitam recepções.
* [ ] Avaliar faltas ofensivas que anulam jogadas explosivas.
* [ ] Definir se as faltas representarão:

  * disciplina;
  * agressividade;
  * estilo tático;
  * uma dimensão separada da identidade.
* [ ] Evitar que faltas distorçam métricas de eficiência.

### Contexto da jogada

* [ ] Incorporar down.
* [ ] Incorporar distância para o first down.
* [ ] Incorporar posição de campo.
* [ ] Incorporar diferença no placar.
* [ ] Incorporar quarto da partida.
* [ ] Incorporar tempo restante.
* [ ] Identificar red zone.
* [ ] Identificar goal line.
* [ ] Identificar two-minute drill.
* [ ] Identificar short yardage.
* [ ] Identificar garbage time.
* [ ] Identificar drives destinados a consumir o relógio.
* [ ] Avaliar a força do adversário.
* [ ] Evitar comparar jogadas estatisticamente semelhantes em contextos diferentes.

### Eficiência, explosividade e consistência

* [ ] Definir como medir eficiência.
* [ ] Definir como medir explosividade.
* [ ] Definir como medir consistência.
* [ ] Calcular frequência de jogadas negativas.
* [ ] Diferenciar ataques consistentes de ataques dependentes de grandes jogadas.
* [ ] Avaliar a dispersão dos resultados por jogada.
* [ ] Avaliar a proporção da produção ofensiva gerada por jogadas explosivas.

### Turnovers

* [ ] Definir como avaliar interceptações.
* [ ] Definir como avaliar fumbles.
* [ ] Separar fumbles perdidos e recuperados pela própria equipe.
* [ ] Avaliar a responsabilidade do quarterback.
* [ ] Avaliar a responsabilidade do recebedor.
* [ ] Avaliar a influência da proteção.
* [ ] Considerar o contexto da jogada.
* [ ] Identificar passes desesperados no fim do tempo ou da partida.
* [ ] Avaliar o impacto do turnover sobre o drive.
* [ ] Avaliar o impacto da posição de campo do turnover.

### Situações especiais

* [ ] Analisar terceiras descidas.
* [ ] Analisar quartas descidas.
* [ ] Analisar red zone.
* [ ] Analisar goal line.
* [ ] Analisar two-minute drill.
* [ ] Analisar short yardage.
* [ ] Analisar drives de consumo de relógio.
* [ ] Analisar garbage time.
* [ ] Analisar jogadas após turnovers.
* [ ] Analisar comportamento quando o time está vencendo.
* [ ] Analisar comportamento quando o time está perdendo.

### Pessoal e estrutura ofensiva

* [ ] Identificar personnel packages.
* [ ] Identificar formações ofensivas.
* [ ] Identificar a formação.
* [ ] Analisar uso de motion.
* [ ] Analisar uso de shifts.
* [ ] Analisar uso de play-action.
* [ ] Avaliar mudanças de pessoal ao longo das semanas.
* [ ] Avaliar se mudanças de formação representam mudanças reais de identidade.

### Qualidade do adversário

* [ ] Ajustar métricas pela qualidade do adversário.
* [ ] Comparar desempenho contra defesas fortes e fracas.
* [ ] Definir quantas semanas são necessárias para identificar uma tendência.
* [ ] Diferenciar uma atuação isolada de uma mudança estrutural.
* [ ] Diferenciar game plan específico de mudança de identidade.
* [ ] Comparar o desempenho observado com o desempenho normalmente permitido pelo adversário.

## Métricas futuras

* [ ] Jogadas explosivas.

  * Passe: 20 ou mais jardas.
  * Corrida: 10 jardas ou mais
* [ ] Taxa de conversão por jogador.
* [ ] Eficiência por situação do placar.
* [ ] Eficiência por quarto.
* [ ] Comparação com a média da liga.
* [ ] EPA por jogada.
* [ ] Success rate.
* [ ] Taxa de jogadas negativas.
* [ ] Taxa de sacks.
* [ ] Taxa de scrambles.
* [ ] Taxa de corridas desenhadas de quarterback.
* [ ] YAC por recepção.
* [ ] YAC por target.
* [ ] Air yards por tentativa.
* [ ] Distribuição de targets por posição.
* [ ] Distribuição de targets por jogador.
* [ ] Taxa de screens.
* [ ] Taxa de play-action.
* [ ] Taxa de passes por profundidade.
* [ ] Pontos por drive.
* [ ] EPA por drive.
* [ ] Jardas por drive.
* [ ] Jogadas por drive.
* [ ] Tempo médio por drive.
* [ ] Taxa de drives terminados em touchdown.
* [ ] Taxa de drives terminados em field goal.
* [ ] Taxa de drives terminados em punt.
* [ ] Taxa de turnovers por drive.
* [ ] Índice de mudança semanal de identidade.
* [ ] Distância entre o perfil atual e o perfil das semanas anteriores.

## Identidade defensiva

* [ ] Definir quais dimensões representarão a identidade defensiva.
* [ ] Analisar frequência de blitz.
* [ ] Analisar geração de pressão.
* [ ] Analisar sacks.
* [ ] Analisar defesa contra corrida.
* [ ] Analisar passes curtos permitidos.
* [ ] Analisar passes profundos permitidos.
* [ ] Analisar YAC permitido.
* [ ] Analisar tackles.
* [ ] Analisar turnovers forçados.
* [ ] Analisar desempenho por down.
* [ ] Analisar desempenho por distância.
* [ ] Analisar desempenho por situação de jogo.
* [ ] Investigar a disponibilidade de dados sobre coberturas defensivas.

## Times especiais

Itens inicialmente fora do núcleo da primeira versão, mas relevantes para a identidade completa de uma equipe.

* [ ] Analisar punts.
* [ ] Analisar distância e posição dos punts.
* [ ] Analisar field goals.
* [ ] Analisar retornos.
* [ ] Analisar posição de campo gerada pelos times especiais.
* [ ] Analisar decisões de quarta descida.
* [ ] Analisar o impacto dos times especiais sobre o início dos drives.

## Interface futura

* [ ] Seletor de equipe.
* [ ] Seletor de temporada.
* [ ] Seletor de semana.
* [ ] Intervalo de semanas para comparação.
* [ ] Atualização automática das análises.
* [ ] Tela principal com métricas resumidas.
* [ ] Opção “Mais detalhes”.
* [ ] Gráfico da distribuição de `ydstogo` por descida.
* [ ] Exibir média e mediana de `ydstogo`.
* [ ] Filtro entre corrida, passe e ambos.
* [ ] Filtro por tipo de corrida de quarterback.
* [ ] Filtro por posição do recebedor.
* [ ] Filtro por resultado do drive.
* [ ] Filtro por situação do placar.
* [ ] Filtro por quarto.
* [ ] Aviso visual para amostras pequenas.
* [ ] Permitir configurar a definição de jogada explosiva.
* [ ] Exibir comparação entre semanas.
* [ ] Destacar as maiores mudanças de comportamento.
* [ ] Exibir evolução das métricas ao longo da temporada.
* [ ] Exibir resumo textual da identidade atual do time.

## Questões em aberto

* Como tratar first downs causados por penalidade?
* Como tratar sacks nas análises de passe?
* O que exatamente será considerado uma corrida?
* Como as RPOs serão classificadas?
* Como separar corridas desenhadas de quarterback e scrambles?
* Como identificar screens?
* Como separar air yards e YAC?
* Como avaliar drives que terminam em touchdown, field goal ou punt?
* Um punt pode representar um resultado positivo para um drive?
* Como avaliar turnovers?
* Como incorporar faltas sem distorcer as métricas?
* Como ajustar as análises pelo contexto da jogada?
* Como ajustar as métricas pela qualidade do adversário?
* Quantas semanas são necessárias para identificar uma mudança de identidade?
* Como diferenciar mudança estrutural de game plan específico?
* Como medir numericamente a mudança de identidade entre semanas?
* Quais métricas devem aparecer na tela principal?
* Qual tamanho mínimo de amostra deve gerar um alerta?
* A classificação short/medium/long deve ser configurável?
* A primeira versão deve analisar apenas o ataque?
* Em qual etapa defesa e times especiais serão incorporados?

## Tabela-base de contexto das jogadas

Criar uma tabela inspirada no modelo apresentado em *Take Your Eye Off the Ball 2.0*, de Pat Kirwan.

Cada linha da tabela deverá representar uma jogada, relacionando o contexto enfrentado pela equipe, o personnel utilizado, a chamada realizada e o resultado obtido.

### Estrutura principal

* [ ] Incluir equipe.
* [ ] Incluir semana.
* [ ] Incluir adversário.
* [ ] Incluir down.
* [ ] Incluir distância para o first down.
* [ ] Incluir posição de campo.
* [ ] Incluir personnel.
* [ ] Incluir tipo de jogada.
* [ ] Incluir o tempo no relógio.
* [ ] Incluir resultado da jogada.

Estrutura conceitual:

| Semana | Time | Down e distância | Posição de campo | Personnel | Tempo | | Jogada | Resultado |
| ------ | ---- | ---------------- | ---------------- | --------- | ----- | | ------ | --------- |

### Identificação da jogada

* [ ] Identificar corrida ou passe.
* [ ] Identificar o subtipo da jogada, quando possível.
* [ ] Identificar corridas desenhadas de quarterback.
* [ ] Identificar scrambles.
* [ ] Identificar screens.
* [ ] Identificar play-action.
* [ ] Identificar RPOs.
* [ ] Identificar sacks.
* [ ] Identificar turnovers.
* [ ] Identificar faltas.

### Resultado da jogada

* [ ] Registrar jardas conquistadas.
* [ ] Registrar first down.
* [ ] Registrar touchdown.
* [ ] Registrar EPA.
* [ ] Registrar success.
* [ ] Registrar turnover.
* [ ] Registrar sack.
* [ ] Registrar penalidade.
* [ ] Registrar se a jogada foi anulada.

### Contexto adicional do Project Cover Zero

Além das informações presentes no modelo original, incluir campos necessários para analisar mudanças semanais de identidade:

* [ ] Número do jogo.
* [ ] Número do drive.
* [ ] Número da jogada.
* [ ] Quarto da partida.
* [ ] Tempo restante.
* [ ] Diferença no placar.
* [ ] Posição inicial do drive.
* [ ] Formação ofensiva, quando disponível.
* [ ] Motion ou shift, quando disponível.
* [ ] Posição do jogador alvo.
* [ ] Identificação do carregador da bola.
* [ ] Situação especial da jogada:

  * red zone;
  * goal line;
  * two-minute drill;
  * short yardage;
  * garbage time.

### Utilização na análise de identidade

* [ ] Permitir a visualização das jogadas individualmente.
* [ ] Permitir filtros por semana.
* [ ] Permitir filtros por down e distância.
* [ ] Permitir filtros por posição de campo.
* [ ] Permitir filtros por personnel.
* [ ] Permitir filtros por tipo de jogada.
* [ ] Permitir filtros por resultado.
* [ ] Comparar a distribuição das chamadas entre semanas.
* [ ] Identificar quais jogadas são utilizadas em cada contexto.
* [ ] Identificar mudanças na relação entre contexto, personnel e chamada.
* [ ] Destacar comportamentos que surgiram, desapareceram ou ganharam frequência ao longo da temporada.

