# invoices are stored in a dictionary for storage after extracting details
invoice={
    "invoice_id":"INV001",
    "vendor":"ABC PVT LTD",
    "amount":2500,
    "due_date":"05-11-2025"
}
# print(invoice)

#list of diffrent invoices

invoices=[]
invoices.append(invoice)
invoices.append({
    "invoice_id":"INV002",
    "vendor":" XYZ LTD",
    "amount":3000,
    "due_date":"04-11-2025"
})

# print(invoices)

#sort by due date

from datetime import datetime

invoices.sort(key=lambda x:
              datetime.strptime(x['due_date'],
                                "%d-%m-%Y"))

print(invoices)

#save to json
import json
with open("invoice.json","w") as f:
    json.dump(invoices , f , indent=4)