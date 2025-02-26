##from decimal import Decimal as D
from decimal import *
#
# sum = D(0);
# sum+=D("0.01")
# sum+=D("0.01")
# sum+=D("0.01")
# sum-=D("0.03")


sum = Decimal(0);
sum+=Decimal("0.01")
sum+=Decimal("0.01")
sum+=Decimal("0.01")
sum-=Decimal("0.03")

print(sum)