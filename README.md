# Portfolio Django — Francisco Pearson (22308485)

Projeto desenvolvido no âmbito da disciplina de **Programação Web**  
Universidade Lusófona — Informática de Gestão — 2025/2026

## Tecnologias
- Python 3.12 / Django 6.0
- SQLite
- HTML, CSS
- GitHub Codespaces

## Como instalar e correr

```bash
git clone https://github.com/FranciscoPearson22308485/Francisco-pearson-22308485
cd Francisco-pearson-22308485
pip install -r requirements.txt
cp .env.example .env  # preencher com credenciais Gmail
python manage.py migrate
python manage.py runserver
```

## Funcionalidades

### Autenticação
- Login e logout com username/password
- Registo de novos utilizadores
- Magic Link por email (Gmail SMTP)
- Grupos e permissões: `gestor-portfolio` e `autores`

### Portfolio
- Projetos, Tecnologias, Competências, Formações, UCs, Interesses
- CRUD completo protegido por permissões
- Making Of com histórico de decisões

### Artigos
- Criação e edição de artigos (só autores)
- Sistema de Likes (qualquer visitante)
- Comentários (utilizadores autenticados)
- Autores só editam os seus próprios artigos

## Credenciais de teste
- **Admin:** `admin` / `root2004`
- **URL:** https://cautious-space-umbrella-97g6ww5x59rx2px9g-8000.app.github.dev
