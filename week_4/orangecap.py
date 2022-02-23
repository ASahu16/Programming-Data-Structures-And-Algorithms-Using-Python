def orangecap(d):
  player_score_table = {}
  for match in d:
    for player in d[match]:
      try:
        player_score_table[player] = player_score_table[player] + d[match][player]
      except:
        player_score_table[player] = d[match][player]

  max_score = list(player_score_table.values())[0]
  player_name = list(player_score_table.keys())[0]
  for player in player_score_table:
    if max_score < player_score_table[player]:
      max_score = player_score_table[player]
      player_name = player
  
  return (player_name,max_score)
       




print(orangecap({'match1':{'player1':57, 'player2':38}, 'match2':{'player3':9, 'player1':42}, 'match3':{'player2':41, 'player4':63, 'player3':91}}))