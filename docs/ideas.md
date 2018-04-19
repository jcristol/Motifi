Ideas markdown is a place to jot down ideas and a tool to come up with them.



<u>Branch Ideas</u>

- database branch * stepping away from this idea
  - build a database that keeps track of stock time series data
    - <u>problems</u>
      - stock data and time series data in general does not need a database
      - time series data does not really benefit that much from databases
      - building a database and a worker program that collects the data must eventually be deployed to a remote machine that is always on and costs money
- datastore
  - could not think of a great name for this branch
  - this branch idea is an alternative option to the database branch
    - instead of doing the work in the database branch. Build a structure that stores time series stock data in custom binary files that are simply stored in machines file system
    - still need to be a worker that reads from the stock api's and writes to the time series data files
  - the structure of the work is divided in between making a class that encodes a stock's time series data and a worker that makes calls the stock api and writes to the files underwriting the encoded stock classes
    - this class will take arguments from an api 
    - this class will have a write method that will write to an underlying data file
      - the system to write to the datafilee will go as follows
        - symbol—date.dat will be the naming convention for the data files
        - all information related to the symbol will be available in the file timestamped and in sequential order
    - the worker will read from the api and write to the proper data file corresponding to that stock instrument. (dencoder) stands for downloader and encoder
    - the worker will read from the data files given parameters on what needs to be seen and produced in panda format. (dpandar) decoder and panda