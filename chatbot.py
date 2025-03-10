# Import necessary libraries
import pandas as pd

# Load the financial data from the Excel file
file_path = 'Manual_Financial_Data.csv'
df = pd.read_csv(file_path)

# Sort by Fiscal Year in Ascending Order
df_sorted = df.sort_values(by=['Company', 'Fiscal Year'], ascending=[True, True])

# Function to get total revenue for a company
def get_total_revenue(company):
    data = df_sorted[df_sorted['Company'] == company]
    result = data[['Fiscal Year', 'Total Revenue']]
    return result.set_index('Fiscal Year').to_dict()['Total Revenue']

# Function to get net income change for a company
def get_net_income_change(company):
    data = df_sorted[df_sorted['Company'] == company]
    data['Net Income Change'] = data['Net Income'].pct_change() * 100
    result = data[['Fiscal Year', 'Net Income Change']].round(2)
    return result.set_index('Fiscal Year').to_dict()['Net Income Change']

# Function to get change metrics 

def get_revenue_change(company):
    data = df_sorted[df_sorted['Company'] == company]
    data['Revenue Change (%)'] = data['Total Revenue'].pct_change() * 100
    result = data[['Fiscal Year', 'Revenue Change (%)']].round(2)
    return result.set_index('Fiscal Year').to_dict()['Revenue Change (%)']

def get_asset_change(company):
    data = df_sorted[df_sorted['Company'] == company]
    data['Asset Change (%)'] = data['Total Assets'].pct_change() * 100
    result = data[['Fiscal Year', 'Asset Change (%)']].round(2)
    return result.set_index('Fiscal Year').to_dict()['Asset Change (%)']

def get_liabilities_change(company):
    data = df_sorted[df_sorted['Company'] == company]
    data['Liabilities Change (%)'] = data['Total Liabilities'].pct_change() * 100
    result = data[['Fiscal Year', 'Liabilities Change (%)']].round(2)
    return result.set_index('Fiscal Year').to_dict()['Liabilities Change (%)']

def get_cash_flow_change(company):
    data = df_sorted[df_sorted['Company'] == company]
    data['Cash Flow Change (%)'] = data['Cash Flow from Operating Activities'].pct_change() * 100
    result = data[['Fiscal Year', 'Cash Flow Change (%)']].round(2)
    return result.set_index('Fiscal Year').to_dict()['Cash Flow Change (%)']

# Function to get total assets for a company
def get_total_assets(company):
    data = df_sorted[df_sorted['Company'] == company]
    result = data[['Fiscal Year', 'Total Assets']]
    return result.set_index('Fiscal Year').to_dict()['Total Assets']

# Function to get total liabilities for a company
def get_total_liabilities(company):
    data = df_sorted[df_sorted['Company'] == company]
    result = data[['Fiscal Year', 'Total Liabilities']]
    return result.set_index('Fiscal Year').to_dict()['Total Liabilities']

# Function to get cash flow from operating activities for a company
def get_cash_flow(company):
    data = df_sorted[df_sorted['Company'] == company]
    result = data[['Fiscal Year', 'Cash Flow from Operating Activities']]
    return result.set_index('Fiscal Year').to_dict()['Cash Flow from Operating Activities']

# Chatbot Logic
def simple_chatbot():
    print("Welcome to the Financial Analysis Chatbot!")
    print("You can ask about the following queries:")
    print("- What is the total revenue for [Company]?")
    print("- How has net income changed over the last year for [Company]?")
    print("- What is the revenue change for [Company]?")
    print("- What is the asset change for [Company]?")
    print("- What is the liabilities change for [Company]?")
    print("- What is the cash flow change for [Company]?")
    print("- What are the total assets of [Company]?")
    print("- What are the total liabilities of [Company]?")
    print("- What is the cash flow from operating activities for [Company]?")
    print("Supported Companies: Microsoft, Tesla, Apple")
    print("Type 'exit' to quit the chatbot.")

    while True:
        user_query = input("\nAsk your question: ").strip().lower()

        if user_query == 'exit':
            print("Goodbye! Thank you for using the Financial Analysis Chatbot.")
            break
        
        # Check for Total Revenue Query
        if "total revenue" in user_query:
            for company in ['Microsoft', 'Tesla', 'Apple']:
                if company.lower() in user_query:
                    revenue = get_total_revenue(company)
                    print(f"\nTotal Revenue for {company}: {revenue}")
                    break
        
        # Check for Net Income Change Query
        elif "net income change" in user_query:
            for company in ['Microsoft', 'Tesla', 'Apple']:
                if company.lower() in user_query:
                    net_income_change = get_net_income_change(company)
                    print(f"\nNet Income Change for {company}: {net_income_change}")
                    break
         # Check for Revenue Change Query
        elif "revenue change" in user_query:
            for company in ['Microsoft', 'Tesla', 'Apple']:
                if company.lower() in user_query:
                    revenue_change = get_revenue_change(company)
                    print(f"\nRevenue Change for {company}: {revenue_change}")
                    break

        # Check for Asset Change Query
        elif "asset change" in user_query:
            for company in ['Microsoft', 'Tesla', 'Apple']:
                if company.lower() in user_query:
                    asset_change = get_asset_change(company)
                    print(f"\nAsset Change for {company}: {asset_change}")
                    break

        # Check for Liabilities Change Query
        elif "liabilities change" in user_query:
            for company in ['Microsoft', 'Tesla', 'Apple']:
                if company.lower() in user_query:
                    liabilities_change = get_liabilities_change(company)
                    print(f"\nLiabilities Change for {company}: {liabilities_change}")
                    break

        # Check for Cash Flow Change Query
        elif "cash flow change" in user_query:
            for company in ['Microsoft', 'Tesla', 'Apple']:
                if company.lower() in user_query:
                    cash_flow_change = get_cash_flow_change(company)
                    print(f"\nCash Flow Change for {company}: {cash_flow_change}")
                    break
        # Check for Total Assets Query
        elif "total assets" in user_query:
            for company in ['Microsoft', 'Tesla', 'Apple']:
                if company.lower() in user_query:
                    assets = get_total_assets(company)
                    print(f"\nTotal Assets for {company}: {assets}")
                    break
        
        # Check for Total Liabilities Query
        elif "total liabilities" in user_query:
            for company in ['Microsoft', 'Tesla', 'Apple']:
                if company.lower() in user_query:
                    liabilities = get_total_liabilities(company)
                    print(f"\nTotal Liabilities for {company}: {liabilities}")
                    break
        
        # Check for Cash Flow Query
        elif "cash flow" in user_query:
            for company in ['Microsoft', 'Tesla', 'Apple']:
                if company.lower() in user_query:
                    cash_flow = get_cash_flow(company)
                    print(f"\nCash Flow from Operating Activities for {company}: {cash_flow}")
                    break
        
        else:
            print("Sorry, I can only provide information on predefined queries.")
            
# Run the chatbot
#simple_chatbot()
