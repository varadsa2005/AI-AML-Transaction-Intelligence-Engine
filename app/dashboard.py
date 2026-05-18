import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="AI AML Engine",
    page_icon="🚨",
    layout="wide"
)

transactions_df = pd.read_csv(
    "data/raw/transactions.csv"
)

# ======================
# KPI CALCULATIONS
# ======================

total_transactions = len(transactions_df)

total_volume = transactions_df["amount"].sum()

suspicious_count = len(
    transactions_df[
        transactions_df["is_suspicious"] == True
    ]
)

avg_transaction = round(
    transactions_df["amount"].mean(),
    2
)

# ======================
# CUSTOM STYLING
# ======================

st.markdown(
    """
    <style>

    .main {
        background-color: #0E1117;
    }

    .block-container {
        padding-top: 2rem;
    }

    div[data-testid="metric-container"] {
        background-color: #1E1E1E;
        border: 1px solid #333333;
        padding: 15px;
        border-radius: 12px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ======================
# SIDEBAR
# ======================

st.sidebar.title("🚨 AML Monitoring System")

st.sidebar.markdown("---")

st.sidebar.info(
    """
    AI Powered Financial Crime Detection System

    Modules:
    - AML Rules
    - Anomaly Detection
    - Risk Scoring
    - Network Analysis
    """
)

# ======================
# HEADER
# ======================

st.title("🚨 AI AML & Transaction Intelligence Engine")

st.caption(
    "Enterprise Financial Crime Monitoring Dashboard"
)

st.markdown("---")

# ======================
# KPI CARDS
# ======================

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Transactions",
    f"{total_transactions:,}"
)

col2.metric(
    "Transaction Volume",
    f"${total_volume:,.0f}"
)

col3.metric(
    "Suspicious Alerts",
    suspicious_count
)

col4.metric(
    "Average Amount",
    f"${avg_transaction:,.0f}"
)

st.markdown("---")

# ======================
# CHARTS
# ======================

left_col, right_col = st.columns(2)

with left_col:

    st.subheader("Transaction Type Distribution")

    fig1 = px.pie(
        transactions_df,
        names="transaction_type",
        hole=0.5
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

with right_col:

    st.subheader("Suspicious Transactions")

    suspicious_chart = transactions_df[
        "is_suspicious"
    ].value_counts()

    fig2 = px.bar(
        x=suspicious_chart.index.astype(str),
        y=suspicious_chart.values,
        labels={
            "x": "Suspicious",
            "y": "Count"
        }
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

# ======================
# HIGH RISK TRANSACTIONS
# ======================

st.subheader("🚨 High Risk Transactions")

high_risk = transactions_df[
    transactions_df["amount"] > 200000
]

st.dataframe(
    high_risk.head(20),
    use_container_width=True
)

# ======================
# RECENT TRANSACTIONS
# ======================

st.subheader("Recent Transactions")

st.dataframe(
    transactions_df.head(20),
    use_container_width=True
)