
# %%
import pandas as pd

from pathlib import Path
import pandas as pd

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "colleges.csv"

def ask_region() -> str:
    valid = {"Northeast", "Midwest", "South", "West"}
    print("Regions:", ", ".join(sorted(valid)))
    region = input("Preferred region (type one exactly): ").strip()
    while region not in valid:
        region = input("Please type exactly one of the listed regions: ").strip()
    return region

def ask_size() -> str:
    valid = {"small", "medium", "large"}
    print("Sizes:", ", ".join(sorted(valid)))
    size = input("Preferred size (type one exactly): ").strip()
    while size not in valid:
        size = input("Please type exactly one of the listed sizes: ").strip()
    return size

def ask_setting() -> str:
    valid = {"urban", "suburban", "rural"}
    print("Settings:", ", ".join(sorted(valid)))
    setting = input("Preferred setting (type one exactly): ").strip()
    while setting not in valid:
        setting = input("Please type exactly one of the listed settings: ").strip()
    return setting

def ask_net_price() -> float:
    while True:
        try:
            price = float(input("Maximum net price willing to pay (e.g., 20000): ").strip())
            if price < 0:
                print("Net price must be a non-negative number.")
                continue
            return price
        except ValueError:
            print("Please enter a valid number.")

def main():
    colleges = pd.read_csv(DATA_PATH)
    print(colleges.columns.tolist())

    region = ask_region()
    filtered = colleges[colleges["region"] == region]
    size = ask_size()
    filtered = filtered[filtered["size"] == size]
    setting = ask_setting()
    filtered = filtered[filtered["setting"] == setting]
    net_price = ask_net_price()
    filtered = filtered[filtered["net_price"] <= net_price]

    print("\nTop matches (filtered by region):")
    print(filtered[["name", "region", "setting", "size", "net_price"]].head(10))

if __name__ == "__main__":
    main()




# %%
