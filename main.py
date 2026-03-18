import dash
from dash import Dash, dcc, html, Input, Output, State, ctx, no_update
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import numpy as np

# ==========================================
# 0. FUNÇÃO MATEMÁTICA COMPARTILHADA
# ==========================================
def rotate_points(pts, start, end, angle):
    if np.allclose(start, end) or angle == 0:
        return pts
    axis = (end - start) / np.linalg.norm(end - start)
    K = np.array([[0, -axis[2], axis[1]], [axis[2], 0, -axis[0]], [-axis[1], axis[0], 0]])
    R_mat = np.eye(3) + np.sin(angle) * K + (1 - np.cos(angle)) * (K @ K)
    return (pts - start) @ R_mat.T + start

# ==========================================
# 1. GEOMETRIA BASE DO TETRAEDRO (_tet)
# ==========================================
sqrt = np.sqrt
a_tet = 1.0 
v0_tet = np.array([0, 0, 0])
v1_tet = np.array([-a_tet, 0, 0])
v2_tet = np.array([-a_tet/2, -a_tet * sqrt(3)/2, 0])
centroid_base_tet = (v0_tet + v1_tet + v2_tet) / 3
v3_tet = centroid_base_tet + np.array([0, 0, a_tet * sqrt(6)/3])

vertices_init_tet = np.array([v0_tet, v1_tet, v2_tet, v3_tet])
labels_fixo_tet = ['2', '3', '4', '1']
labels_movel_tet = ["2'", "3'", "4'", "1'"]

def get_pontos_tet(v):
    return {
        'Vértice 1': v[3], 'Vértice 2': v[0], 'Vértice 3': v[1], 'Vértice 4': v[2],
        'Ponto Médio M(1,2)': (v[3] + v[0]) / 2, 'Ponto Médio M(3,4)': (v[1] + v[2]) / 2,
        'Ponto Médio M(1,3)': (v[3] + v[1]) / 2, 'Ponto Médio M(2,4)': (v[0] + v[2]) / 2,
        'Ponto Médio M(1,4)': (v[3] + v[2]) / 2, 'Ponto Médio M(2,3)': (v[0] + v[1]) / 2,
        'Centro C(2,3,4)': (v[0] + v[1] + v[2]) / 3,
        'Centro C(1,2,3)': (v[3] + v[0] + v[1]) / 3,
        'Centro C(1,3,4)': (v[3] + v[1] + v[2]) / 3,
        'Centro C(1,2,4)': (v[3] + v[0] + v[2]) / 3
    }
opcoes_dropdown_tet = [{'label': k, 'value': k} for k in get_pontos_tet(vertices_init_tet).keys()]

# ==========================================
# 2. GEOMETRIA BASE DO CUBO (_cub)
# ==========================================
a_cub = 1.0  
vertices_init_cub = np.array([
    [-a_cub/2, -a_cub/2, -a_cub/2], [ a_cub/2, -a_cub/2, -a_cub/2], 
    [ a_cub/2,  a_cub/2, -a_cub/2], [-a_cub/2,  a_cub/2, -a_cub/2],
    [-a_cub/2, -a_cub/2,  a_cub/2], [ a_cub/2, -a_cub/2,  a_cub/2], 
    [ a_cub/2,  a_cub/2,  a_cub/2], [-a_cub/2,  a_cub/2,  a_cub/2]
])

labels_fixo_cub = ["2'", "3'", "4'", "1'", "4", "1", "2", "3"]
labels_movel_cub = [l + "*" for l in labels_fixo_cub] 
solid_edges_idx_cub = [(5, 6), (6, 7), (7, 4), (4, 5), (5, 1), (7, 3), (4, 0), (3, 0), (0, 1)]
dotted_edges_idx_cub = [(1, 2), (2, 3), (6, 2)]

faces_cub = [[0,1,2,3], [0,1,5,4], [1,2,6,5], [2,3,7,6], [0,3,7,4], [4,5,6,7]]
i_f_cub, j_f_cub, k_f_cub = [], [], []
for f in faces_cub:
    i_f_cub.extend([f[0], f[0]]); j_f_cub.extend([f[1], f[2]]); k_f_cub.extend([f[2], f[3]])
faces_dict_cub = dict(i=i_f_cub, j=j_f_cub, k=k_f_cub)

def get_pontos_cub(v):
    return {
        'Centro do Cubo': np.mean(v, axis=0),
        'Centro Face (1,2,3,4)': np.mean(v[[4,5,6,7]], axis=0),
        'Centro Face (1\',2\',3\',4\')': np.mean(v[[0,1,2,3]], axis=0),
        'Centro Face (1,4,2\',3\')': np.mean(v[[0,1,5,4]], axis=0),
        'Centro Face (2,3,1\',4\')': np.mean(v[[2,3,7,6]], axis=0),
        'Centro Face (1,2,3\',4\')': np.mean(v[[1,2,6,5]], axis=0),
        'Centro Face (3,4,1\',2\')': np.mean(v[[0,3,7,4]], axis=0),
        "Vértice 1": v[5], "Vértice 2": v[6], "Vértice 3": v[7], "Vértice 4": v[4],
        "Vértice 1'": v[3], "Vértice 2'": v[0], "Vértice 3'": v[1], "Vértice 4'": v[2],
        "Ponto Médio M(1, 2)": (v[5] + v[6]) / 2, "Ponto Médio M(2, 3)": (v[6] + v[7]) / 2,
        "Ponto Médio M(3, 4)": (v[7] + v[4]) / 2, "Ponto Médio M(4, 1)": (v[4] + v[5]) / 2,
        "Ponto Médio M(1', 2')": (v[3] + v[0]) / 2, "Ponto Médio M(2', 3')": (v[0] + v[1]) / 2,
        "Ponto Médio M(3', 4')": (v[1] + v[2]) / 2, "Ponto Médio M(4', 1')": (v[2] + v[3]) / 2,
        "Ponto Médio M(1, 3')": (v[5] + v[1]) / 2, "Ponto Médio M(2, 4')": (v[6] + v[2]) / 2,
        "Ponto Médio M(3, 1')": (v[7] + v[3]) / 2, "Ponto Médio M(4, 2')": (v[4] + v[0]) / 2,
    }
opcoes_dropdown_cub = [{'label': k, 'value': k} for k in get_pontos_cub(vertices_init_cub).keys()]

# ==========================================
# 3. INICIALIZAÇÃO DO APP
# ==========================================
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY], suppress_callback_exceptions=True)
server = app.server

# Estilos
SIDEBAR_STYLE = {
    "position": "fixed", "top": 0, "left": 0, "bottom": 0,
    "width": "18rem", "padding": "2rem 1rem", "background-color": "#2c3e50", "color": "white"
}

CONTENT_STYLE = {
    "margin-left": "20rem", "margin-right": "2rem", "padding": "2rem 1rem"
}

# ==========================================
# 4. MENU LATERAL E ROTEAMENTO
# ==========================================
sidebar = html.Div([
    html.H4("Simetrias dos Sólidos de Platão", className="display-6", style={'color': 'white'}),
    html.Hr(style={'borderColor': 'white'}),
    # html.P("Grupos e Sólidos Platônicos", className="lead", style={'fontSize': '14px'}),
    dbc.Nav([
        dbc.NavLink("Fundamentos e Teoremas", href="/", active="exact", style={'color': '#e0e2e2'}),
        dbc.NavLink("O Tetraedro (A4)", href="/tetraedro", active="exact", style={'color': '#e0e2e2'}),
        dbc.NavLink("Cubo e Octaedro (S4)", href="/cubo", active="exact", style={'color': '#e0e2e2'}),
       # dbc.NavLink("Dodecaedro e Icosaedro", href="/dodecaedro", active="exact", style={'color': '#e0e2e2'}),
    ], vertical=True, pills=True),
], style=SIDEBAR_STYLE)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

# ==========================================
# 5. CONSTRUÇÃO DAS PÁGINAS
# ==========================================

# --- Página Inicial (Textos Teóricos) ---
# Tenta ler o arquivo cap2.md se existir, ou pode criar a página da forma que preferir
try:
    with open('cap2.md', 'r', encoding='utf-8') as arquivo:
        texto_home = arquivo.read()
except FileNotFoundError:
        texto_home = "Texto do Capítulo 2 será lido aqui (Crie o arquivo cap2.md)."

pagina_home = html.Div([
    html.H1("Classes de grupos e exemplos notáveis", className="text-primary"),
    html.Hr(),
    dcc.Markdown(texto_home, mathjax=True,dangerously_allow_html=True,  style={'fontSize': '18px', 'lineHeight': '1.8'})
])


# --- Página do Tetraedro (Visual + App) ---
pagina_tetraedro = html.Div([
    html.H1("Simetrias do Tetraedro", className="text-primary"),
    html.Hr(),
    dcc.Store(id='memory-state-tet', data={'vertices': vertices_init_tet.tolist(), 'p1': 'Vértice 1', 'p2': 'Centro C(2,3,4)'}),
    html.Div(style={'display': 'flex', 'height': '75vh'}, children=[
        html.Div(style={'width': '30%', 'padding': '20px', 'border-right': '1px solid #ccc', 'background-color': '#f9f9f9', 'border-radius': '10px'}, children=[
            html.H4("Controles do Sólido"),
            html.P("Mova o sólido com o botão esquerdo do mouse", style={'color': 'gray', 'font-size': '14px'}),
            html.Label("Eixo de Rotação (Ponto 1):"),
            dcc.Dropdown(id='dropdown-p1-tet', options=opcoes_dropdown_tet, value='Vértice 1', clearable=False, style={'margin-bottom': '20px'}),
            html.Label("Eixo de Rotação (Ponto 2):"),
            dcc.Dropdown(id='dropdown-p2-tet', options=opcoes_dropdown_tet, value='Centro C(2,3,4)', clearable=False, style={'margin-bottom': '20px'}),
            html.Label("Ângulo de Rotação Atual (α):"),
            dcc.Slider(id='slider-angulo-tet', min=0, max=360, step=1, value=0, marks={0: '0°', 90: '90°', 120: '120°', 180: '180°', 240: '240°', 360: '360°'}, tooltip={"placement": "bottom", "always_visible": True}, updatemode='drag'),
            html.Button('Resetar Posição Original', id='btn-reset-tet', n_clicks=0, className="btn btn-secondary", style={'margin-top': '40px', 'width': '100%'})
        ]),
        html.Div(style={'width': '70%'}, children=[dcc.Graph(id='grafico-tetraedro', style={'height': '100%'}, config={'displayModeBar': False})])
    ])
])


# --- Página do Cubo (Visual + App) ---
pagina_cubo = html.Div([
    html.H1("Simetrias do Cubo e Octaedro", className="text-primary"),
    html.Hr(),
    dcc.Store(id='memory-state-cub', data={'vertices': vertices_init_cub.tolist(), 'p1': 'Centro Face (1,2,3,4)', 'p2': 'Centro Face (1\',2\',3\',4\')'}),
    html.Div(style={'display': 'flex', 'height': '75vh'}, children=[
        html.Div(style={'width': '30%', 'padding': '20px', 'border-right': '1px solid #ccc', 'background-color': '#f9f9f9', 'border-radius': '10px'}, children=[
            html.H4("Controles do Sólido"),
            html.P("Mova o sólido com o botão esquerdo do mouse", style={'color': 'gray', 'font-size': '14px'}),
            html.Label("Eixo de Rotação (Ponto 1):"),
            dcc.Dropdown(id='dropdown-p1-cub', options=opcoes_dropdown_cub, value='Centro Face (1,2,3,4)', clearable=False, style={'margin-bottom': '20px'}),
            html.Label("Eixo de Rotação (Ponto 2):"),
            dcc.Dropdown(id='dropdown-p2-cub', options=opcoes_dropdown_cub, value='Centro Face (1\',2\',3\',4\')', clearable=False, style={'margin-bottom': '20px'}),
            html.Label("Ângulo de Rotação Atual (α):"),
            dcc.Slider(id='slider-angulo-cub', min=0, max=360, step=1, value=0, marks={0: '0°', 90: '90°', 120: '120°', 180: '180°', 270: '270°', 360: '360°'}, tooltip={"placement": "bottom", "always_visible": True}, updatemode='drag'),
            html.Button('Resetar Posição Original', id='btn-reset-cub', n_clicks=0, className="btn btn-secondary", style={'margin-top': '40px', 'width': '100%'})
        ]),
        html.Div(style={'width': '70%'}, children=[dcc.Graph(id='grafico-cubo', style={'height': '100%'}, config={'displayModeBar': False})])
    ])
])

# Para o Dodecaedro, enquanto não unimos o código, mantemos em branco (podemos fazer igual ao cubo depois!)
pagina_dodecaedro = html.Div([html.H1("Dodecaedro e Icosaedro", className="text-primary"), html.Hr(), html.H3("Página em Construção...")])


# ==========================================
# 6. ROTEAMENTO ENTRE PÁGINAS
# ==========================================
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    # Alterado para ir para a home na raiz do site
    if pathname == "/": return pagina_home
    elif pathname == "/tetraedro": return pagina_tetraedro
    elif pathname == "/cubo": return pagina_cubo
    elif pathname == "/dodecaedro": return pagina_dodecaedro
    return html.Div([html.H1("404: Página não encontrada", className="text-danger")])


# ==========================================
# 7. CALLBACKS (Cálculos de Rotação e Renderização 3D)
# ==========================================
@app.callback(
    [Output('grafico-tetraedro', 'figure'), Output('memory-state-tet', 'data'), Output('slider-angulo-tet', 'value')],
    [Input('dropdown-p1-tet', 'value'), Input('dropdown-p2-tet', 'value'), Input('slider-angulo-tet', 'value'), Input('btn-reset-tet', 'n_clicks')],
    [State('memory-state-tet', 'data')]
)
def update_tetraedro(p1_name, p2_name, angulo_graus, btn_reset, memory):
    trigger = ctx.triggered_id
    stored_vertices = np.array(memory['vertices'])
    
    if trigger == 'btn-reset-tet':
        current_vertices = vertices_init_tet
        new_memory = {'vertices': vertices_init_tet.tolist(), 'p1': p1_name, 'p2': p2_name}
        new_slider_val = 0; angulo_rad_current = 0.0
    elif trigger in ['dropdown-p1-tet', 'dropdown-p2-tet']:
        old_pontos = get_pontos_tet(stored_vertices)
        baked_vertices = rotate_points(stored_vertices, old_pontos[memory['p1']], old_pontos[memory['p2']], np.radians(angulo_graus))
        new_memory = {'vertices': baked_vertices.tolist(), 'p1': p1_name, 'p2': p2_name}
        current_vertices = baked_vertices
        new_slider_val = 0; angulo_rad_current = 0.0
    else:
        current_vertices = stored_vertices
        new_memory = no_update; new_slider_val = no_update
        angulo_rad_current = np.radians(angulo_graus)
        
    curr_pontos = get_pontos_tet(current_vertices)
    start_curr, end_curr = curr_pontos[p1_name], curr_pontos[p2_name]
    pts_movel = rotate_points(current_vertices, start_curr, end_curr, angulo_rad_current)
    
    faces_idx = dict(i=[0,0,0,1], j=[1,2,3,2], k=[2,3,1,3])
    solid_edges = [(3, 0), (3, 1), (3, 2), (0, 2), (1, 2)]
    dotted_edges = [(0, 1)]
    fig = go.Figure()

    fig.add_trace(go.Mesh3d(x=vertices_init_tet[:,0], y=vertices_init_tet[:,1], z=vertices_init_tet[:,2], **faces_idx, color='lightgray', opacity=0.15, showlegend=False))
    for i1, i2 in solid_edges: fig.add_trace(go.Scatter3d(x=[vertices_init_tet[i1,0], vertices_init_tet[i2,0]], y=[vertices_init_tet[i1,1], vertices_init_tet[i2,1]], z=[vertices_init_tet[i1,2], vertices_init_tet[i2,2]], mode='lines', line=dict(color='gray', width=2), showlegend=False))
    for i1, i2 in dotted_edges: fig.add_trace(go.Scatter3d(x=[vertices_init_tet[i1,0], vertices_init_tet[i2,0]], y=[vertices_init_tet[i1,1], vertices_init_tet[i2,1]], z=[vertices_init_tet[i1,2], vertices_init_tet[i2,2]], mode='lines', line=dict(color='gray', width=2, dash='dot'), showlegend=False))
    fig.add_trace(go.Scatter3d(x=vertices_init_tet[:,0]+0.03, y=vertices_init_tet[:,1], z=vertices_init_tet[:,2], mode='text', text=labels_fixo_tet, textfont=dict(color='gray', size=12), marker=dict(size=4, color='gray'), showlegend=False))

    fig.add_trace(go.Mesh3d(x=pts_movel[:,0], y=pts_movel[:,1], z=pts_movel[:,2], **faces_idx, color='firebrick', opacity=0.4, showlegend=False))
    for i1, i2 in solid_edges: fig.add_trace(go.Scatter3d(x=[pts_movel[i1,0], pts_movel[i2,0]], y=[pts_movel[i1,1], pts_movel[i2,1]], z=[pts_movel[i1,2], pts_movel[i2,2]], mode='lines', line=dict(color='black', width=3), showlegend=False))
    for i1, i2 in dotted_edges: fig.add_trace(go.Scatter3d(x=[pts_movel[i1,0], pts_movel[i2,0]], y=[pts_movel[i1,1], pts_movel[i2,1]], z=[pts_movel[i1,2], pts_movel[i2,2]], mode='lines', line=dict(color='black', width=3, dash='dot'), showlegend=False))
    fig.add_trace(go.Scatter3d(x=pts_movel[:,0]-0.05, y=pts_movel[:,1], z=pts_movel[:,2], mode='text', text=labels_movel_tet, textfont=dict(color='black', size=16), marker=dict(size=6, color='black'), showlegend=False))


    if not np.allclose(start_curr, end_curr):
        vec = (end_curr - start_curr) / np.linalg.norm(end_curr - start_curr)
        fig.add_trace(go.Scatter3d(x=[start_curr[0]-vec[0]*0.8, end_curr[0]+vec[0]*0.8], y=[start_curr[1]-vec[1]*0.8, end_curr[1]+vec[1]*0.8], z=[start_curr[2]-vec[2]*0.8, end_curr[2]+vec[2]*0.8], mode='lines', line=dict(color='black', width=4, dash='solid'), showlegend=False))
        fig.add_trace(go.Scatter3d(x=[start_curr[0], end_curr[0]], y=[start_curr[1], end_curr[1]], z=[start_curr[2], end_curr[2]], mode='markers', marker=dict(size=5, color='gold'), showlegend=False))

    fig.update_layout(uirevision='tet', scene=dict(xaxis=dict(visible=False), yaxis=dict(visible=False), zaxis=dict(visible=False), aspectmode='data', camera_eye=dict(x=1.5, y=-2.7, z=0.8)), margin=dict(l=0, r=0, b=0, t=0), plot_bgcolor='white', paper_bgcolor='white')
    return fig, new_memory, new_slider_val

@app.callback(
    [Output('grafico-cubo', 'figure'), Output('memory-state-cub', 'data'), Output('slider-angulo-cub', 'value')],
    [Input('dropdown-p1-cub', 'value'), Input('dropdown-p2-cub', 'value'), Input('slider-angulo-cub', 'value'), Input('btn-reset-cub', 'n_clicks')],
    [State('memory-state-cub', 'data')]
)
def update_cubo(p1_name, p2_name, angulo_graus, btn_reset, memory):
    trigger = ctx.triggered_id
    stored_vertices = np.array(memory['vertices'])
    
    if trigger == 'btn-reset-cub':
        current_vertices = vertices_init_cub
        new_memory = {'vertices': vertices_init_cub.tolist(), 'p1': p1_name, 'p2': p2_name}
        new_slider_val = 0; angulo_rad_current = 0.0
    elif trigger in ['dropdown-p1-cub', 'dropdown-p2-cub']:
        old_pontos = get_pontos_cub(stored_vertices)
        baked_vertices = rotate_points(stored_vertices, old_pontos[memory['p1']], old_pontos[memory['p2']], np.radians(angulo_graus))
        new_memory = {'vertices': baked_vertices.tolist(), 'p1': p1_name, 'p2': p2_name}
        current_vertices = baked_vertices
        new_slider_val = 0; angulo_rad_current = 0.0
    else:
        current_vertices = stored_vertices
        new_memory = no_update; new_slider_val = no_update
        angulo_rad_current = np.radians(angulo_graus)
        
    curr_pontos = get_pontos_cub(current_vertices)
    start_curr, end_curr = curr_pontos[p1_name], curr_pontos[p2_name]
    pts_movel = rotate_points(current_vertices, start_curr, end_curr, angulo_rad_current)
    
    fig = go.Figure()

    fig.add_trace(go.Mesh3d(x=vertices_init_cub[:,0], y=vertices_init_cub[:,1], z=vertices_init_cub[:,2], **faces_dict_cub, color='lightgray', opacity=0.1, showlegend=False))
    for i1, i2 in solid_edges_idx_cub: fig.add_trace(go.Scatter3d(x=[vertices_init_cub[i1,0], vertices_init_cub[i2,0]], y=[vertices_init_cub[i1,1], vertices_init_cub[i2,1]], z=[vertices_init_cub[i1,2], vertices_init_cub[i2,2]], mode='lines', line=dict(color='gray', width=2), showlegend=False))
    for i1, i2 in dotted_edges_idx_cub: fig.add_trace(go.Scatter3d(x=[vertices_init_cub[i1,0], vertices_init_cub[i2,0]], y=[vertices_init_cub[i1,1], vertices_init_cub[i2,1]], z=[vertices_init_cub[i1,2], vertices_init_cub[i2,2]], mode='lines', line=dict(color='gray', width=2, dash='dot'), showlegend=False))
    fig.add_trace(go.Scatter3d(x=vertices_init_cub[:,0]+0.15, y=vertices_init_cub[:,1], z=vertices_init_cub[:,2]-0.25, mode='text', text=labels_fixo_cub, textfont=dict(color='gray', size=12), showlegend=False))

    fig.add_trace(go.Mesh3d(x=pts_movel[:,0], y=pts_movel[:,1], z=pts_movel[:,2], **faces_dict_cub, color='firebrick', opacity=0.3, showlegend=False))
    for i1, i2 in solid_edges_idx_cub: fig.add_trace(go.Scatter3d(x=[pts_movel[i1,0], pts_movel[i2,0]], y=[pts_movel[i1,1], pts_movel[i2,1]], z=[pts_movel[i1,2], pts_movel[i2,2]], mode='lines', line=dict(color='black', width=4), showlegend=False))
    for i1, i2 in dotted_edges_idx_cub: fig.add_trace(go.Scatter3d(x=[pts_movel[i1,0], pts_movel[i2,0]], y=[pts_movel[i1,1], pts_movel[i2,1]], z=[pts_movel[i1,2], pts_movel[i2,2]], mode='lines', line=dict(color='black', width=3, dash='dot'), showlegend=False))
    fig.add_trace(go.Scatter3d(x=pts_movel[:,0], y=pts_movel[:,1], z=pts_movel[:,2], mode='text', text=labels_movel_cub, textfont=dict(color='black', size=16), showlegend=False))

    if not np.allclose(start_curr, end_curr):
        vec = (end_curr - start_curr) / np.linalg.norm(end_curr - start_curr)
        fig.add_trace(go.Scatter3d(x=[start_curr[0]-vec[0]*1.0, end_curr[0]+vec[0]*1.0], y=[start_curr[1]-vec[1]*1.0, end_curr[1]+vec[1]*1.0], z=[start_curr[2]-vec[2]*1.0, end_curr[2]+vec[2]*1.0], mode='lines', line=dict(color='black', width=4, dash='solid'), showlegend=False))
        fig.add_trace(go.Scatter3d(x=[start_curr[0], end_curr[0]], y=[start_curr[1], end_curr[1]], z=[start_curr[2], end_curr[2]], mode='markers', marker=dict(size=5, color='gold'), showlegend=False))

    fig.update_layout(uirevision='cub', scene=dict(xaxis=dict(visible=False), yaxis=dict(visible=False), zaxis=dict(visible=False), aspectmode='data', camera_eye=dict(x=-2.8, y=-1.8, z=1.2)), margin=dict(l=0, r=0, b=0, t=0), plot_bgcolor='white', paper_bgcolor='white')
    return fig, new_memory, new_slider_val

# if __name__ == "__main__":
#     app.run(debug=True, port=8060)
