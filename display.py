import operator
from constants import Constants as con
class DisplayData:
    heading = con.heading

    def displayData(self, hourly, daily, weekly, monthly, sixty, ninety):
        #DISPLAY DATA SET
        #DISPLAY TOP 10
        n = con.numberOfElements
        hourly_worst = hourly[:n+1]
        hourly_best = hourly[-n:]
        daily_worst = daily[:n+1]
        daily_best = daily[-n:]
        weekly_worst = weekly[:n+1]
        weekly_best = weekly[-n:]
        monthly_worst = monthly[:n+1]
        monthly_best = monthly[-n:]
        sixty_worst = sixty[:n+1]
        sixty_best = sixty[-n:]
        ninety_worst = ninety[:n+1]
        ninety_best = ninety[-n:]

        hourly_best.reverse()
        weekly_best.reverse()
        daily_best.reverse()
        monthly_best.reverse()
        sixty_best.reverse()
        ninety_best.reverse()
        #----------------------------------------------------------------------------------------------
        #sections hourly, daily, weekly
        bestPerforming = [[hourly_best, hourly_worst], [daily_best, daily_worst], [weekly_best, weekly_worst], [monthly_best, monthly_worst], [sixty_best, sixty_worst], [ninety_best, ninety_worst]]

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