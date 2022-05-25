import os
import subprocess
import pandas as pd

input_file = "/home/a1705053/Dropbox/Masters/Codes_Uni/2022_code_tests/gamma.ini"

# with open(input_file, "r") as file_in:
file = pd.read_csv(input_file, names=["gamma", "decay"])
# print(file)
for i,data in file.iterrows():
    os.system(f'sed -e "s:XXXGamma_dcdmXXX:{data.gamma}:g" -e "s:XXXdecayfractionXXX:{data.decay}:g" -e "s:XXXoutputXXX:output_{i}_:g" "example_dm_decay_template.ini" > example_dm_decay.ini')
    subprocess.run(["./class","example_dm_decay.ini"])