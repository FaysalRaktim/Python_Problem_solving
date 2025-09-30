'''

                                            A. Series of Crimes

The Berland capital is shaken with three bold crimes committed by the Pihsters, a notorious criminal gang.

The Berland capital's map is represented by an n × m rectangular table. Each cell of the table on the map
represents some districts of the capital.

The capital's main detective Polycarpus took a map and marked there the districts where the first three robberies
had been committed as asterisks. Deduction tells Polycarpus that the fourth robbery will be committed in such district,
that all four robbed districts will form the vertices of some rectangle, parallel to the sides of the map.

Polycarpus is good at deduction but he's hopeless at math. So he asked you to find the district where the fourth robbery
will be committed.

Input
The first line contains two space-separated integers n and m (2 ≤ n, m ≤ 100) — the number of rows and
columns in the table, correspondingly.

Each of the next n lines contains m characters — the description of the capital's map. Each character can either be
a "." (dot), or an "*" (asterisk). A character equals "*" if the corresponding district has been robbed. Otherwise,
it equals ".".

It is guaranteed that the map has exactly three characters "*" and we can always find the fourth district that meets the
problem requirements.

Output
Print two integers — the number of the row and the number of the column of the city district that is the fourth one to be robbed.
The rows are numbered starting from one from top to bottom and the columns are numbered starting from one from left to right.

'''

district,robbery_place = map(int, input().split())

atteck_location = [input().split() for _ in range(district)]

place_position = []

for i in range(district):
    for j in range(robbery_place):
        if atteck_location[i][j] == "*":
            place_position.append((i+1, j+1))

rows = [pos[0] for pos in place_position]
cols = [pos[1] for pos in place_position]

for i in rows:
    if rows.count(i) == 1:
        next_dis = i
        break

for j in cols:
    if cols.count(j) == 1:
        next_rob = j
        break

print(next_dis, next_rob)