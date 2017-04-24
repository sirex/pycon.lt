#!/usr/bin/env python3.6

from datetime import timedelta
from collections import namedtuple


Entry = namedtuple('Entry', ('time', 'title'))

TIMETABLE = [
    Entry(60, 'Dalyvių registracija.'),
    Entry(10, 'Konrefencijos pradžia, renginio atidarymas.'),

    Entry(30, 'Endrew Svetlov'),
    Entry(25, 'Mantas Zimnickas'),

    Entry(15, 'Pertrauka'),

    Entry(25, 'Irmantas Ramoška'),
    Entry(15, 'Simona Bekeraitė'),

    Entry(10, 'Greitieji pranešimai'),
    Entry(15, 'Įdarbinimo sesija'),

    Entry(45, 'Pietų pertrauka'),

    Entry(25, 'Petras Zdanavičius'),
    Entry(25, 'Justas Sadzevičius'),

    Entry(15, 'Pertrauka'),

    Entry(25, 'Šarūnas Navickas'),
    Entry(25, 'Karolis Kalantojus'),

    Entry(10, 'Renginio uždarymas'),
]


def main():
    time = timedelta(hours=10)
    for entry in TIMETABLE:
        a = time
        b = time = time + timedelta(minutes=entry.time)
        print(f"{str(a)[:5]} - {str(b)[:5]}  {entry.title}")


if __name__ == "__main__":
    main()
