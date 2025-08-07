import pandas as pd


def load_data(filepath):
    """
    Wczytuje dane z pliku CSV.

    :param filepath: Ścieżka do pliku CSV
    :return: DataFrame z danymi
    """
    try:
        df = pd.read_csv(filepath)
        print(f"Wczytano dane: {df.shape[0]} wierszy, {df.shape[1]} kolumn")
        return df
    except Exception as e:
        print("Błąd podczas wczytywania danych:", e)
        return None