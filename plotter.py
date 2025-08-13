import matplotlib as plt

def plot_currency(df, currency_code="USD"):
    plt.plot(df["date"], df["rate"], marker="o")
    plt.title(f"Курс {currency_code}")
    plt.xlabel("Дата")
    plt.ylabel("Курс")
    plt.grid(True)
    plt.show()