
print("Enter 'x' to go back. ")
print("You can choose to calculate speed distance or time.")
choice = (input('Enter your choice: '))
if choice == 'x':
    import MHOME
if choice == 'speed':
    distance_done = int(input("Enter the distance travelled: "))
    time_done = int(input("Enter the time taken: "))
    speed_done = (distance_done/time_done)
    print("The speed was: ")
    print(speed_done)
elif choice == 'distance':
     time_done = int(input("Enter the time taken: "))
     speed_done = int(input("Enter the speed taken: "))
     distance_done = (time_done * speed_done)
     print("The distance travelled was: ")
     print(distance_done)
elif choice == 'time':
    distance_done = int(input("Enter the distance travelled: "))
    speed_done = int(input("Enter the speed travelled at: "))
    time_done = (distance_done/speed_done)
    print("The time taken was: ")
    print(time_done)