# 82
# json module in python
# java script object notation

import json

# load and loads functions
data='{"var1":"arvind","var2":"priya"}'

parsed=json.loads(data)
print(parsed["var1"],parsed["var2"])
print(type(parsed))

# task > json.load ???

# jason.dump
data2={
    "channel_name":"karanjelearning",
    "cars":['lambhorgini','rangerover','creta','verna'],
    "homes":('kotgyal','bidar','hydrabad','nittur'),
}

jscomp=json.loads(data2)
print(jscomp["channel_name"])

# task > what is sort keys parameter in dumps
