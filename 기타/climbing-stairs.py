class Solution(object):
    def minCostClimbingStairs(self, cost):
        costlen=len(cost)
        recordcost=[0]*costlen

        for i in range(costlen):
            if i==0 or i==1:
                recordcost[i]=cost[i]
                continue
            
            if recordcost[i-1]>recordcost[i-2]:
                recordcost[i]=recordcost[i-2]+cost[i]
            else:ㄹㄹㄹㅇㅇㅇㅇ
                recordcost[i]=recordcost[i-1]+cost[i]

        # 최종 최소인 return 선택
        '''if recordcost[-1]>recordcost[-2]:
            return recordcost[-2]
        else:
            return recordcost[-1]'''
        return min(recordcost[-2:])
