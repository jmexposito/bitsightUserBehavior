import requests
import time

# API DOCUMENTATION: https://help.bitsighttech.com/hc/en-us/articles/360022913734-GET-Finding-Details
api_key = "USER_APIKEY"
# ASSETS AFFECTING THE RATING IN USER BEHAVIOUR CATEGORY
url = "https://api.bitsighttech.com/ratings/v1/companies/XXXXXXXX/findings?risk_vector=file_sharing"


# API CHECK
response = requests.get(url, auth=(api_key, ""))
print(response.status_code)
if response.status_code == 401 and str(response.json()["detail"]) == "Invalid token":
        print("Invalid Api key. Please Insert Valid Api key:\n\n\n")
        print(response.status_code)
        exit()
else:
        print("Api Key is Valid.\n")


json = response.json()
#print(json)

#time.sleep(5)




def u_behavior():
    
    for result in json['results']:
        for r in result['assets']:
            company_assets = r['asset']
            print("\nASSET -->  " + company_assets + '\n')


    for result in json['results']:
        #print(result)      # JSON RESPONSE
        for detail in result['details']:
            #for d in detail['category']:   # YOU CAN FILTER BY CATEGORY, COUNTRY, START/END DATES...
                #print(d)
            print(detail)


u_behavior()
        
