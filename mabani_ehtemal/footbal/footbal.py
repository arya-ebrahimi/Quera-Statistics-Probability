import pandas as pd

league_data = pd.read_csv("spanish_league.csv")
league_data.head()

example_prob=(len(league_data[league_data['localTeam']=='Real Madrid'][league_data['localGoals']==0])/(len(league_data)))

#calculate probability:
unusual_game = (len (league_data[league_data['localGoals'] + league_data['visitorGoals'] >= 7]) + len (league_data[league_data['localGoals'] + league_data['visitorGoals'] <= 1])) / len(league_data)

season_prob = len(league_data[league_data['season'] == '1982-83']) / len(league_data)


real_local = league_data[league_data['localTeam'] == 'Real Madrid']
local_three = real_local[real_local['localGoals'] == 3]

a= len(local_three) / len(real_local)

b= len(local_three[local_three['visitorGoals'] == 1]) / len(real_local[real_local['visitorGoals'] == 1])

c= len(local_three[local_three['season'] >= '1986-87']) / len(real_local[real_local['season'] >= '1986-87'])



equals_three = (league_data[league_data['localGoals'] + league_data['visitorGoals'] == 3])

p_a = len(equals_three[equals_three['localGoals'] > equals_three['visitorGoals']]) / len(equals_three) 
p_b = len(equals_three[equals_three['localGoals'] == 0]) / len(equals_three)
p_c = len(equals_three[equals_three['visitorGoals'] == 0]) / len(equals_three)
p_d = len(league_data[league_data['visitorGoals'] >= 2]) / len(league_data)

visitor_wins = league_data[league_data['visitorGoals'] > league_data['localGoals']]
p_e = len(visitor_wins[visitor_wins['visitorGoals'] >= 2]) / len(visitor_wins)

draw = league_data[league_data['visitorGoals'] == league_data['localGoals']]
p_f = len(draw[draw['visitorGoals'] >= 2]) / len(draw)



sum_two = league_data[league_data['visitorGoals'] + league_data['localGoals'] == 2]

pAB = len(sum_two[sum_two['visitorGoals'] == sum_two['localGoals']]) / len(sum_two) 

draw = league_data[league_data['localGoals'] == league_data['visitorGoals']]
p_draw = len(draw) / len(league_data)
p_twoGolasDraw = len(draw[draw['localGoals'] + draw['visitorGoals'] == 2]) / len(draw)

nDraw = league_data[league_data['localGoals'] != league_data['visitorGoals']]
p_nDraw = len(nDraw) / len(league_data)
p_twoGoalsNDraw = len(nDraw[nDraw['localGoals'] + nDraw['visitorGoals'] == 2]) / len(nDraw)

pB_1 = p_twoGolasDraw * p_draw + p_twoGoalsNDraw * p_nDraw

check_law_total = pB_1 == (len(sum_two) / len(league_data))
check_law_total


bayes = (p_twoGolasDraw * p_draw) / pB_1
check_bayes= pAB == bayes
check_bayes