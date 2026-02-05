import plotly.graph_objects as go
import plotly.io as pio

def plot_sankey_base_vs_cenario(
    cenario_nome: str,
    valores_base: dict,
    valores_cenario: dict,
    output_path: str,
    tamanho_fonte: int = 15,
    largura: int = 1000,
    altura: int = 500,
    cor_centro: str = "#7F8C8D"
):
    """
    Sankey: Cenário Base -> Centro -> Cenário
    A ordem do cenário é a MESMA do cenário base (fixa e consistente).
    """

    # Ordem fixa (base e cenário)
    ordem = [
        "Derivados de Petróleo",
        "Biodiesel",
        "Etanol",
        "Eletricidade (GC)",
        "Eletricidade (GD)",
        "Gás Natural"
    ]

    # Paleta
    cores = {
        "Derivados de Petróleo": "#C0392B",
        "Biodiesel": "#F39C12",
        "Etanol": "#27AE60",
        "Eletricidade (GC)": "#F1C40F",
        "Eletricidade (GD)": "#F1C40F",
        "Gás Natural": "#2980B9",
        "CENTRO": cor_centro
    }

    # Labels
    labels = ordem + [""] + [f"{s} ({cenario_nome})" for s in ordem]

    # Valores para rótulos
    total_base = sum(valores_base.values())
    valores_nos = (
        [valores_base[s] for s in ordem] +
        [total_base] +
        [valores_cenario[s] for s in ordem]
    )

    label_final = [
        f"{l}: {v:,.2f}" if (l != "" and v > 0)
        else f"{l} - 0.00" if l != "" else ""
        for l, v in zip(labels, valores_nos)
    ]

    # Cores dos nós
    colors_nodes = (
        [cores[s] for s in ordem] +
        [cores["CENTRO"]] +
        [cores[s] for s in ordem]
    )

    # Links
    n = len(ordem)
    centro_idx = n

    source = list(range(n)) + [centro_idx] * n
    target = [centro_idx] * n + list(range(centro_idx + 1, centro_idx + 1 + n))
    values = [valores_base[s] for s in ordem] + [valores_cenario[s] for s in ordem]

    def hex_to_rgba(hex_color, alpha=0.6):
        hex_color = hex_color.lstrip("#")
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)
        return f"rgba({r},{g},{b},{alpha})"

    colors_links = (
        [hex_to_rgba(cores[s], 0.6) for s in ordem] +
        [hex_to_rgba(cores[s], 0.6) for s in ordem]
    )

    # Figura
    fig = go.Figure(data=[go.Sankey(
        node=dict(
            pad=35,
            thickness=15,
            line=dict(color="white", width=0),
            label=label_final,
            color=colors_nodes
        ),
        link=dict(
            source=source,
            target=target,
            value=values,
            color=colors_links
        )
    )])

    # Anotação central
    fig.add_annotation(
        x=0.5, y=0.5,
        xanchor="center", yanchor="bottom",
        text=f"<b>Cenário Base - {cenario_nome}</b><br>{total_base:,.2f}",
        showarrow=False,
        font=dict(family="Times New Roman", size=tamanho_fonte, color="black"),
        align="center",
        bgcolor="rgba(255,255,255,0.6)",
        borderpad=6
    )

    fig.update_layout(
        font=dict(family="Times New Roman", size=tamanho_fonte, color="black"),
        plot_bgcolor="white",
        paper_bgcolor="white",
        width=largura,
        height=altura,
        margin=dict(l=50, r=50, t=50, b=50)
    )

    pio.write_image(fig, output_path, engine="kaleido")
    fig.show()
