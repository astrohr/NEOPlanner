import json
import os
import subprocess
import sys

"""
     P21vZw7  C2022 08 10.51576201 44 24.237+09 18 53.56         20.21GVNEOCPF52
     P21vZw7* C2022 08 10.52636801 44 23.250+09 15 02.21         20.12iUNEOCPF52
     P21vZw7  C2022 08 10.53711901 44 22.105+09 11 10.91         19.67iUNEOCPF52
     P21vZw7  C2022 08 10.54798801 44 20.824+09 07 21.69         19.52iUNEOCPF52
     P21vZw7  C2022 08 10.62198701 44 10.026+08 42 03.72         19.89GVNEOCPF52
     P21vZw7  C2022 08 10.62261601 44 09.932+08 41 51.38         19.90GVNEOCPF52
     A10IpCH* C2022 08 08.96009623 29 40.882-29 53 51.36         17.69oVNEOCPM22
     A10IpCH  C2022 08 08.96247523 29 40.500-29 54 05.83         17.99oVNEOCPM22
     A10IpCH  C2022 08 08.96870423 29 39.497-29 54 44.57         17.84oVNEOCPM22
     A10IpCH  C2022 08 08.97382823 29 38.602-29 55 16.18         17.47oVNEOCPM22
     A10IpCH [C2022 08 09.58245 23 28 14.088-31 10 08.26         17.1 GVNEOCPQ62
     A10IpCH [C2022 08 09.58600 23 28 13.284-31 10 40.87         17.3 GVNEOCPQ62
     A10IpCH [C2022 08 09.59044 23 28 12.254-31 11 21.52         17.2 GVNEOCPQ62
     A10IpCH [C2022 08 09.59488 23 28 11.234-31 12 02.27         17.9 GVNEOCPQ62
     A10IpCH [C2022 08 09.59929 23 28 10.188-31 12 43.99         17.1 GVNEOCPQ62
     A10IpCH  C2022 08 10.03177823 26 31.71 -32 29 47.2          16.8 GVNEOCPK93
     A10IpCH  C2022 08 10.03222423 26 31.56 -32 29 52.9          17.0 GVNEOCPK93
     A10IpCH  C2022 08 10.03266623 26 31.42 -32 29 58.5          16.8 GVNEOCPK93
     A10IpCH  C2022 08 10.03311223 26 31.26 -32 30 04.0          16.9 GVNEOCPK93
     A10IpCH  C2022 08 10.03355623 26 31.11 -32 30 09.7          16.9 GVNEOCPK93
     A10IpCH  C2022 08 10.03400123 26 30.97 -32 30 15.2          16.7 GVNEOCPK93
     A10IpCH  C2022 08 10.21488023 25 45.415-33 11 16.66         16.50oVNEOCPW68
     A10IpCH  C2022 08 10.21668223 25 44.741-33 11 43.37         16.98oVNEOCPW68
     A10IpCH  C2022 08 10.22322823 25 42.209-33 13 21.65         16.45oVNEOCPW68
     A10IpCH  C2022 08 10.22906123 25 39.931-33 14 50.24         16.84oVNEOCPW68
     A10IpCH KC2022 08 10.54213 23 23 49.06 -34 44 39.1          16.7 VqNEOCPE23
     A10IpCH KC2022 08 10.54907 23 23 45.51 -34 47 02.8          16.7 VqNEOCPE23
     A10IpCH KC2022 08 10.55601 23 23 41.95 -34 49 27.6          16.6 VqNEOCPE23
"""


def get_elements(name, measurements, MPC_CODE):
    """Returns orbital elements dictionary"""
    # -C MPC_CODE
    # -E 17 (computer friendly output?)
    os.chdir("find_orb")
    with open("measurements.txt", "w") as f:
        f.write(measurements)

    if sys.platform == "darwin":
        fo = "./fo"

    # sys.platform will be win32 regardless of the bitness
    # code is intended for 64 bit platform
    elif sys.platform == "win32":
        fo = "fo64.exe"

    subprocess.run([fo, "measurements.txt", "-C", MPC_CODE],
                   check=True, stdout=subprocess.PIPE).stdout

    with open("elem_short.json") as f:
        data = json.loads(f.read())
        elements = data.get("objects").get(name).get("elements")

    # os.remove("elem_short.json")
    # os.remove("measurements.txt")
    os.chdir("..")

    return elements
