import csv 
with open('C:\\Users\\inapraz\\Documents\\git\\100 Sales Records.csv') as csvfile:
    with open('C:\\Users\\inapraz\\Documents\\git\\copy.csv', "w") as myfile: 
        readCSV = csv.reader(csvfile, delimiter=',')
        writer = csv.writer(myfile)
        all=[]
        count=0;
        ncol=len(next(readCSV))
        print(ncol)
        #print (row0)
        for row in readCSV:
            row0=next(readCSV)
            t=float(row[ncol-1])
            k=float(row[ncol-2])
            p=round((t/k)*100, 2)
            row.append(p)
            all.append(row)
            

        for rows in all:
            writer.writerows(all)
    