#Syntax:
#ALTER TABLE table_name CHANGE column_name column_definition COMMENT "Your comment"

#Example:
#ALTER TABLE Forecast CHANGE FrozenPercipitation FrozenPercipitation tinyint( 4 ) COMMENT '[%] If No Percipitation, this will be -9';
#ALTER TABLE Forecast CHANGE Temperature Temperature decimal( 6,1 ) COMMENT '[deg C]';
#ALTER TABLE Forecast CHANGE MinPercipitation MinPercipitation decimal( 6,1 ) COMMENT '[mm]';
#ALTER TABLE Forecast CHANGE MaxPercipitation MaxPercipitation decimal( 6,1 ) COMMENT '[mm]';
#ALTER TABLE Forecast CHANGE MeanPercipitation MeanPercipitation decimal( 6,1 ) COMMENT '[mm]';
ALTER TABLE Station CHANGE Temperature Temperature decimal( 4,2 ) COMMENT '[deg C]';
ALTER TABLE Station CHANGE Percipitation Percipitation decimal( 5,2 ) COMMENT '[mm]';