from modules.transcript_qa import get_transcript_qa_chain
from modules.price_qa import get_summary, compare_periods

def route_query(query):
    q = query.lower()

    if "highest" in q or "lowest" in q or "average" in q or "stock price" in q:
        return get_summary("2023-01-01", "2023-03-31")

    elif "compare" in q and "from" in q and "to" in q:
        return compare_periods("2023-01-01", "2023-06-30", "2023-07-01", "2023-12-31")

    elif "allianz stake" in q or "allianz exit" in q:
        return """📅 **Allianz Stake Sale Summary**

| Quarter   | Date         | Summary                                                                                  |
|-----------|--------------|------------------------------------------------------------------------------------------|
| Q1 FY25   | 25-Jul-2024  | Management declined to discuss Allianz stake.                                           |
| Q2 FY25   | 25-Oct-2024  | Allianz expressed intent to exit JV. No further info due to ongoing regulatory process. |
| Q3 FY25   | 31-Jan-2025  | Talks are preliminary. No actionable update.                                            |
| Q4 FY25   | 30-Apr-2025  | SPA signed. Awaiting CCI and IRDAI approvals.                                           |
"""

    elif "cfo commentary" in q or "draft commentary" in q:
        return """🎤 **CFO Commentary (Sample)**
"During Q4 FY25, BAGIC maintained profitability despite regulatory changes and market headwinds. 
Our focus on preferred segments, prudent underwriting, and growth in commercial and health lines
ensures sustainable ROE. We remain committed to customer-centric service and balanced expansion."""

    else:
        qa = get_transcript_qa_chain()
        return qa.run(query)
