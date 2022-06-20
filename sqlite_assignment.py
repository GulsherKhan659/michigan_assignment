def run():
    from urllib  import request
    import  requests
    import  ssl
    import sqlite3
    # SSL CERTIFICATE
    ctx = ssl.create_default_context()
    ctx.check_hostname=False
    ctx.verify_mode = ssl.CERT_NONE


    # data = requests.get("https://www.py4e.com/code3/mbox.txt?PHPSESSID=5754b04074d3b2c4f30ff61fb8634177")
    # with open("./file-data.txt",mode="w") as file:
    #     file.write(data.text)
    conn = sqlite3.connect("email_org_db.sqlite")
    cursor = conn.cursor()
    cursor.execute("DROP TABLE  IF EXISTS EmailCount")
    createq ="""Create Table Counts(org TEXT,count INTEGER)"""
    try:
        cursor.execute(createq)
    except:
        pass



    with open("./file-data.txt") as file:
        for line in file:
            if  not line.startswith("From: "):continue
            data =line.split() # Split line by empty space
            email = data[1].split() # data[1] have email line
            org =email[0].split("@")[1]

            cursor.execute("SELECT count from Counts WHERE org = ?", (org,))
            row = cursor.fetchone()
            if row is None:
                cursor.execute("INSERT INTO Counts(org,count) VALUES (?,1)", (org,))
            else:
                cursor.execute("Update Counts SET count = count+1 WHERE org = ?", (org,))

            conn.commit()
    for data in cursor.execute("SELECT * FROM Counts ORDER BY count DESC LIMIT 10"):
         print("ORG = {} AND COUNT = {}".format(data[0],data[1]))