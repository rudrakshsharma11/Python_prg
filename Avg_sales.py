def av_sal(sum,num):
    return(sum/num)
print("Avrage sales of a month\n")
s_sale = 0
count = 0
while(count<4):
    rd = float(input("Sales per week {}: ".format(count+1)))
    s_sale += rd
    count = count + 1

avg = av_sal(s_sale, count)

print("The total sales of the months is=", s_sale)
print("Average sale of this month=", avg)