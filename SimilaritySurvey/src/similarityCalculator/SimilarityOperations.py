'''
Created on Dec 29, 2013

@author: ttt
'''

class SimilarityOperations(object):
    
    
    def __init__(self, allUsers=None, similarityCoeffs = {'Timestamp':'0','Your Sehir Student Address':'0','Gender':'0.02','Age':'0.03','Department':'0.07','Hometown':'0.05','Hobbies':'0.13','Choose Your Favorite 2 Book Genres':'0.05','Your Favorite 2 Writers':'0.05','Choose Your Favorite 3 Music Genres':'0.1','Your Favorite 3 Singers':'0.05','Your Favorite 5 Songs':'0.1','Your Favorite 2 Directors':'0.05','Your Favorite 3 Actors/Actress':'0.05','Your Favorite 3 Movies':'0.1','Your Favorite 3 Sport Branches':'0.12','Your Favorite Sport Team':'0.03','Facebook Account Link':'0','Twitter Account Link':'0'}
):
        self.allUsers = allUsers
        self.userID = self.getUserId()
        self.similarityBetweenUsers = [[0 for x in xrange(len(self.userID))] for x in xrange(len(self.allUsers))]
        self.userSpouses = [[0 for x in xrange(len(self.userID))] for x in xrange(len(self.allUsers))]
        self.userSpouse =  [[0 for x in xrange(2)] for x in xrange(len(self.allUsers))]
        self.similarityCoeffs = similarityCoeffs
        
    def apply(self):
        self.compareAllUsers()
        self.combinedPointsOfUsers()
        self.optimizePoints()
        self.findBestSpouse()
        
    def getUserId(self):
        userID = []
        for key in self.allUsers:
            userID.append(self.allUsers[key].get('Your Sehir Student Address'))
        return userID
    
    def compareAllUsers(self):
        
        for key1 in self.allUsers:
            for key2 in self.allUsers:
                if key1 == key2:
                    self.similarityBetweenUsers[key1-1][key2-1] = 0
                else:
                    self.similarityBetweenUsers[key1-1][key2-1] = self.compareUser(self.allUsers[key1], self.allUsers[key2])
        
        
    def compareUser(self,user1,user2):  
        similarityOfUser1 = []
        
        for key in user1:
            if (len(user1[key]) != 0) :   
                similarityOfUser1.append(self.compareAttribute(user1[key], user2[key], key))
            else :
                similarityOfUser1.append(0);
                
        return similarityOfUser1
               
    def compareAttribute(self,att1,att2,attName):
        
        count = 0
        for i in range(len(att1)):
            for j in range(len(att1)):
                try:
                    if(att1[i].upper() == att2[j].upper()) :
                        count += 1
                except AttributeError:
                    if att1[i] == att2[j] :
                        count += 1
        leng = len(att1)
        if count!=0:   
            comparePoint = float(((float(float(self.similarityCoeffs.get(attName))) / leng )) * count)
        else:
            comparePoint = 0
        return comparePoint   
            
    def optimizePoints(self):
        
        for i in range(len(self.userSpouses)):
            for j in range(len(self.userSpouses[i])):
                tempOp = self.userSpouses[i][j] / 1.2400000000000002
                self.userSpouses[i][j] = tempOp
    
    def combinedPointsOfUsers(self):
        
        for i in range(len(self.similarityBetweenUsers)):
            for j in range(len(self.similarityBetweenUsers[i])):
                temp = 0
                if self.similarityBetweenUsers[i][j] is list or i!=j:  
                    for k in range(len(self.similarityBetweenUsers[i][j])):
                        temp += self.similarityBetweenUsers[i][j][k]
                self.userSpouses[i][j] = temp
                    
        
    def findBestSpouse(self):
        
        for i in range(len(self.userSpouses)):
            temp = -1
            for j in range(len(self.userSpouses[i])):
                if (j!= 0) and (self.userSpouses[i][j] > self.userSpouses[i][j-1]):
                    temp = j
                if j == 0 :
                    temp = j
            self.userSpouse[i][0] = temp
            self.userSpouse[i][1] = self.userSpouses[i][temp]
      
    def spouseName(self, spouseNumber):
        return self.userID[spouseNumber]
               
                
              
            
            
            
            
            
            
            
            
            
