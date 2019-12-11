import glob
import os
class ConvertOptionToFlatRecord:
    def flat(self,stockname,directory_name):
        directory=directory_name+"/"+stockname+"/*.csv"
        print("Checking in .. ")
        print(directory)
        files = glob.glob(directory)
        files.sort()
        strike_dict={}
        dateAndTime = ""
        for eachFile in files:
            name=os.path.basename(eachFile)
            dateAndTime=name.split(".")
            handle=open(eachFile,"r")
            contents=handle.read()
            records=contents.split("\n")
            for record in records:
                elements=record.split(",")
                if elements[0] == "Call OI":
                    continue
                if len(elements) != 7:
                    continue
                data = dateAndTime[0]+","+dateAndTime[1].replace("-",".")
                for element in elements:
                    data = data + ","+element
                strike = elements[3]
                
                if strike in strike_dict:
                    strike_dict[strike].append(data)
                else:
                    strike_dict.__setitem__(strike,[])
                    strike_dict[strike].append("Date,Hour.Min,Call OI,Call IV,Call Price,Strike Price,Put Price,Put_IV,Put OI")
                    strike_dict[strike].append(data)
            handle.close()
        keys=strike_dict.keys()
        for key in keys:
            content=strike_dict[key]
            file_name = directory_name+"/"+stockname+"/strike_data/"+dateAndTime[0]
            if not os.path.exists(file_name):
                os.makedirs(file_name)
            file_name = directory_name+"/"+stockname+"/strike_data/"+dateAndTime[0]+"/"+key+".csv"
            print("Writing option chain of strike : "+ key +" into --> "+file_name)
            f = open(file_name,"w+")
            for record in content:
                f.write(record)
                f.write("\n")
            f.close()
        for eachFile in files:
            os.remove(eachFile)

fileConverter = ConvertOptionToFlatRecord()
fileConverter.flat("BANKNIFTY","D:/Data/stocks/options/snapshot")