import pandas as pd
from datawrapper import Datawrapper

dw = Datawrapper(access_token = "GswPeiFlwo5MdbAsNJdyLkGG1Wvprw5dP2YEzmgiupKMcXYFokjiAUrFX8femkiJ")

df = pd.read_csv("sample_dataset.csv")
dw_data = df.pivot_table(columns='ticket_type', index='month,year', values='ticket_count', aggfunc='sum')
dw_data = dw_data.apply(lambda x: x*100 / x.sum(),axis=1).reset_index()
new_chart_info = dw.create_chart(title = 'Sum of ticket types', chart_type = 'd3-bars-stacked', data = dw_data)
print(dw_data)
print(new_chart_info)

dw.update_description(
chart_id = new_chart_info['id'],
source_name = 'Internal Data',
source_url = '',
byline = 'Saumya Dudeja',
)
dw.publish_chart(chart_id = new_chart_info['id'])
