import pandas as pd

df = pd.read_csv("sales_data.csv", parse_dates=["order_date"])

# Basic validation
df = df.drop_duplicates(subset=["order_id"]).dropna()
df["revenue"] = pd.to_numeric(df["revenue"], errors="coerce")
df["profit"] = pd.to_numeric(df["profit"], errors="coerce")

summary = pd.DataFrame({
    "metric": [
        "order_count","total_units","total_revenue","total_cost",
        "total_profit","average_order_revenue","profit_margin_pct"
    ],
    "value": [
        len(df), df["units"].sum(), df["revenue"].sum(), df["cost"].sum(),
        df["profit"].sum(), df["revenue"].mean(),
        100 * df["profit"].sum() / df["revenue"].sum()
    ]
})
summary["value"] = summary["value"].round(2)
summary.to_csv("results/sales_summary.csv", index=False)

region = df.groupby("region", as_index=False).agg(
    orders=("order_id","count"),
    units=("units","sum"),
    revenue=("revenue","sum"),
    profit=("profit","sum")
)
region["profit_margin_pct"] = 100 * region["profit"] / region["revenue"]
region.round(2).to_csv("results/region_summary.csv", index=False)

category = df.groupby("category", as_index=False).agg(
    orders=("order_id","count"),
    units=("units","sum"),
    revenue=("revenue","sum"),
    profit=("profit","sum")
)
category["profit_margin_pct"] = 100 * category["profit"] / category["revenue"]
category.round(2).to_csv("results/category_summary.csv", index=False)

print("Sales analysis complete.")
print(summary.to_string(index=False))
print("\nRegional summary:")
print(region.round(2).to_string(index=False))
print("\nCategory summary:")
print(category.round(2).to_string(index=False))
