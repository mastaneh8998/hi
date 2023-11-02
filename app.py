from flask import Flask, request, render_template, url_for
from flask_bootstrap import Bootstrap
from bs4 import BeautifulSoup
from flask import session
import json
import qrcode
from jdatetime import date
from datetime import datetime, timedelta
# import lib

today = date.today()
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.secret_key = '12345678'
bootstrap = Bootstrap(app)


# functions
# /////////////////////////////////////////////////////////////////////////////////////////////////
def write_def(room_code):
    with open(f'rooms\\{room_code}.txt', 'w') as file:
        file.write('1')
    now = str(datetime.now())
    with open(f'days\\{room_code}.txt', 'w') as file:
        file.write(now)
# //////////////////////////////////////////////////////////////////////////////////////////////////
def rooms_def(room_code):
    with open(f'rooms\\{room_code}.txt', 'r') as file:
        time_str = int(file.read())
        if time_str > 0:
            with open(f'days\\{room_code}.txt', 'r') as file:
                time_str1 = file.readline().strip()

            time_format1 = '%Y-%m-%d %H:%M:%S.%f'
            time_obj1 = datetime.strptime(time_str1, time_format1)
            current_time1 = datetime.now()
            time_difference1 = current_time1 - time_obj1
            if time_difference1.days > time_str:
                room1_op = open(f'days\\{room_code}.txt', 'w')
                room1_op.write('0')
                room1_r_op = open(f'rooms\\{room_code}.txt', 'w')
                room1_r_op.write('0')
                with open(f'texts\\room-text\\{room_code}.txt', 'w') as file:
                    file.write("0")
            elif time_difference1.days < time_str:
                with open(f'texts\\room-text\\{room_code}.txt', 'w') as file:
                    file.write("1")
        else:
            with open(f'texts\\room-text\\{room_code}.txt', 'w') as file:
                file.write("0")

# //////////////////////////////////////////////////////////////
def rooms_def1(rooms,list2):
    with open(f'texts\\room-text\\{rooms}.txt', 'r') as file:
        room1_rs2 = str(file.read())
        list2.append(room1_rs2)
    
# //////////////////////////////////////////////////////////////
def fun1():
    rooms_def("room1")
    rooms_def("room2")
    rooms_def("room3")
    rooms_def("room4")
    rooms_def("room5")
    rooms_def("room6")
    rooms_def("room7")
    rooms_def("room8")
    rooms_def("room9")
    rooms_def("room10")
    rooms_def("room11")
    rooms_def("room12")
# //////////////////////////////////////////////////////////////

def def_1(code_room,num,string):
    if code_room == num:
        write_def(string)
# //////////////////////////////////////////////////////////////

def def_2(list_name):
    rooms_def1("room1", list_name)
    rooms_def1("room2", list_name)
    rooms_def1("room3", list_name)
    rooms_def1("room4", list_name)
    rooms_def1("room5", list_name)
    rooms_def1("room6", list_name)
    rooms_def1("room7", list_name)
    rooms_def1("room8", list_name)
    rooms_def1("room9", list_name)
    rooms_def1("room10", list_name)
    rooms_def1("room11", list_name)
    rooms_def1("room12", list_name)

# /////////////////////////////////////////////////////////

# class

class Room:
    def __init__(self, code, price, beds, capacity, reservation):
        self.code = code
        self.price = price
        self.beds = beds
        self.capacity = capacity
        self.reservation = reservation
# /////////////////////////////////////////////////////////


room1 = Room(1101, 2000000, 2, 2, False)
room2 = Room(1102, 1500000, 1, 1, True)
room3 = Room(1103, 2000000, 2, 2, False)
room4 = Room(1104, 1650000, 1, 1, False)
room5 = Room(1105, 2500000, 3, 3, False)
room6 = Room(1106, 1900000, 1, 1, False)
room7 = Room(1107, 2300000, 2, 2, False)
room8 = Room(1108, 3000000, 3, 3, False)
room9 = Room(1109, 4100000, 3, 3, False)
room10 = Room(1110, 1500000, 1, 1, False)
room11 = Room(1111, 2800000, 2, 2, False)
room12 = Room(1112, 3900000, 2, 2, False)
# //////////////////////////////////////////////////////
room1_code = "1101"
room2_code = "1102"
room3_code = "1103"
room4_code = "1104"
room5_code = "1105"
room6_code = "1106"
# /////////////////////////////////////////////////////////
@app.route('/')
def home():
    path = url_for('static', filename='music.mp3')
    return render_template('welcome.html', path=path)


# /////////////////////////////////////////////////////////


@app.route('/otherpage-pr')
def new_page_pr():
    fun1()
    list1= []
    def_2(list1)
    return render_template('rooms-persian.html',
                           room1_code=room1.code,
                           room1_price=room1.price,
                           room1_beds=room1.beds,
                           room1_capacity=room1.capacity,
                           room1_reservation=list1[0],
                           room2_code=room2.code,
                           room2_price=room2.price,
                           room2_beds=room2.beds,
                           room2_capacity=room2.capacity,
                           room2_reservation=list1[1],
                           room3_code=room3.code,
                           room3_price=room3.price,
                           room3_beds=room3.beds,
                           room3_capacity=room3.capacity,
                           room3_reservation=list1[2],
                           room4_code=room4.code,
                           room4_price=room4.price,
                           room4_beds=room4.beds,
                           room4_capacity=room4.capacity,
                           room4_reservation=list1[3],
                           room5_code=room5.code,
                           room5_price=room5.price,
                           room5_beds=room5.beds,
                           room5_capacity=room5.capacity,
                           room5_reservation=list1[4],
                           room6_code=room6.code,
                           room6_price=room6.price,
                           room6_beds=room6.beds,
                           room6_capacity=room6.capacity,
                           room6_reservation=list1[5],
                           room7_code=room7.code,
                           room7_price=room7.price,
                           room7_beds=room7.beds,
                           room7_capacity=room7.capacity,
                           room7_reservation=list1[6],
                           room8_code=room8.code,
                           room8_price=room8.price,
                           room8_beds=room8.beds,
                           room8_capacity=room8.capacity,
                           room8_reservation=list1[7],
                           room9_code=room9.code,
                           room9_price=room9.price,
                           room9_beds=room9.beds,
                           room9_capacity=room9.capacity,
                           room9_reservation=list1[8],
                           room10_code=room10.code,
                           room10_price=room10.price,
                           room10_beds=room10.beds,
                           room10_capacity=room10.capacity,
                           room10_reservation=list1[9],
                           room11_code=room11.code,
                           room11_price=room11.price,
                           room11_beds=room11.beds,
                           room11_capacity=room11.capacity,
                           room11_reservation=list1[10],
                           room12_code=room12.code,
                           room12_price=room12.price,
                           room12_beds=room12.beds,
                           room12_capacity=room12.capacity,
                           room12_reservation=list1[11]
                           )



# /////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////

#  english rooms page

@app.route('/otherpage-en')
def other_page():
    fun1()
    
# ////////////////////////////////////////////////////////////////////////////////////////////////////
    list2= []
    def_2(list2)
    
    return render_template('rooms-english.html',
                           room1_code=room1.code,
                           room1_price=room1.price,
                           room1_beds=room1.beds,
                           room1_capacity=room1.capacity,
                           room1_reservation=list2[0],
                           room2_code=room2.code,
                           room2_price=room2.price,
                           room2_beds=room2.beds,
                           room2_capacity=room2.capacity,
                           room2_reservation=list2[1],
                           room3_code=room3.code,
                           room3_price=room3.price,
                           room3_beds=room3.beds,
                           room3_capacity=room3.capacity,
                           room3_reservation=list2[2],
                           room4_code=room4.code,
                           room4_price=room4.price,
                           room4_beds=room4.beds,
                           room4_capacity=room4.capacity,
                           room4_reservation=list2[3],
                           room5_code=room5.code,
                           room5_price=room5.price,
                           room5_beds=room5.beds,
                           room5_capacity=room5.capacity,
                           room5_reservation=list2[4],
                           room6_code=room6.code,
                           room6_price=room6.price,
                           room6_beds=room6.beds,
                           room6_capacity=room6.capacity,
                           room6_reservation=list2[5],
                           room7_code=room7.code,
                           room7_price=room7.price,
                           room7_beds=room7.beds,
                           room7_capacity=room7.capacity,
                           room7_reservation=list2[6],
                           room8_code=room8.code,
                           room8_price=room8.price,
                           room8_beds=room8.beds,
                           room8_capacity=room8.capacity,
                           room8_reservation=list2[7],
                           room9_code=room9.code,
                           room9_price=room9.price,
                           room9_beds=room9.beds,
                           room9_capacity=room9.capacity,
                           room9_reservation=list2[8],
                           room10_code=room10.code,
                           room10_price=room10.price,
                           room10_beds=room10.beds,
                           room10_capacity=room10.capacity,
                           room10_reservation=list2[9],
                           room11_code=room11.code,
                           room11_price=room11.price,
                           room11_beds=room11.beds,
                           room11_capacity=room11.capacity,
                           room11_reservation=list2[10],
                           room12_code=room12.code,
                           room12_price=room12.price,
                           room12_beds=room12.beds,
                           room12_capacity=room12.capacity,
                           room12_reservation=list2[11]
                           )

# /////////////////////////////////////////////////////////

# persian page rooms

# book_price = None

# //////


@app.route('/book_1101')
def book_1101():
    session['book_room_code'] = '1101'
    book_price = room1.price
    return render_template('book_1101.html', book_price=book_price)


@app.route('/book_1102')
def book_1102():
    session['book_room_code'] = '1102'
    book_price = room2.price
    return render_template('book_1101.html', book_price=book_price)


@app.route('/book_1103')
def book_1103():
    session['book_room_code'] = '1103'
    book_price = room3.price
    return render_template('book_1101.html', book_price=book_price)


@app.route('/book_1104')
def book_1104():
    session['book_room_code'] = '1104'
    book_price = room4.price
    return render_template('book_1101.html', book_price=book_price)


@app.route('/book_1105')
def book_1105():
    session['book_room_code'] = '1105'
    book_price = room5.price
    return render_template('book_1101.html', book_price=book_price)


@app.route('/book_1106')
def book_1106():
    session['book_room_code'] = '1106'
    book_price = room6.price
    return render_template('book_1101.html', book_price=book_price)


@app.route('/book_1107')
def book_1107():
    session['book_room_code'] = '1107'
    book_price = room7.price
    return render_template('book_1101.html', book_price=book_price)


@app.route('/book_1108')
def book_1108():
    session['book_room_code'] = '1108'
    book_price = room8.price
    return render_template('book_1101.html', book_price=book_price)

@app.route('/book_1109')
def book_1109():
    session['book_room_code'] = '1109'
    book_price = room9.price
    return render_template('book_1101.html', book_price=book_price)

@app.route('/book_1110')
def book_1110():
    session['book_room_code'] = '1110'
    book_price = room10.price
    return render_template('book_1101.html', book_price=book_price)


@app.route('/book_1111')
def book_1111():
    session['book_room_code'] = '1111'
    book_price = room11.price
    return render_template('book_1101.html', book_price=book_price)

@app.route('/book_1112')
def book_1112():
    session['book_room_code'] = '1112'
    book_price = room12.price
    return render_template('book_1101.html', book_price=book_price)

# /////////////////////////////////////////////////////////


# english page rooms
book_price_en = 1


@app.route('/book_1101_en')
def book_1101_en():
    session['book_room_code_en'] = '1101'
    book_price_en = room1.price
    return render_template('book-en.html', book_price_en=book_price_en)


@app.route('/book_1102_en')
def book_1102_en():
    session['book_room_code_en'] = '1102'
    book_price_en = room2.price
    return render_template('book-en.html', book_price_en=book_price_en)


@app.route('/book_1103_en')
def book_1103_en():
    book_price_en = room3.price
    session['book_room_code_en'] = '1103'
    return render_template('book-en.html', book_price_en=book_price_en)


@app.route('/book_1104_en')
def book_1104_en():
    book_price_en = room4.price
    session['book_room_code_en'] = "1104"
    return render_template('book-en.html', book_price_en=book_price_en)


@app.route('/book_1105_en')
def book_1105_en():
    book_price_en = room5.price
    session['book_room_code_en'] = "1105"
    return render_template('book-en.html', book_price_en=book_price_en)


@app.route('/book_1106_en')
def book_1106_en():
    book_price_en = room6.price
    session['book_room_code_en'] = "1106"
    return render_template('book-en.html', book_price_en=book_price_en)

@app.route('/book_1107_en')
def book_1107_en():
    book_price_en = room7.price
    session['book_room_code_en'] = "1107"
    return render_template('book-en.html', book_price_en=book_price_en)


@app.route('/book_1108_en')
def book_1108_en():
    book_price_en = room8.price
    session['book_room_code_en'] = "1108"
    return render_template('book-en.html', book_price_en=book_price_en)


@app.route('/book_1109_en')
def book_1109_en():
    book_price_en = room9.price
    session['book_room_code_en'] = "1109"
    return render_template('book-en.html', book_price_en=book_price_en)


@app.route('/book_1110_en')
def book_1110_en():
    book_price_en = room10.price
    session['book_room_code_en'] = "1110"
    return render_template('book-en.html', book_price_en=book_price_en)


@app.route('/book_1111_en')
def book_1111_en():
    book_price_en = room6.price
    session['book_room_code_en'] = "1111"
    return render_template('book-en.html', book_price_en=book_price_en)


@app.route('/book_1112_en')
def book_1112_en():
    book_price_en = room6.price
    session['book_room_code_en'] = "1112"
    return render_template('book-en.html', book_price_en=book_price_en)

# /////////////////////////////////////////////////////////
# persian reservation page

@app.route("/next", methods=["POST"])
def room():
    book_room_code = session.get('book_room_code')
    input_day =int(request.form.get("multiplier"))
    input_name = request.form.get('input_name')
    input_user_code = request.form.get("national_code")
    input_name_en = request.form.get("name")
    date_of_birth = request.form.get("date_of_birth")
    input_country = request.form.get("country")
    input_address = request.form.get("inputaddress")
    input_phone_number = request.form.get("inputphonenumber")
    input_result = request.form.get("result")
    file_txt = open(f'texts\\{input_name_en}.txt', "w", encoding='utf-8')
    dic = {'name' : str(input_name) ,'room code' : str(book_room_code) ,'day' : str(input_day) , 'National Code' : str(input_user_code) , 'name_en' : str(input_name_en) , 'date of birth' : str(date_of_birth) , 'country' : str(input_country) , 'address' : str(input_address) , 'phone number': str(input_phone_number) }
    file_txt.write(str(dic))
    file_txt.close()
    # img
    img2 = qrcode.make(str(book_room_code))
    img2.save(
        f'images\\{input_name_en}.png')
    # ////
    def_1(book_room_code , "1101" ,"room1")
    def_1(book_room_code , "1102" ,"room2")
    def_1(book_room_code , "1103" ,"room4")
    def_1(book_room_code , "1104" ,"room4")
    def_1(book_room_code , "1105" ,"room5")
    def_1(book_room_code , "1106" ,"room6")
    def_1(book_room_code , "1107" ,"room7")
    def_1(book_room_code , "1108" ,"room8")
    def_1(book_room_code , "1109" ,"room9")
    def_1(book_room_code , "1110" ,"room10")
    def_1(book_room_code , "1111" ,"room11")
    def_1(book_room_code , "1112" ,"room12")

    # /////
    return render_template('sava.html', national_code=input_user_code, name=input_name, room_code=book_room_code, days=input_day)

# ////////////////////////////////////////////////////////////////////////////////////////////////////////

# english reservation pag
@app.route("/process_en", methods=["POST"])
def process_en():
    book_room_code_en = session.get('book_room_code_en')
    input_day1_en = request.form.get("multiplier_en")
    input_name1 = request.form.get("input_data_en")
    name_en = request.form.get("name")
    input_user_code1 = request.form.get("national_code")
    input_address1 = request.form.get("inputaddressen")
    input_country1 = request.form.get("countryen")
    input_date_of_birth_en = request.form.get("birthen")
    input_phone_number1 = request.form.get("inputphonnumberen")
    input_result1_en = request.form.get("resulten")
    img3 = qrcode.make(str(book_room_code_en))
    img3.save(
        f'images\\{name_en}.png')
    # /////
    file_txt_1 = open(f'texts\\{name_en}.txt', "w" )
    dic1 = {'name' : name_en ,'room code' : str(book_room_code_en) ,'day' : input_day1_en , 'National Code' : input_user_code1  , 'date of birth' : input_date_of_birth_en, 'country' : input_country1 , 'address' : input_address1 , 'phone number': input_phone_number1 }
    file_txt_1.write(str(dic1))
    file_txt_1.close()
    
    def_1(book_room_code_en , "1101" ,"room1")
    def_1(book_room_code_en , "1102" ,"room2")
    def_1(book_room_code_en , "1103" ,"room4")
    def_1(book_room_code_en , "1104" ,"room4")
    def_1(book_room_code_en , "1105" ,"room5")
    def_1(book_room_code_en , "1106" ,"room6")
    def_1(book_room_code_en , "1107" ,"room7")
    def_1(book_room_code_en , "1108" ,"room8")
    def_1(book_room_code_en , "1109" ,"room9")
    def_1(book_room_code_en , "1110" ,"room10")
    def_1(book_room_code_en , "1111" ,"room11")
    def_1(book_room_code_en , "1112" ,"room12")
    # //////////////////////////////////////////////// 
    img1 = qrcode.make(str(book_room_code_en))
    img1.save(f'images\\{name_en}.png')
    return render_template('save_en.html', national_code1=input_user_code1, name1=name_en, room_code1=book_room_code_en, days1=input_day1_en)
# /////////////////////////////////////////////////////////
if __name__ == '__main__':
    app.run(debug=True)
