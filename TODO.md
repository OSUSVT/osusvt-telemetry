#TODO
##Migrate the ITEMPROP array
##Refactor to use only import statements
##Change C# code to use epoch time
```
Int32 unixTimestamp = (Int32)((DateTime.UtcNow.Subtract(new DateTime(1970, 1, 1))).TotalSeconds * 1000);
```
##Functional Decompostion
###Move Code that accesses database to a deticated file
###Store JavaScript in their own files
##Rename models.py to something more semantically correct
##Research/Implement multiproccessing for database updates
```
threading.daemon = True #Terminates Proccess if main thread exits
```
Python set() could be used to determine if a peice of data has been 'grabed'
###Assumptions for Updating Data
1) Data Will Never Be Deleted While Telemetry is Running
2) New Data will have a Greater Index than the Maximum Index Number already in the database
##Possible Structure of Data
```
ns.database = ordered from most recent to oldest array of tupples containing the database data
ns.database[-1800:] = get last 30 minutes
ns.current = dictionary of the most current values in the database for 
sd.database.insert(0, (121351, 13216351, 1213151) )
speciallizedarray = [row[0], row[rownum]] for row in ns.database
```
##Kill all Humans!!
