import requests
import json

header = {"Authorization": "Bearer DGXDDdL0J8nkGGDudmyUxV1jLl-r1OPZdCgY2rt0uT8"}
url = 'https://api.tibber.com/v1-beta/gql'


def run_query(query): # A simple function to use requests.post to make the API call. Note the json= section.
    request = requests.post(url, json={'query': query}, headers=header)
    
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))

        
# The GraphQL query (with a few aditional bits included) itself defined as a multi-line string.       
consumption = """
{
  viewer {
    homes {
      consumption(resolution: HOURLY, last: 1) {
        nodes {
          from
          to
          cost
          consumption
          consumptionUnit
        }
      }
    }
  }
}

"""

price = """
{
  viewer {
    homes {
      currentSubscription {
          priceInfo {
              tomorrow {
                  total
                  energy
                  tax
                  startsAt
                  }
        }
      }
    }
  }
}
"""

c = run_query(consumption) # Execute the query
p = run_query(price) # Execute the query
print(json.dumps(c["data"]["viewer"]["homes"][0]["consumption"]["nodes"][0], indent=2))
prices = json.dump(p["data"]["viewer"]["homes"][0]["currentSubscription"]["priceInfo"]["tomorrow"])
print(type(prices))