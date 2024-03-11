import pandas as pd
import pickle
from scipy import spatial

df = pd.read_csv("input.csv")
df = df.rename({df.columns[2]:"y"})

df_thunder = df[df["dmg_type"] == "thunder"].reset_index(drop=True)
df_acid = df[df["dmg_type"] == "acid"].reset_index(drop=True)
df_cold = df[df["dmg_type"] == "cold"].reset_index(drop=True)
df_fire = df[df["dmg_type"] == "fire"].reset_index(drop=True)
df_lightning = df[df["dmg_type"] == "lightning"].reset_index(drop=True)
df_poison = df[df["dmg_type"] == "poison"].reset_index(drop=True)

tree_thunder = spatial.KDTree(df_thunder[["x","y"]])
with open("tree_thunder.pkl","wb") as file_thunder:
    pickle.dump(tree_thunder, file_thunder)

tree_poison = spatial.KDTree(df_poison[["x","y"]])
with open("tree_poison.pkl","wb") as file_poison:
    pickle.dump(tree_poison, file_poison)

tree_cold = spatial.KDTree(df_cold[["x","y"]])
with open("tree_cold.pkl","wb") as file_cold:
    pickle.dump(tree_cold, file_cold)

tree_acid = spatial.KDTree(df_acid[["x","y"]])
with open("tree_acid.pkl","wb") as file_acid:
    pickle.dump(tree_acid, file_acid)

tree_lightning = spatial.KDTree(df_lightning[["x","y"]])
with open("tree_lightning.pkl","wb") as file_lightning:
    pickle.dump(tree_lightning, file_lightning)

tree_fire = spatial.KDTree(df_fire[["x","y"]])
with open("tree_fire.pkl","wb") as file_fire:
    pickle.dump(tree_fire, file_fire)
