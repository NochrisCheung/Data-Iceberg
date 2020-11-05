from mido import MidiFile
import plotly.graph_objects as go
import visualisation_toolkit.chart_format_config as cfc
import plotly.express as px
import pandas as pd
import time
import datetime


mid = MidiFile('topics/zd_hey_jude_midi_visualisation/data_processed/BEATLES_THE_-_Hey_Jude.mid')

for msg in mid:
    if msg.is_meta:
        print(msg)

mid.tracks
for i, track in enumerate(mid.tracks):
    print('Track {}: {}'.format(i, track.name))
    for msg in track:
        if i == 1:
            print(msg)

messages = pd.DataFrame([], columns = ['channel','type','note','time'])
# for msg in mid:
#     if msg.type in ['note_on','note_off']:
#         # print([msg.channel, msg.type, msg.note, msg.time])
#         new_note = {'channel':msg.channel, 'type': msg.type, 'note':msg.note, 'time':msg.time}
#         # pd.DataFrame([msg.channel, msg.type, msg.note, msg.time], columns = ['channel','type','note','time'], axis = 1)
#         # ,columns = ['channel','type','note','time']),
#         messages = messages.append(new_note, ignore_index= True)
for i, track in enumerate(mid.tracks):
    # print('Track {}: {}'.format(i, track.name))
    for msg in track:
        if msg.type in ['note_on','note_off']:
        # if i == 1:
            new_note = {'channel':msg.channel, 'type': msg.type, 'note':msg.note, 'time':msg.time}
        #         # pd.DataFrame([msg.channel, msg.type, msg.note, msg.time], columns = ['channel','type','note','time'], axis = 1)
        #         # ,columns = ['channel','type','note','time']),
            messages = messages.append(new_note, ignore_index= True)


messages_set = messages
# messages_set['time'] = messages['time']*3
messages_set.head(30)
channel_one_messages = messages_set[messages_set['channel'] == 1].reset_index(drop = True)
channel_one_messages = pd.concat([channel_one_messages[channel_one_messages['type']=='note_on'][['channel','note','time']].reset_index(drop = True),channel_one_messages[channel_one_messages['type']=='note_off']['time'].reset_index(drop = True)], axis=1)
channel_one_messages.columns = ['channel','note','on_time','duration']
channel_one_messages['end_time'] = channel_one_messages['on_time'] + channel_one_messages['duration']
channel_one_messages['end_time'] = channel_one_messages['end_time'].cumsum()
channel_one_messages['start_time'] = channel_one_messages['end_time'] - channel_one_messages['duration']
channel_one_messages.tail(50)
channel_one .head(50)
messages_set['channel'].unique
channel_one =  messages_set[messages_set['channel'] == 1]
channel_one['end_time'] = channel_one['time'].cumsum()
channel_one[channel_one['note'] == 72]
for o in channel_one[channel_one['note'] == 72].values:
    print(o)

color_scheme = [
    '65,105,225',
    '127,255,212',
    '144,238,144',
    '240,230,140',
    '255,160,122',
    '205,92,92',
    '219,112,147',
    '186,85,211',
    '147,112,219',
    '33,33,33'
]
channel_one['note'].unique()
channel_one.sort_values('time')
channel_one[channel_one['note'] == 89].values
channel_one[channel_one['note'] == 72].values[1][1]
channel_one

channel_one.tail(50)

fig = cfc.configure_chart()
# for c in messages_set['channel'].unique():
c=1
channel_one = messages_set[messages_set['channel'] == c]
channel_one.head(20)
channel_one['end_time'] = channel_one['time'].cumsum()
channel_one = channel_one.sort_values('end_time', ascending = False)
for n in channel_one['note'].unique():
    for o in channel_one[channel_one['note'] == n].values:
        if o[1] == 'note_on':
            fig.add_trace(
                go.Bar(
                    x = [o[4]],
                    y = [n],
                    orientation = 'h',
                    marker = dict(
                        # color = 'rgba('+color_scheme[1]+',1)',
                        color = 'rgba(240,248,255,1)',
                        line = dict(
                            # shape = 'spline',
                            width = 0,
                            # color = 'rgb('+color_scheme[i]+')',
                            color = 'rgba(240,248,255,1)',
                        ),
                    ),
                    width = 1
                ),
            )
        # elif o[1] == 'note_off':
        else:
            fig.add_trace(
                go.Bar(
                    x = [o[4]],
                    y = [n],
                    orientation = 'h',
                    marker = dict(
                        color = 'rgba('+color_scheme[c-1]+',1)',
                        line = dict(
                            # shape = 'spline',
                            width = 0.,
                            # color = 'rgb('+color_scheme[i]+')',
                            color = 'rgba(240,248,255,1)',
                        ),
                    ),
                    width = 1
                ),
            )

fig.update_layout(
    barmode = 'overlay',
    showlegend = False,
    yaxis = dict(
        showgrid = False
    )
)

fig.update_layout(
    width = 1400,
    # barmode = 'group',
    # bargap = 0,
    # bargroupgap = 0,
)

fig.update_layout(
    margin=dict(
        l=52,
        r=52,
        b=60,
        t=100,
        pad = 5
    )
)

fig.show()

fig.write_image('./topics/zd_hey_jude_midi_visualisation/data_processed/BEATLES_THE_-_Hey_Jude.svg')

# channel_one_messages['start_time_dt'] = ['2020-01-01 '+ str(datetime.timedelta(seconds=round(st+60,2))) for st in channel_one_messages['start_time'].tolist()]
# channel_one_messages['end_time_dt'] = ['2020-01-01 '+ str(datetime.timedelta(seconds=round(et+60,2))) for et in channel_one_messages['end_time'].tolist()]
# channel_one_messages

# px.timeline(channel_one_messages, x_start='start_time_dt', x_end='end_time_dt', y='note', color='channel')



# pitch = []
# note_on = []
# note_off = []
# for i, track in enumerate(mid.tracks):
#     pitch = []
#     note_on = []
#     note_off = []
#     print('Track {}: {}'.format(i, track.name))
#     for msg in track:
#         if i == 1 and msg.type == 'note_on':
#             pitch = pitch + [msg.note]
#             note_on = note_on + [msg.time]
#             ,'note_off']
#             print(msg)
