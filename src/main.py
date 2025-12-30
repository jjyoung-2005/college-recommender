
# %%
import pandas as pd

from pathlib import Path
import pandas as pd

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "colleges.csv"

def ask_region() -> str:
    valid = {"Northeast", "Midwest", "South", "West"}
    print("Regions:", ", ".join(sorted(valid)))
    region = input("Enter preferred region (Type exactly one): ").strip()
    while region not in valid:
        region = input("Please enter a valid region: ").strip()
    return region

def main():
    colleges = pd.read_csv(DATA_PATH)
    region = ask_region()
    filtered_region = colleges[colleges["region"] == region].copy()
    print(f"\nColleges in the {region} region:")
    print(filtered_region[["name", "region", "setting", "size", "net_price"]].head(10))

if __name__ == "__main__":
    main()



# %%
