# Portfólio Django — Ficha 6
**Francisco Pearson | 22308485 | Informática de Gestão**  
**Universidade Lusófona | Programação Web | Prof. Lúcio Studer**

## Credenciais Admin
| Campo    | Valor    |
|----------|----------|
| Username | admin    |
| Password | root2004 |

## Lançar a aplicação
```bash
python manage.py runserver
```

## Carregar dados
```bash
python manage.py load_tfcs       # carrega 595 TFCs do JSON
python manage.py load_ucs_api    # importa Licenciatura e UCs da API Lusófona
```

## Modelos do Portfólio
- **Licenciatura** — curso que frequento
- **Docente** — professores das UCs
- **UnidadeCurricular** — disciplinas do curso
- **Tecnologia** — linguagens, frameworks e ferramentas
- **Projeto** — projectos realizados nas UCs
- **TFC** — trabalhos finais de curso do DEISI (595 registos)
- **Competência** — competências técnicas e soft skills
- **Formação** — cursos e certificações
- **Interesse** — interesses pessoais e profissionais *(entidade adicional)*
- **MakingOf** — registo do processo de desenvolvimento

## Making Of
Ver ficheiro [making_of.md](making_of.md)