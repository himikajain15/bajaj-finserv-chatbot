import pandas as pd
from datetime import datetime

df = pd.read_csv("data/BFS_Share_Price.csv")
df['Date'] = pd.to_datetime(df['Date'], format='%d-%b-%y')

def get_summary(start_date, end_date):
    mask = (df['Date'] >= pd.to_datetime(start_date)) & (df['Date'] <= pd.to_datetime(end_date))
    filtered = df[mask]
    if filtered.empty:
        return "No data found for the given period."

    high = filtered['Close Price'].max()
    low = filtered['Close Price'].min()
    avg = filtered['Close Price'].mean()

    return f"""📊 **Stock Summary ({start_date} to {end_date})**
- Highest Price: ₹{high:.2f}
- Lowest Price: ₹{low:.2f}
- Average Price: ₹{avg:.2f}"""

def compare_periods(p1_start, p1_end, p2_start, p2_end):
    def summarize(start, end):
        mask = (df['Date'] >= pd.to_datetime(start)) & (df['Date'] <= pd.to_datetime(end))
        data = df.loc[mask]
        return {
            "period": f"{start} to {end}",
            "high": data["Close Price"].max(),
            "low": data["Close Price"].min(),
            "avg": data["Close Price"].mean()
        } if not data.empty else None

    p1 = summarize(p1_start, p1_end)
    p2 = summarize(p2_start, p2_end)

    if not p1 or not p2:
        return "Not enough data to compare these periods."

    return f"""📊 **Comparison**
| Period | High | Low | Average |
|--------|------|-----|---------|
| {p1['period']} | ₹{p1['high']:.2f} | ₹{p1['low']:.2f} | ₹{p1['avg']:.2f} |
| {p2['period']} | ₹{p2['high']:.2f} | ₹{p2['low']:.2f} | ₹{p2['avg']:.2f} |
"""
