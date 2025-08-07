import matplotlib.pyplot as plt
import pandas as pd

def analyze_sales_by_date(df):
    """
    Rysuje wykres trendu sprzedaży według daty.
    Zakłada, że kolumny to: 'Date' i 'Sales'.
    """
    # Upewnij się, że kolumna 'Date' jest w formacie daty
    df['Date'] = pd.to_datetime(df['Date'])

    # Grupuj dane po dacie i sumuj sprzedaż
    daily_sales = df.groupby('Date')['Sales'].sum()

    # Rysuj wykres
    plt.figure(figsize=(10, 5))
    daily_sales.plot()
    plt.title("Trendy sprzedaży")
    plt.xlabel("Data")
    plt.ylabel("Suma sprzedaży")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
