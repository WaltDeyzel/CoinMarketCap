import operator
from constants import Constants as con
class DisplayData:
    heading = con.heading

    def getPairs(self, percent_change_info):
        #DISPLAY TOP 10
        n = con.numberOfElements
        bestPerforming = []
        for percent_change in percent_change_info:
            best = percent_change[:n+1]
            best.reverse()
            worst = percent_change[-n:]
            pair = [worst, best]
            bestPerforming.append(pair)
        return bestPerforming

    def displayData(self, percent_change_info):
        #DISPLAY DATA SET
        #DISPLAY TOP 10
        n = con.numberOfElements
        bestPerforming = DisplayData.getPairs(DisplayData, percent_change_info)

        for section in bestPerforming:
            print()
            print(self.heading, ' ', self.heading)
            print(con.stripes, con.stripes)
            
            lhs = section[0] # DATA DISPLAYED ON THE LEFT
            rhs = section[1] # DATA DISPLAYED ON THE RIGHT

            for i in range(n):
                displayL = lhs[i].displayDaily()
                displayR = rhs[i].displayDaily()

                if(section == bestPerforming[0]):
                    displayL = lhs[i].displayHourly()
                    displayR = rhs[i].displayHourly()
            
                #DO NOT NEED TO CHECH FOR SECTION == BESTPERFORMING[1] BECAUSE IT IS THE DEFAULT
                    
                if(section == bestPerforming[2]):
                    displayL = lhs[i].displayWeekly()
                    displayR = rhs[i].displayWeekly()
                
                if(section == bestPerforming[3]):
                    displayL = lhs[i].displayMonthly()
                    displayR = rhs[i].displayMonthly()
                
                if(section == bestPerforming[4]):
                    displayL = lhs[i].displaySixty()
                    displayR = rhs[i].displaySixty()
                
                if(section == bestPerforming[5]):
                    displayL = lhs[i].displayNinety()
                    displayR = rhs[i].displayNinety()
                
                print(displayL,'|', displayR,'|')
            print(con.stripes, con.stripes)
    
    def displayWatchlist(self, watchlist):
        print(con.stripes, con.stripes)
        print()
        print('___________________________________WATCHLIST___________________________________')
        print(self.heading)
        print(con.stripes, con.stripes)

        for coin in watchlist:
            print(coin.displayWeekly())

    def displayWorstPerforming(self, weekly):
        print()
        print('WORST PERFORMING IN TOP' , len(weekly))
        print(self.heading)
        for coin in weekly:
            print(coin.displayWeekly())
    
    def displayGrowth(self, watchlist):
        print(con.stripes, con.stripes)
        print()
        print('___________________________________GROWTH___________________________________')
        print(self.heading)
        print(con.stripes, con.stripes)

        for coin in watchlist:
            print(coin.displayGrowth())