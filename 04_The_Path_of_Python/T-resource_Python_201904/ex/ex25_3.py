# ex25_3.py
import pandas as pd
states = {'state':['North America', 'South America', 'Europe',
                   'Afirca', 'Asia'],
          'population':[3.8, 6.2, 7.4, 12.28, 45.45]}
statedf = pd.DataFrame(states, columns=['population'],
                      index=states['state'])
cum = statedf['population'].cumsum()
statedf['Cumulative'] = cum
print(statedf)











