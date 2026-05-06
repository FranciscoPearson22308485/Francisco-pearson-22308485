"""
Scraping dos docentes do curso de Informatica de Gestao
da Universidade Lusofona usando Playwright.

A pagina usa accordions UIKit que precisam ser clicados.
"""
from playwright.sync_api import sync_playwright
import re
import time

URL = "https://www.ulusofona.pt/lisboa/licenciaturas/informatica-de-gestao"

print("=" * 60)
print("SCRAPING DOCENTES - INFORMATICA DE GESTAO")
print("=" * 60)

with sync_playwright() as p:
    print("\n[1/6] Lancando Chromium...")
    browser = p.chromium.launch(headless=True)
    context = browser.new_context(
        viewport={"width": 1920, "height": 1080},
        user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
    )
    page = context.new_page()
    
    print(f"[2/6] Acedendo a: {URL}")
    page.goto(URL, wait_until="networkidle", timeout=60000)
    
    print("[3/6] Aguardando renderizacao (5s)...")
    time.sleep(5)
    
    # Aceitar cookies se aparecer
    try:
        page.click("button:has-text('PERMITIR')", timeout=3000)
        print("    -> Cookies aceites")
        time.sleep(2)
    except:
        try:
            page.click("button:has-text('Permitir')", timeout=2000)
            print("    -> Cookies aceites")
        except:
            print("    -> Sem popup de cookies")
    
    print("[4/6] Clicando em TODOS os accordions...")
    accordions = page.query_selector_all("a.uk-accordion-title")
    print(f"    -> Encontrados {len(accordions)} accordions")
    
    for i, acc in enumerate(accordions):
        try:
            titulo = acc.inner_text().strip()[:60]
            acc.scroll_into_view_if_needed()
            time.sleep(0.3)
            acc.click()
            print(f"    [{i+1}/{len(accordions)}] Clicado: {titulo}")
            time.sleep(0.8)
        except Exception as e:
            print(f"    [{i+1}] Falhou: {str(e)[:80]}")
    
    print("\n[5/6] Aguardando conteudo carregar (5s)...")
    time.sleep(5)
    
    # Salvar HTML completo
    html = page.content()
    with open('lusofona_page.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"    -> HTML guardado: lusofona_page.html ({len(html)} chars)")
    
    print("\n[6/6] Procurando 'Corpo Docente'...")
    print("=" * 60)
    
    # Procurar texto "Corpo Docente" no HTML
    idx_corpo = html.lower().find('corpo docente')
    
    if idx_corpo != -1:
        print(f"OK 'Corpo Docente' encontrado na posicao {idx_corpo}")
        
        # Pegar 50000 caracteres a partir de Corpo Docente
        secao = html[idx_corpo:idx_corpo + 50000]
        
        # Padrao para nomes proprios em texto: Nome Apelido (com acentos)
        padrao = re.compile(
            r'>\s*([A-ZÁÉÍÓÚÂÊÔÃÕÇÀ][a-záéíóúâêôãõçà]+(?:\s+(?:de|da|do|dos|das|e)?\s*[A-ZÁÉÍÓÚÂÊÔÃÕÇÀ][a-záéíóúâêôãõçà]+){1,5})\s*<'
        )
        matches = padrao.findall(secao)
        
        # Filtrar nomes plausiveis
        excluir = {
            'Corpo', 'Docente', 'Coordenacao', 'Coordenador', 'Coordenadora',
            'Universidade', 'Lusofona', 'Lusófona', 'Curso', 'Plano', 'Ano',
            'Semestre', 'Tronco', 'Comum', 'Sobre', 'Saber', 'Mais',
            'Despacho', 'Registo', 'Politica', 'Cookies', 'Permitir',
            'Rejeitar', 'Escolher', 'Servicos', 'Cinema', 'Fernando', 'Lopes',
            'Informatica', 'Gestao', 'Licenciatura', 'Mestrado', 'Doutoramento',
            'Anual', 'Ects', 'Funcoes', 'Departamento', 'Instituto',
            'Faculdade', 'Escola', 'Lisboa', 'Porto', 'Campus'
        }
        
        nomes_unicos = set()
        for nome in matches:
            nome = re.sub(r'\s+', ' ', nome).strip()
            palavras = nome.split()
            
            if 2 <= len(palavras) <= 5:
                # Excluir se primeira palavra esta na blacklist
                if palavras[0] not in excluir and palavras[-1] not in excluir:
                    # Excluir se TODAS palavras sao curtas
                    if not all(len(p) < 3 for p in palavras):
                        nomes_unicos.add(nome)
        
        nomes_ordenados = sorted(nomes_unicos)
        
        print(f"\nOK ENCONTRADOS {len(nomes_ordenados)} POSSIVEIS DOCENTES:")
        print("-" * 60)
        for i, nome in enumerate(nomes_ordenados, 1):
            print(f"  {i:2d}. {nome}")
        
        # Salvar lista para ficheiro
        with open('docentes_extraidos.txt', 'w', encoding='utf-8') as f:
            for nome in nomes_ordenados:
                f.write(nome + '\n')
        print(f"\n-> Lista guardada em: docentes_extraidos.txt")
    else:
        print("XX Nao encontrei 'Corpo Docente' no HTML")
        print("    Verifica lusofona_page.html manualmente")
    
    browser.close()

print("\n" + "=" * 60)
print("DONE!")
print("=" * 60)
