import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page configuration
st.set_page_config(
    page_title="Healthcare Insurance Cost Analysis",
    page_icon="🏥",
    layout="wide"
)

# Dashboard title
st.title("Healthcare Insurance Cost Analysis")
st.write(
    "Explore recorded healthcare insurance charges "
    "by smoking status, age, BMI and region."
)

# Load the cleaned dataset


@st.cache_data
def load_data():
    return pd.read_csv("data/insurance_cleaned.csv")


df = load_data()

# Dataset overview
st.header("Dataset Overview")
col1, col2, col3 = st.columns(3)

col1.metric("Number of Records", f"{len(df):,}")
col2.metric("Number of Columns", f"{len(df.columns)}")
col3.metric("Mean Recorded Charges", f"{df['charges'].mean():,.2f}")

st.write("Preview of the cleaned dataset")
st.dataframe(df.head(10), use_container_width=True)

# Sidebar filters
st.sidebar.header("Filter the Data")

selected_region = st.sidebar.multiselect(
    "Select region",
    options=sorted(df["region"].unique()),
    default=sorted(df["region"].unique())
)

selected_smoker = st.sidebar.multiselect(
    "Smoking status",
    options=sorted(df["smoker"].unique()),
    default=sorted(df["smoker"].unique())
)

filtered_df = df[
    df["region"].isin(selected_region)
    & df["smoker"].isin(selected_smoker)
]

# Filtered dataset summary
st.header("Explore Recorded Charges")
st.write(f"Records matching your filters: **{len(filtered_df):,}**")

if filtered_df.empty:
    st.warning("No records match your selected filters.")
else:
    # Charges by smoking status
    st.subheader("Recorded Charges by Smoking Status")
    fig1, ax1 = plt.subplots(figsize=(8, 5))
    sns.boxplot(data=filtered_df, x="smoker", y="charges", ax=ax1)
    ax1.set_xlabel("Smoker")
    ax1.set_ylabel("Recorded Charges")
    st.pyplot(fig1)
    plt.close(fig1)

    # Mean charges by region
    st.subheader("Mean Recorded Charges by Region")
    region_summary = (
        filtered_df.groupby("region", as_index=False)["charges"]
        .mean()
    )
    fig2, ax2 = plt.subplots(figsize=(8, 5))
    sns.barplot(
        data=region_summary,
        x="region",
        y="charges",
        ax=ax2
    )
    ax2.set_xlabel("Region")
    ax2.set_ylabel("Mean Recorded Charges")
    st.pyplot(fig2)
    plt.close(fig2)

    # Age and charges
    st.subheader("Age and Recorded Charges")
    fig3, ax3 = plt.subplots(figsize=(8, 5))
    sns.scatterplot(
        data=filtered_df,
        x="age",
        y="charges",
        alpha=0.5,
        s=25,
        ax=ax3
    )
    ax3.set_xlabel("Age")
    ax3.set_ylabel("Recorded Charges")
    st.pyplot(fig3)
    plt.close(fig3)

    # BMI and charges
    st.subheader("BMI and Recorded Charges")
    fig4, ax4 = plt.subplots(figsize=(8, 5))
    sns.scatterplot(
        data=filtered_df,
        x="bmi",
        y="charges",
        alpha=0.5,
        s=25,
        ax=ax4
    )
    ax4.set_xlabel("BMI")
    ax4.set_ylabel("Recorded Charges")
    st.pyplot(fig4)
    plt.close(fig4)

st.caption(
    "This dashboard describes patterns in the dataset. "
    "Associations do not establish causation."
)
