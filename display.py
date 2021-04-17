import operator
from constants import Constants as con
class DisplayData:
    heading = con.heading

    def getPairs(self, percent_change_info):
        #DISPLAY TOP 10
        n = con.numberOfElements
        pairs = []
        for percent_change in percent_change_info:
            best = percent_change[:n+1]
            worst = percent_change[-n:]
            worst.reverse()
            pair = [worst, best]
            pairs.append(pair)
        return pairs
    
    def displaySection(self, pairs, tag):

        for i in range(len(pairs[0])):
            DisplayData.displayData2(DisplayData, pairs[0][i], pairs[1][i],tag)
    
    def displayData2(self, left, right, tag):
        if tag == '1h':
            print(left.displayHourly(),'|', right.displayHourly(),'|')
        elif tag == '24h':
            print(left.displayDaily(),'|', right.displayDaily(),'|')
        elif tag == '7d':
            print(left.displayWeekly(),'|', right.displayWeekly(),'|')
        elif tag == '30d':
            print(left.displayMonthly(),'|', right.displayMonthly(),'|')
        elif tag == '60d':
            print(left.displaySixty(),'|', right.displaySixty(),'|')
        elif tag == '90d':
            print(left.displayNinety(),'|', right.displayNinety(),'|')
        else:
            print('displayData error')

    def displayData(self, percent_change_info):
        #DISPLAY DATA SET
        
        pair_list = DisplayData.getPairs(DisplayData, percent_change_info)
        tags = ['1h', '24h', '7d', '30d', '60d', '90d']
        print(con.stripes, con.stripes)
        i = 0
        for pair in pair_list:
            DisplayData.displaySection(DisplayData, pair, tags[i])
            i += 1
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