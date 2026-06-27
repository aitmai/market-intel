import gspread
from google.oauth2.service_account import Credentials

def get_sheet(sheet_name):
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]
    creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
    client = gspread.authorize(creds)
    return client.open(sheet_name).sheet1

def write_all_results(sheet, results):
    sheet.clear()
    headers = [
        "Property", "Purchase Price", "ARV", "Repair Cost",
        "Max Offer", "Cap Rate", "Monthly Cash Flow", "ROI 5yr", "Grade"
    ]
    rows = [headers]
    for r in results:
        rows.append([
            r["property"], r["purchase_price"], r["arv"], r["repair_cost"],
            r["max_offer"], r["cap_rate"], r["monthly_cash_flow"], r["roi_5yr"], r["grade"]
        ])
    sheet.update("A1", rows)
    print(f"Written {len(results)} properties to Google Sheets")
    