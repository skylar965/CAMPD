
import requests
import pandas as pd

API_KEY = 'RQplOAYzGxdIJMlywGxBbex7qwL5nhcrihe7QGl5'

start_year = 2010
end_year = 2010

states = [ 'MT','AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
           'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME',
           'MI', 'MN', 'MO', 'MS',  'NC', 'ND', 'NE', 'NH', 'NJ', 'NM',
           'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX',
           'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']
# states = ['MT']

for current_year in range(start_year, end_year+1, 1):
    
    for state in states:
# api parameters for the streaming facility/attributes endpoint
        beginDate = f'{current_year}-01-01'
        endDate = f'{current_year}-01-01'
        parameters = {
            'api_key': API_KEY,
            'year': current_year,
            'beginDate': beginDate,
            'endDate': endDate,
            'stateCode': state,
        }
    
# making get request using the emissions/apportioned/annual endpoint
        streamingUrl = "https://api.epa.gov/easey/streaming-services/emissions/apportioned/hourly"
        streamingResponse = requests.get(streamingUrl, headers={'content-type':'application/json'}, params=parameters)
        streamingResponse_df = pd.DataFrame(streamingResponse.json())
        # drop the rows with missing value
        # streamingResponse_df = streamingResponse_df[pd.notnull(streamingResponse_df['so2Mass'])]
        streamingResponse_df.to_csv(f"emission_{state}_{current_year}.csv")
        
        # for state in set(streamingResponse_df['stateCode']):
        #     state_table = streamingResponse_df.loc[streamingResponse_df['stateCode'] == state]
        #     state_table.to_csv(f"emission_{state}_{current_year}.csv")
