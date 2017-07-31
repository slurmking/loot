Share = 0
Platinum_value = "pp"
Gold_value = "gp,"
Silver_value = "sp,"
Copper_value = "cp,"
Remainder_Value = "With a remainder of"
import platform
print "Python Version " +(platform.python_version())
print "\n"
print ("Welcome to Loot Calculator v1.01 for Pathfinder")
print ("For questions please emails ryan@fannon.net")
print "\n"
print("This tool will split the amount of gold equally between party members")
print("and round it to the least ammount of coins")
print "\n"

def User_Input():
  global Gold
  global Silver
  global Copper
  global Players
  global Platinum
  Platinum = input('Please Enter the Total Ammount of Platinum Pieces ') or 0
  Gold = input('Please Enter the Total Ammount of Gold Pieces') or 0
  Silver = input('Please Enter the Total Ammount of Silver Pieces') or 0
  Copper = input('Please Enter the Total Ammount of Copper Pieces ') or 0
  Players = input('Enter ammount of players or hit Enter to calculate personal') or 1

  return
def Convert():
    global Gold
    global Silver
    global Copper
    global Players
    global Platinum
    Copper = int(Platinum) * 1000 + int(Copper)
    Copper = int(Gold) * 100 + int(Copper)
    Copper = int(Silver) * 10 + int(Copper)
    print "Total Copper Value",Copper_value,Copper
    return

def Calculate():
    Share = float(Copper) / int(Players)
    print "Total Share Value",Share
    Real_Platinum = int(Share) / 1000
    Real_Gold = int(Share) / 100 - (int(Real_Platinum) * 10)
    Real_Silver = int(Share) / 10 % 10
    Real_Copper = int(Share) % 10
    Weight = (Real_Platinum + Real_Gold + Real_Silver + Real_Copper) / 50
    print "\n"
    print "========================="
    print "       Gold  Share       "
    print "========================="
    print "Each PLayer Will Be Given"
    print int(Real_Copper),Copper_value,int(Real_Silver),Silver_value,int(Real_Gold),Gold_value,int(Real_Platinum),Platinum_value
    print "That Adds "
    print round(Weight, 2),"Lbs To Their Inventory"
    print "========================="
    print "   slurmking.net/loot    "
    print "========================="
    return

def restart():
  print "\n"
  print "\n"
  input("Press Enter To Calculate Again")
  User_Input()
  Convert()
  Calculate()
  restart()
  return
User_Input()
Convert()
Calculate()
restart()

