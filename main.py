import json

from get_elements import get_elements
from initialize import initialize

# Test
measurements = """
     P21vWjp* C2022 08 08.49812700 38 52.879-07 22 05.96         21.36wUNEOCPF52
     P21vWjp  C2022 08 08.50906800 38 53.246-07 21 22.80         21.55wUNEOCPF52
     P21vWjp  C2022 08 08.53094300 38 53.975-07 19 56.09         21.23wUNEOCPF52
     P21vWjp  C2022 08 08.59686100 38 56.071-07 15 34.24         21.24GVNEOCPF52
     P21vWjp  C2022 08 08.59749100 38 56.087-07 15 31.72         21.17GVNEOCPF52
     P21vWjp ^C2022 08 08.59790700 38 56.070-07 15 29.62         21.64GVNEOCP568
     P21vWjp ^C2022 08 08.59891700 38 56.107-07 15 25.65         21.41GVNEOCP568
     P21vWjp ^C2022 08 08.59984700 38 56.136-07 15 21.78         21.54GVNEOCP568
     P21vWjp |C2022 08 09.40688 00 39 30.66 -06 21 30.5          21.4 GVNEOCP807
     P21vWjp |C2022 08 09.40993 00 39 30.84 -06 21 18.5          21.4 GVNEOCP807
     P21vWjp |C2022 08 09.41307 00 39 30.86 -06 21 05.3          21.4 GVNEOCP807
"""

initialize()
with open("config.json") as f:
    config = json.loads(f.read())
MPC_CODE = config.get("MPC_CODE")
elements = get_elements("P21vWjp", measurements, MPC_CODE)

print("q:", elements.get("q"))
print("e:", elements.get("e"))
