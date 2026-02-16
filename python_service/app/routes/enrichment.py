# =============================================================================
# app/routes/enrichment.py — Dados Financeiros e Odds
# =============================================================================
# - Transfermarkt: Valor de mercado, idade, contrato.
# - SoccerAPI: Odds (Bet365 scraper ou fallback).
# =============================================================================

from fastapi import APIRouter
from pydantic import BaseModel
import requests
import re
from lxml import html as lxml_html

router = APIRouter(prefix="/enrich", tags=["enrichment"])

# ---------------------------------------------------------------------------
# Configuração
# ---------------------------------------------------------------------------
HEADERS_TM = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# ---------------------------------------------------------------------------
# Models
# ---------------------------------------------------------------------------
class TransfermarktRequest(BaseModel):
    query: str  # Nome do jogador ou time
    type: str = "player" # player | team

class TransfermarktResponse(BaseModel):
    name: str
    market_value: str
    age: str
    position: str
    contract_expires: str
    image_url: str
    profile_url: str
    found: bool
    results: list[dict] = []

class OddsRequest(BaseModel):
    home_team: str
    away_team: str

class OddsResponse(BaseModel):
    bookmaker: str
    home_win: float
    draw: float
    away_win: float
    found: bool

# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------

@router.post("/transfermarkt", response_model=TransfermarktResponse)
async def get_transfermarkt_data(payload: TransfermarktRequest):
    """
    Busca dados no Transfermarkt com Parse Inteligente de Título.
    """
    # 1. Tenta extrair times do título (ex: "Girona x Barcelona")
    query_clean = payload.query
    search_queries = [payload.query] # Default: busca o que veio
    
    # Regex para "Time A x Time B" ou "Time A vs Time B"
    match = re.search(r'(.*?)\s+(?:x|vs|v|-)\s+(.*)', payload.query, re.IGNORECASE)
    if match:
        t1 = match.group(1).strip()
        t2 = match.group(2).strip().split(' ')[0] # Pega só a primeira palavra do segundo time para evitar lixo do final ("- Campeonato...")
        search_queries = [t1, t2]
    
    results = []
    
    # Busca cada entidade encontrada
    for q in search_queries:
        if len(q) < 3: continue
        
        url = f"https://www.transfermarkt.com/schnellsuche/ergebnis/schnellsuche?query={q}"
        try:
            r = requests.get(url, headers=HEADERS_TM, timeout=5)
            if r.status_code == 200:
                tree = lxml_html.fromstring(r.content)
                # Tenta pegar o primeiro resultado da tabela de times ou jogadores
                # ... Lógica simplificada: Pega o primeiro item da tabela "items"
                nodes = tree.xpath('//div[@class="box"]//table[@class="items"]//tbody/tr')
                if nodes:
                    first = nodes[0]
                    name_node = first.xpath('.//td[@class="hauptlink"]//a')
                    img_node = first.xpath('.//td//img/@src')
                    value_node = first.xpath('.//td[@class="rechts hauptlink"]')
                    
                    if name_node:
                        name = name_node[0].text_content().strip()
                        link = "https://www.transfermarkt.com" + name_node[0].get('href')
                        img = img_node[0] if img_node else ""
                        val = value_node[0].text_content().strip() if value_node else "?"
                        
                        results.append({
                            "name": name,
                            "market_value": val,
                            "profile": link,
                            "image": img,
                            "query_used": q
                        })
        except Exception:
            pass

    if results:
        # Retorna o primeiro como "principal" mas anexa todos em results
        best = results[0]
        return TransfermarktResponse(
            name=best['name'],
            market_value=best['market_value'],
            age="?",
            position="?",
            contract_expires="?",
            image_url=best['image'],
            profile_url=best['profile'],
            found=True,
            results=results
        )

    # Fallback para busca original se nada acima funcionou
    search_url = f"https://www.transfermarkt.com/schnellsuche/ergebnis/schnellsuche?query={payload.query}"
    
    try:
        r = requests.get(search_url, headers=HEADERS_TM, timeout=10)
        if r.status_code != 200:
            return TransfermarktResponse(name=payload.query, market_value="", age="", position="", contract_expires="", image_url="", profile_url="", found=False)
        
        tree = lxml_html.fromstring(r.content)
        
        # Lógica simplificada de busca correta (assumindo que o primeiro resultado é o desejado)
        # O layout do TM muda, mas geralmente jogadores estão numa tabela específica.
        
        # Tenta pegar o primeiro jogador da lista de resultados
        # Xpath aproximado para a tabela de jogadores
        player_nodes = tree.xpath('//div[@class="box"]//table[@class="items"]//tbody/tr')
        
        if not player_nodes:
             # Tenta fallback se for time? (futuro)
             return TransfermarktResponse(name=payload.query, market_value="", age="", position="", contract_expires="", image_url="", profile_url="", found=False)
             
        first_player = player_nodes[0]
        
        # Extração (Varia muito com layout mobile/desktop, tentando desktop)
        # Nome e Link
        name_link = first_player.xpath('.//td[@class="hauptlink"]//a')
        
        if not name_link:
             # Tente outro layout (odd/even rows)
             return TransfermarktResponse(name=payload.query, market_value="", age="", position="", contract_expires="", image_url="", profile_url="", found=False)

        full_name = name_link[0].text_content().strip()
        profile_url = "https://www.transfermarkt.com" + name_link[0].get('href')

        # Idade
        age_nodes = first_player.xpath('.//td[position()=4]') 
        age = age_nodes[0].text_content().strip() if age_nodes else "?"

        # Posição
        pos_nodes = first_player.xpath('.//td[position()=2]') # As vezes é a 2a td
        position = pos_nodes[0].text_content().strip() if pos_nodes else "?"
        
        # Valor de Mercado
        value_nodes = first_player.xpath('.//td[@class="rechts hauptlink"]')
        market_value = value_nodes[0].text_content().strip() if value_nodes else "?"

        # Imagem
        img_nodes = first_player.xpath('.//td//img/@src')
        image_url = img_nodes[0] if img_nodes else ""

        return TransfermarktResponse(
            name=full_name,
            market_value=market_value,
            age=age,
            position=position,
            contract_expires="?", # Difícil pegar na busca rapida
            image_url=image_url,
            profile_url=profile_url,
            found=True,
            results=[{
                "name": full_name,
                "type": "player",
                "market_value": market_value,
                "image": image_url
            }]
        )

    except Exception as e:
        print(f"[Transfermarkt] Query: {payload.query} | Erro: {e}")
        return TransfermarktResponse(name=payload.query, market_value="", age="", position="", contract_expires="", image_url="", profile_url="", found=False)


@router.post("/odds", response_model=OddsResponse)
async def get_odds(payload: OddsRequest):
    """
    Busca odds (Mock/Placeholder para futura implementação complexa de scraping ou API externa).
    Scraping de Bet365 é extremamente difícil de manter em container sem browser real (anti-bot).
    Retornamos 'not found' para que o n8n use o fallback do API-Football se necessário.
    """
    # TODO: Implementar scraper real se o usuário fornecer proxy residencial ou API paga.
    return OddsResponse(
        bookmaker="None",
        home_win=0.0,
        draw=0.0,
        away_win=0.0,
        found=False
    )


class FixturesRequest(BaseModel):
    query: str

class FixturesResponse(BaseModel):
    fixtures: list[dict] = []
    found: bool = False

@router.post("/fixtures", response_model=FixturesResponse)
async def get_fixtures(payload: FixturesRequest):
    # Mock de Fixtures (Fallback para evitar travamento do n8n)
    # Retorna um jogo "dummy" se não encontrar nada real
    return FixturesResponse(
        fixtures=[
            {
                "home_team": "Time Casa",
                "away_team": "Time Visitante",
                "date": "2024-12-31",
                "status": "Not Found - Fallback",
                "league": "Amistoso",
                "prediction": "Sem dados"
            }
        ],
        found=True
    )


# ---------------------------------------------------------------------------
# TheSportsDB Logic (New)
# ---------------------------------------------------------------------------

class SportsDBRequest(BaseModel):
    query: str

class SportsDBResponse(BaseModel):
    teams: list[dict] = []
    players: list[dict] = []
    found: bool

@router.post("/sportsdb", response_model=SportsDBResponse)
async def get_sportsdb_data(payload: SportsDBRequest):
    """
    Busca dados no TheSportsDB (Teams ou Players).
    Parse inteligente de título para decidir estratégia.
    """
    # 1. Tenta extrair times do título (ex: "Girona x Barcelona")
    # Regex para "Time A x Time B" ou "Time A vs Time B"
    match = re.search(r'(.*?)\s+(?:x|vs|v|-)\s+(.*)', payload.query, re.IGNORECASE)
    teams_found = []
    
    if match:
        t1 = match.group(1).strip()
        t2 = match.group(2).strip().split(' ')[0] # Pega só a primeira palavra do segundo time
        queries = [t1, t2]
    else:
        queries = [payload.query]
        
    # Busca Times
    for q in queries:
        if len(q) < 3: continue
        try:
            url = f"https://www.thesportsdb.com/api/v1/json/3/searchteams.php?t={q}"
            r = requests.get(url, timeout=5)
            if r.status_code == 200:
                data = r.json()
                if data.get('teams'):
                    for team in data['teams']:
                        # Filtro básico de esporte (Soccer)
                        if team.get('strSport') == 'Soccer':
                            teams_found.append({
                                "name": team.get('strTeam'),
                                "league": team.get('strLeague'),
                                "badge": team.get('strTeamBadge'),
                                "description": team.get('strDescriptionPT') or team.get('strDescriptionEN') or ""
                            })
                            break # Pega só o primeiro match relevante por query
        except Exception as e:
            print(f"[SportsDB] Erro buscando time {q}: {e}")

    # Se não achou times, ou se parece ser sobre jogador, tenta busca de players
    players_found = []
    if not teams_found:
        try:
             url = f"https://www.thesportsdb.com/api/v1/json/3/searchplayers.php?p={payload.query}"
             r = requests.get(url, timeout=5)
             if r.status_code == 200:
                 data = r.json()
                 if data.get('player'):
                     for p in data['player']:
                         if p.get('strSport') == 'Soccer':
                             players_found.append({
                                 "name": p.get('strPlayer'),
                                 "team": p.get('strTeam'),
                                 "thumb": p.get('strThumb'),
                                 "description": p.get('strDescriptionPT') or p.get('strDescriptionEN') or ""
                             })
                             break
        except Exception as e:
            print(f"[SportsDB] Erro buscando player {payload.query}: {e}")
            
    return SportsDBResponse(
        teams=teams_found,
        players=players_found,
        found=(len(teams_found) > 0 or len(players_found) > 0)
    )
