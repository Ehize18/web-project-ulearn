import sqlite3

database = input()
table = input()


conn = sqlite3.connect(database)


cur = conn.cursor()


cur.execute(f"""
    SELECT gender, ROUND(AVG(height), 2) AS avg_height, SUM(weight) AS total_weight
    FROM {table}
    GROUP BY gender
""")


for row in cur.fetchall():
    result = ""
    for item in row:
        result.join(item)
    print(result)

conn.close()
