import pandas as pd
import plotly.graph_objects as go
import visualisation_toolkit.chart_format_config as cfc

fraud_loss_df = pd.read_csv('./data_source/uk_finance/fraud_the_fact/uk_fraud_loss_by_type.csv')
fraud_loss_df = fraud_loss_df.dropna()
fraud_loss_df['Loss Value'] = fraud_loss_df['Loss Value'].str.extract('(\d+..)').astype('float')
fraud_loss_df['Report Volume'] = fraud_loss_df['Report Volume'].str.replace(',','').astype('float')
# fraud_loss_by_category = fraud_loss_df.groupby(by = 'Fraud Category')[['Loss Value', 'Report Volume']].sum().sort_values(by = 'Loss Value', ascending = False).reset_index()
# fraud_loss_by_category['Fraud Category'].append(fraud_loss_df['Fraud Typology'])

fraud_loss_df['Value per Case'] = round(fraud_loss_df['Loss Value']/fraud_loss_df['Report Volume']*1000000,2)
fraud_loss_df = fraud_loss_df.sort_values(by = 'Value per Case', ascending = True).reset_index(drop = True)
fraud_loss_df
fig = cfc.configure_chart()

fig.add_trace(
    go.Bar(
        x = fraud_loss_df['Value per Case'].tail(10),
        y = fraud_loss_df['Fraud Typology'].tail(10),
        orientation = 'h'
    )

)

fig.update_traces(
    marker = dict(
        # color = [1,3,1,1,1,1,1,2,2,2],
        color = ['steelblue','steelblue','steelblue','indigo','indigo','indigo','indigo','indigo','darkslateblue','indigo']
        # colorscale = ['navy','indigo','steelblue', 'darkslateblue']
    )
)

fig.update_layout(
    xaxis = dict(
        zeroline = True,
        rangemode = 'tozero'
    ),
    yaxis = dict(
        showgrid = False,
        linewidth = 1,
        linecolor='lightsteelblue',
        showline = True
    )
)
