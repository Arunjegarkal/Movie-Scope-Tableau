import json

with open("1.json", "r") as f:
    for line in f: 
        if(len(line)>1):
            #line = f.readline() # read only the first tweet/line
            data = json.loads(line.encode("UTF-8")) # load it as Python dict
            print "title	year	imdbID	rating	genre	value	revenue	original_language	popularity	vote_average	budget"
            for i in range (0,data.__len__()):
                print data[i]["imdbInfo"]["title"].encode("UTF-8"),"	",data[i]["imdbInfo"]["year"].encode("UTF-8"),"	",data[i]["imdbInfo"]["imdbID"].encode("UTF-8").strip(" "),"	",data[i]["imdbInfo"]["rating"].encode("UTF-8"),"	",data[i]["imdbInfo"]["genre"].encode("UTF-8"),"	",data[i]["imdbInfo"]["value"].encode("UTF-8"),"	",data[i]["tmdbInfo"]["revenue"],"	",data[i]["tmdbInfo"]["original_language"].encode("UTF-8"),"	",data[i]["tmdbInfo"]["popularity"],"	",data[i]["tmdbInfo"]["vote_average"],"	",data[i]["tmdbInfo"]["budget"]
    f.close()
