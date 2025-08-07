from src.data_loader import load_data
from src.analysis import analyze_sales_by_date

# Podaj ścieżkę do swojego pliku CSV
csv_file = 'data/sales.csv'

# Wczytaj dane
df = load_data(csv_file)

# Przeanalizuj i narysuj wykres, jeśli dane wczytane poprawnie
if df is not None:
    analyze_sales_by_date(df)
