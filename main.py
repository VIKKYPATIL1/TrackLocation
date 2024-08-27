#Library Phone Number is imported for Purforming operation on phone numbers
import phonenumbers
from phonenumbers import geocoder

#imported pycountry to get country of the given phone number
import pycountry

#tkinter to open GUI
from tkinter import Tk, Label, Button, Entry

#phone number to the ISO-3166-1 alpha 2 (two letter) country code, associated with that number
from phone_iso3166.country import phone_country
# tkinter to open GUI
from tkinter import Tk, Label, Button, Entry

import phonenumbers
# imported pycountry to get country of the given phone number
import pycountry
# phone number to the ISO-3166-1 alpha 2 (two letter) country code, associated with that number
from phone_iso3166.country import phone_country
from phonenumbers import geocoder


#NEEL
#Number Function is use for taking phone number as user input
def Number():
    print("----------------------phone number tracking system----------------------")
    print()
    print("""Example :-         Area       code
                                india      +91
                             Indonesia      62
                                Iran        98
                                Iraq        964
                                Ireland     353"""
          )
    A = input("enter area code = ")
    B = input("enter phone number = ")
    number1 = (A + B)
    print(number1)

    return number1

Flag=True
while(Flag):
    print("""----------------------Phone Number Details and Tracking System-----------------------""")
    print("""Type Track  :- 'To get country for phone number' 
    Type  SP :- 'To get Service Provider' 
    Type VPT :- 'To Check Possibility and Validity of Number and Time Zone of given number'
    Type Map :- 'To Open Map And Get The Location'
    Type Esc :- 'To Exit Application'""")
    Option=input("Enter the Above Option = ")
    if Option == "Track":
            #Tanish
        #open GUI and perform operation of tracking the location
        class Location_Tracker:
            def __init__(self, App):
                self.window = App
                self.window.title("Phone number Tracker")
                self.window.geometry("500x400")
                self.window.configure(bg="#3f5efb")
                self.window.resizable(False, False)

                # ___________Application menu_____________
                Label(App, text="Enter a phone number with country code", fg="white", font=("Times", 10), bg="#3f5efb").place(x=150, y=30)
                self.phone_number = Entry(App, width=16, font=("Arial", 15), relief="flat")
                self.track_button = Button(App, text="Track Country", bg="#22c1c3", relief="sunken")
                self.country_label = Label(App, fg="white", font=("Times", 20), bg="#3f5efb")

                # ___________Place widgets on the window______
                self.phone_number.place(x=170, y=120)
                self.track_button.place(x=200, y=200)
                self.country_label.place(x=100, y=280)

                # __________Linking button with countries ________
                self.track_button.bind("<Button-1>", self.Track_location)

            #function tracking the location of number
            def Track_location(self, event):
                phone_number = self.phone_number.get()
                country = "Country is Unknown"
                if phone_number:
                    tracked = pycountry.countries.get(alpha_2=phone_country(phone_number))
                    print(tracked)
                    if tracked:
                        if hasattr(tracked, "official_name"):
                            country = tracked.official_name
                        else:
                            country = tracked.name
                self.country_label.configure(text=country)


        PhoneTracker = Tk()
        MyApp = Location_Tracker(PhoneTracker)
        PhoneTracker.mainloop()



    elif Option == "SP":
#Chetan
        number=Number()
        #importing carrier from phone number to obtain imformation of carrier
        from phonenumbers import carrier
        servicepro = phonenumbers.parse(number)
        print(carrier.name_for_number(servicepro, "en"))



    elif Option== "VPT":
        #NEEL
        number=Number()
        #from phonenumbers importing timezone to obtain timezone of number's location
        from phonenumbers import timezone
        mobileNo=phonenumbers.parse(number)
        print(timezone.time_zones_for_number(mobileNo))
        #checking validity of number
        print("Valid Mobile Number:",phonenumbers.is_valid_number(mobileNo))
        #checking possibility of number
        print("Checking possibility of Number:",phonenumbers.is_possible_number(mobileNo))


    elif Option== "Map":
#Chetan
        number=Number()

        pepnumber = phonenumbers.parse(number)
        location = geocoder.description_for_number(pepnumber, "en")

        #importing API libraru to use different functions of API
        from opencage.geocoder import OpenCageGeocode
        #key Of API OPENCAGE
        key = '6afaabb26b2344e8af1e73ebb125a67b'
        #makes it easy to locate the coordinates of addresses, cities, countries,
        #and landmarks across the globe using third-party geocoders and other data sources.
        geocoder = OpenCageGeocode(key)
        query = str(location)

        results = geocoder.geocode(query)

        print(results)
        print("Latitude And Longitude")
        lat = results[0]['geometry']['lat']
        lng = results[1]['geometry']['lng']

        print("Lat = ", lat, " ", "lng = ", lng)

        #folium makes it easy to visualize data that's been manipulated in Python on an interactive leaflet map.
        import folium

        myMap = folium.Map(location=[lat, lng], zoom_start=4)
        folium.Marker([lat, lng], popup=location).add_to(myMap)

        myMap.save("mylocation.html")
    elif Option=='Esc':
        print("We Wish You Get Your Desire Output")
        Flag=False
    else:
        Flag=True


