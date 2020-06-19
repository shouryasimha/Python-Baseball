import os
import glob
import pandas as pd
path = "../"
game_files = glob.glob(os.path.join(path,'games','*.EVE'))
game_files.sort()
game_frames=[]
for files in game_files:
    game_frame = pd.read_csv(files,names=['type', 'multi2', 'multi3', 'multi4', 'multi5', 'multi6','event'])
    game_frames.append(game_frame)
print(game_frames)
games = pd.concat(game_frames)
games.loc[games['multi5']=='??',['multi5']]=""
identifiers = games['multi2'].str.extract(r'(.LS(\d{4})\d{5})')
identifiers = identifiers.fillna(method='ffill')
identifiers.columns=['game_id','year']
games = pd.concat([identifiers,games],axis=1,sort=False)
games.fillna(' ',inplace=True)
a=pd.Categorical(games['type'])
games.loc[a,['type']]
# print(a)
