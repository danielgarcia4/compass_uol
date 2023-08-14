## Técnicas de Processamento de Dados

O processamento em lote, ou do inglês ***Batch processing***, é o processamento que acontece em blocos de dados que já foram armazenados durante um período de tempo, ou seja, é o processamento de diversas transações que ocorreram num sistema de origem e serão processadas para outros sistemas em conjunto ou em bloco.

O ***Hadoop MapReduce*** é um dos melhores frameworks para processar dados em lotes.

O **processamento *stream*** trabalha com fluxos de dados que são capturados em tempo real e processados com latência mínima para o sistema de destino. Neste processamento uma ou um pequeno conjunto de transações é processada e enviada ao sistema de destino.

## Business Intelligence (BI)

É um conjunto de teorias, metodologias, práticas, processos, tecnologias e estruturas para desenvolver uma inteligência ao negócio.

As principais funções de um BI são: relatórios, análises, mineração de dados, processamento de eventos complexos, gerenciamento de desempenho dos negócios, benchmarking, mineração de dados, análises previsíveis e análises prescritivas.

## Data Warehouse (DW)

Tem por objetivo a centralização dos dados retirados de diversas origens para facilitar ou simplificar o consumo futuro. É um repositório centralizado otimizado para análises. De um DW pode-se extrair: Relatórios, Relatórios ad-hoc e Análises.

Um DW possui diversos Data marts e um **Data mart** é um pequeno DW ou uma pequena parte de um DW, que atende às necessidades de uma equipe ou unidade de negócios específica.

## Slowly Changing Dimension (SCD)

Serve para armazenamento de dados históricos. Um SCD é uma dimensão que armazena e gerencia dados atuais e históricos ao longo do tempo em um data warehouse. Existem 4 tipos:

* **SCD Tipo 1 (Sobreposição)**: é o comportamento padrão de um objeto, sem versionamento. Os novos dados substituem os dados existentes

* **SCD Tipo 2 (Criação de novo registro):** é a técnica mais utilizada para atualizações de dimensões. Mantém o histórico completo dos valores. Quando o valor de um atributo é alterado, o registro atual é fechado. Um novo registro é criado com os valores de dados alterados e esse novo registro se torna o registro vigente/atual. Cada registro contém o tempo efetivo e o tempo de expiração para identificar o período de tempo entre o qual o registro estava ativo.

* **SCD Tipo 3 (Criação de novo campo):** armazena duas versões de valores para determinados atributos. Cada registro armazena o valor anterior e o valor atual do atributo. Ou seja, cria uma coluna nova para cada coluna modificada.

* **SCD Tipo 6 ou SCD Híbrido:** pode combinar todos os tipos de SCD anteriores.

## Mineração de Dados

É o processo de descobrir correlações, padrões e tendências significativas analisando grandes quantidades de dados armazenados em repositórios. A mineração de dados emprega tecnologias de reconhecimento de padrões, bem como técnicas estatísticas e matemáticas. Compreende a **estatística**, **inteligência artificial** e ***machine learning***.

## Machine Learning

É uma espécie de inteligência artificial que é responsável por fornecer aos computadores a capacidade de aprender sobre novos conjuntos de dados sem serem programados por meio de uma fonte explícita. São algoritmos avançados de aprendizado de máquina compostos de muitas tecnologias (como ***deep learning***, **redes neurais** e **processamento de linguagem natural**), usadas em aprendizado supervisionado e não supervisionado, que operam guiados por lições de informações existentes.

**Algoritmos de aprendizado supervisionado** são treinados por meio de exemplos rotulados, como uma entrada na qual a saída desejada é conhecida. O **aprendizado não-supervisionado** é utilizado contra dados que não possuem rótulos históricos. O **aprendizado semi-supervisionado** é utilizado para as mesmas aplicações que o aprendizado supervisionado, mas manipula tanto dados rotulados quanto não-rotulados para treinamento. O **aprendizado por reforço** descobre através de testes do tipo 'tentativa e erro' quais ações rendem as maiores recompensas. Este tipo de aprendizado possui três componentes principais: o agente (o aprendiz ou tomador de decisão), o ambiente (tudo com que o agente interage) e ações (o que o agente pode fazer).

## Deep Learning

É um tipo de ***machine learning*** com o objetivo de treinar computadores para realizar tarefas como seres humanos, o que inclui reconhecimento de fala, identificação de imagem e previsões.

## Relatórios

É um documento que apresenta informações em um formato organizado para um público específico e propósito.

## Dashboards

É um indicador de negócios, pode ser um número ou um gráfico.


## Internet das coisas (IoT)

É a rede de objetos físicos que contém tecnologia embarcada para comunicar e sentir ou interagir com seus estados internos ou com o ambiente externo. Em outras palavras, são dispositivos físicos capazes de coletar e transmitir dados.

## API

Uma API, do inglês ***Application Program Interface***, é um conjunto de rotinas, protocolos e ferramentas para criar aplicativos de software. Basicamente, uma API especifica como os componentes de software devem interagir.

## Atalhos
[Voltar para o README.md da raiz](/README.md)