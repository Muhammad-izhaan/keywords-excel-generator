import pandas as pd

# Step 1: List of companies with contact details

companies =[

    {
        "name": "Apple Inc.",
        "service_number": "1-800-MY-APPLE",
        "email": "contactus@apple.com"
    },
    {
        "name": "Microsoft Corporation",
        "service_number": "1-800-MICROSOFT",
    }


]


def generate_keywords(company_name):
    return [
        f"{company_name} customer service number",
        f"{company_name} contact number",
        f"{company_name} toll-free number",
        f"{company_name} helpline",
        f"{company_name} support number",
        f"{company_name} customer care number,"
        f"{company_name}, "
        f"{company_name} help,"
        f"{company_name} support,"
        f"{company_name} phone number,"
        f"{company_name} website,"
        f"{company_name} email help,"
        f"{company_name} email,"
        f"{company_name} company,"
    ]


data = []


data.append([
    'Company Name', '', '', 
    'Phone Number', '', '', 
    'Email Support', '', '', 
    'Keywords'
])


for company in companies:
    company_name = company['name']
    service_number = company['service_number']
    email = company['email']
    keywords = generate_keywords(company_name)

 
    keywords_string = ', '.join(keywords)
    

    data.append([
        company_name, '', '', 
        service_number, '', '', 
        email, '', '', 
        keywords_string
    ])


df = pd.DataFrame(data)

e
df.to_excel('company_keywords_final.xlsx', index=False, header=False)

print("Keywords, contact numbers, and emails generated and saved to 'company_keywords_final.xlsx'!") 