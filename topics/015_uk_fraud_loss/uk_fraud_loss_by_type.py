import pandas as pd
import plotly.graph_objects as go
import visualisation_toolkit.chart_format_config as cfc

fraud_loss_df = pd.read_csv('./data_source/uk_finance/fraud_the_fact/uk_fraud_loss_by_type.csv')
fraud_loss_df = fraud_loss_df.dropna()
fraud_loss_df['Loss Value'] = fraud_loss_df['Loss Value'].str.extract('(\d+..)').astype('float')
fraud_loss_df['Report Volume'] = fraud_loss_df['Report Volume'].str.replace(',','').astype('float')
fraud_loss_by_category = fraud_loss_df.groupby(by = 'Fraud Category')[['Loss Value', 'Report Volume']].sum().sort_values(by = 'Loss Value', ascending = False).reset_index()
fraud_loss_by_category['Fraud Category'].append(fraud_loss_df['Fraud Typology'])
fraud_loss_by_category['Fraud Category']
fig = cfc.configure_chart()

fig.add_trace(
    go.Sunburst(
        labels = ['total'] + fraud_loss_by_category['Fraud Category'].append(fraud_loss_df['Fraud Typology']).reset_index(drop = True).tolist()[0:],
        parents = ['']+ pd.DataFrame(['total']*4, columns = ['Fraud Category'])['Fraud Category'].append(fraud_loss_df['Fraud Category']).tolist()[0:],
        values = [round(fraud_loss_by_category['Loss Value'].sum(),1)]+[round(n,1) for n in fraud_loss_by_category['Loss Value'].append(fraud_loss_df['Loss Value']).reset_index(drop = True).tolist()][0:],
        branchvalues = 'total',
    )
)

fig.update_traces(
    marker = dict(
        colors = ['white','navy','indigo','steelblue', 'darkslateblue'],
        # size = 10
        # ,'white'],
    ),
    textinfo = 'none'
)

fig.update_layout(
     showlegend = False,
     margin=dict(
         l=30,
         r=30,
         b=60,
         t=180,
         pad = 5
     )
)

fig = cfc.configure_chart()

fig.add_trace(
    go.Pie(
        labels = ['total'] + fraud_loss_by_category['Fraud Category'].append(fraud_loss_df['Fraud Typology']).reset_index(drop = True).tolist()[0:],
        parents = ['']+ pd.DataFrame(['total']*4, columns = ['Fraud Category'])['Fraud Category'].append(fraud_loss_df['Fraud Category']).tolist()[0:],
        values = [round(fraud_loss_by_category['Loss Value'].sum(),1)]+[round(n,1) for n in fraud_loss_by_category['Loss Value'].append(fraud_loss_df['Loss Value']).reset_index(drop = True).tolist()][0:],
        branchvalues = 'total',
    )

fig.write_image('./topics/014_uk_fraud_loss/data_processed/fraud_loss_by_type.svg')
