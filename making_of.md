# Making Of — Portfólio Django
**Francisco Pearson | 22308485 | Informática de Gestão | Universidade Lusófona**

---

## Licenciatura
**Atributos:** nome, sigla, instituicao, ano_inicio, duracao_anos, url_pagina

**Justificação 1:** Escolhi `sigla` como identificador rápido porque é como
os alunos e professores identificam o curso no dia-a-dia (ex: "IG").

**Justificação 2:** `url_pagina` permite ligar directamente ao site oficial
da Lusófona, útil para quem visitar o portfólio querer saber mais.

---

## Docente
**Atributos:** nome, email, url_pagina_lusofona, foto

**Justificação 1:** Separei Docente de UnidadeCurricular com ManyToMany
porque um docente pode leccionar várias UCs e uma UC pode ter co-regência
— evita duplicação de dados.

**Justificação 2:** `url_pagina_lusofona` permite ligar ao perfil oficial
do docente, tornando o portfólio mais profissional e verificável.

---

## UnidadeCurricular
**Atributos:** nome, sigla, ano_curricular, semestre, descricao, ects, imagem

**Justificação 1:** `ects` é relevante para mostrar o peso académico de
cada UC — útil em contexto de entrevista para explicar a carga de trabalho.

**Justificação 2:** `imagem` permite associar um visual a cada UC,
tornando o portfólio mais apelativo visualmente.

---

## Tecnologia
**Atributos:** nome, descricao, logo, url_oficial, categoria, nivel_interesse

**Justificação 1:** `nivel_interesse` (escala 1-5) permite mostrar não só
o que sei mas o que gosto mais — diferenciador em entrevistas.

**Justificação 2:** `categoria` com choices (Linguagem, Framework, BD, etc.)
permite filtrar e organizar as tecnologias por tipo na página do portfólio.

---

## Projeto
**Atributos:** titulo, descricao, data_inicio, data_fim, imagem, url_github,
url_demo, conceitos_uc, FK:uc, M2M:tecnologias

**Justificação 1:** `url_github` é o atributo mais importante para
entrevistas de emprego — permite ao recrutador ver o código real.

**Justificação 2:** FK para UnidadeCurricular liga cada projecto à
disciplina onde foi desenvolvido, dando contexto académico.

---

## TFC
**Atributos:** titulo, autor, orientador, ano, resumo, url, area, destacado,
M2M:tecnologias

**Justificação 1:** `destacado` (BooleanField) permite filtrar os TFCs
mais interessantes sem eliminar os restantes da base de dados.

**Justificação 2:** M2M com Tecnologia permite cruzar TFCs com as
tecnologias que já conheço — útil para perceber o que está a ser usado
na investigação da área.

---

## Competência
**Atributos:** nome, descricao, nivel, tipo, M2M:tecnologias, M2M:projetos

**Justificação 1:** Dois tipos (Técnica / Soft Skill) porque ambas são
valorizadas em CVs e entrevistas, mas de natureza diferente.

**Justificação 2:** M2M com Projeto permite mostrar onde cada
competência foi aplicada na prática, tornando-a verificável.

---

## Formação
**Atributos:** titulo, instituicao, data_inicio, data_conclusao, certificado,
url, tipo, M2M:tecnologias

**Justificação 1:** `ordering = ['-data_inicio']` na Meta garante que
as formações mais recentes aparecem primeiro automaticamente.

**Justificação 2:** `certificado` (FileField) permite anexar o PDF do
certificado directamente, tornando o portfólio auto-suficiente.

---

## Interesse
**Atributos:** nome, descricao, categoria, url

**Justificação 1:** Esta entidade não estava no enunciado — adicionei-a
porque um portfólio profissional deve mostrar a pessoa como um todo,
não só as competências técnicas.

**Justificação 2:** `categoria` com choices permite organizar interesses
por área (Tecnologia, Negócio, Desporto, etc.) para apresentação visual.

---

## MakingOf
**Atributos:** titulo, data, descricao, foto, tipo, entidade_relacionada,
FK:uc, FK:projeto

**Justificação 1:** `tipo` com choices (DER, Decisão, Erro, Justificação,
Evolução, IA) permite filtrar no Admin por categoria de registo.

**Justificação 2:** Adicionei FKs opcionais para UC e Projeto porque são
as entidades com mais decisões de modelação documentadas — permite ligar
cada registo ao dado real correspondente.

---

## Uso de Inteligência Artificial
Utilizei o Claude (Anthropic) como mentor e explicador Django ao longo
do desenvolvimento. A IA ajudou a estruturar os modelos, corrigir erros
e guiar o processo passo a passo. Todas as decisões de modelação foram
tomadas por mim e sou capaz de as justificar e alterar na defesa.
O Claude foi usado como apoio, não como substituição do meu pensamento.

---

## Erros encontrados e correcções
- **Erro:** Colei código Python directamente no terminal bash →
  **Correcção:** Abri o ficheiro com `code portfolio/models.py` e editei
  no VS Code.
- **Erro:** API da Lusófona inacessível no Codespaces por timeout →
  **Correcção:** Inseri a Licenciatura e UCs manualmente no Admin.
- **Erro:** Servidor Django não acessível no browser →
  **Correcção:** Usei `runserver 0.0.0.0:8000` e tornei a porta pública
  no separador PORTS do Codespaces.