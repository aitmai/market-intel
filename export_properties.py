"""
Export mock properties to Google Sheets
"""
from data.mock_properties import get_sample_properties, get_market_data
from sheets_writer import get_sheet

def export_properties_to_sheet():
    sheet = get_sheet("Property-To-Evaluate")
    sheet.clear()

    # Headers
    headers = [
        "Property ID", "Address", "City", "State", "Price",
        "Bedrooms", "Bathrooms", "Sqft", "Year Built", "Property Type",
        "Est. Rent", "HOA Fees", "Property Tax", "Insurance",
        "Appreciation Rate", "Market Heat", "Competition", 
        "Neighborhood Rating", "School Rating", "Crime Index", "Avg $/Sqft"
    ]

    rows = [headers]

    properties = get_sample_properties()

    for prop in properties:
        market = get_market_data(prop.city)
        rows.append([
            prop.property_id,
            prop.address,
            prop.city,
            prop.state,
            prop.price,
            prop.bedrooms,
            prop.bathrooms,
            prop.sqft,
            prop.year_built,
            prop.property_type,
            prop.estimated_rent,
            prop.hoa_fees,
            prop.property_tax_annual,
            prop.insurance_annual,
            market["appreciation_rate"],
            market["market_heat"],
            market["competition_level"],
            market["neighborhood_rating"],
            market["school_rating"],
            market["crime_index"],
            market["avg_price_per_sqft"]
        ])

    sheet.update(rows, "A1")
    print(f"Exported {len(properties)} properties to Google Sheets")

if __name__ == "__main__":
    export_properties_to_sheet()