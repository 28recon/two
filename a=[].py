with open("c:/input.txt","r") as a:
    books = a.read().splitlines()
for n in range(len(books)) :
    i = books[n].split()    
    books[n] = i
alist = a.readlines()
alist = [line.rstrip("\n") for line in alist]  

##메뉴
def menu():
    print("\n----------\n")
    print('1.도서 추가 \n2.도서 검색 \n3.도서 정보 수정 \n4.도서 삭제 \n5.현재 총 도서 목록 출력 \n6.저장 \n7.프로그램 나가기')
    print("\n----------\n")

while True:
    menu()
    num = int(input("\n수행할 기능의 번호를 입력하세요 : "))
    
    if num == 1 :
        add_book()
    elif num == 2 :
        search_book()
    elif num == 3 :
        modify_book()
    elif num == 4 :
        delete_book()
    elif num == 5 :
        print_book()
    elif num == 6 :
        save_book()    
    elif num == 7 :
        exit_book()

##1번을 눌렀을때: 도서 추가
def add_book():#menu 1
        bookname=input('도서명:')
        person=input('저자:')    
        year=input('출판연도:')
        company=input('출판사명:')
        genre=input('장르:')
        a.append([bookname,person,year,company,genre])

##2번을 눌렀을때: 도서 검색
def search_book():
    ##서브메뉴
        while True:
             print("\n----------\n")
             print("1.도서명 \n2.저자 \n3.출판연도 \n4.출판사명 \n5.장르")
             print("\n----------\n")
             submenu=int(input("메뉴 선택>>"))

             if(submenu==1):
                tmp=0
                search=input('검색할 도서명:')
                for i in range(len(a)):
                     if(a[i][0]==search):
                      print(a[i])
                      tmp+=1

                if(tmp>0):
                     print('총 %d개의 도서를 찾았습니다.'%tmp)
                else:
                     print('없는 도서입니다.')

             elif(submenu==2):
                 tmp=0
                 search=input('검색할 저자:')
                 for i in range(len(a)):
                     if(a[i][1]==search):
                         print(a[i])
                         tmp+=1

                 if(tmp>0):
                     print('총 %d개의 도서를 찾았습니다.'%tmp)
                 else:
                     print('없는 도서입니다.') 

             elif(submenu==3):
                 tmp=0
                 search=input('검색할 출판연도:')
                 for i in range(len(a)):
                     if(a[i][2]==search):
                         print(a[i])
                         tmp+=1

                 if(tmp>0):
                     print('총 %d개의 도서를 찾았습니다.'%tmp)
                 else:
                     print('없는 도서입니다.') 

             elif(submenu==4):
                 tmp=0
                 search=input('검색할 출판사명:')
                 for i in range(len(a)):
                     if(a[i][3]==search):
                         print(a[i])
                         tmp+=1

                 if(tmp>0):
                      print('총 %d개의 도서를 찾았습니다.'%tmp)
                 else:
                     print('없는 도서입니다.') 

             elif(submenu==5):
                 tmp=0
                 search=input('검색할 장르:')
                 for i in range(len(a)):
                     if(a[i][4]==search):
                         print(a[i])
                         tmp+=1

                 if(tmp>0):
                      print('총 %d개의 도서를 찾았습니다.'%tmp)
                 else:
                     print('없는 도서입니다.') 

             elif(submenu==6):
                 break 

##도서 정보 수정                                               
def modify_book():    
         i = int(input("수정할 도서의 번호를 입력하세요: \n")) - 1
         print("1.도서명 \n2.저자 \n3.출판연도 \n4.출판사명 \n5.장르")
         num = int(input("\n무엇을 수정하시겠습니까? : "))
       
         if num==1:
                a[i][0] = input("\n수정내용 : ")
                print("수정되었습니다.")

         elif num==2:
                a[i][1] = input("\n수정내용 : ")
                print("수정되었습니다.")

         elif num==3:
                a[i][2] = input("\n수정내용 : ")
                print("수정되었습니다.")

         elif num==4:
                a[i][3] = input("\n수정내용 : ")
                print("수정되었습니다.")       

         elif num==5:
                a[i][4] = input("\n수정내용 : ")
                print("수정되었습니다.")


##도서 삭제
def delete_book():    
         count=0 ##삭제할 정보 선택시 사용
         list=1 ##책 목록

         for i in range(len(a)):
             print(("%d"+str(a[i]))%list)
             list+=1

             count=int(input('삭제할 도서의 번호를 입력하세요:'))
             a.pop(count-1)
             print('**********')
             print('삭제 완료')
             print('**********')

##현재 총 도서 목록 출력
def print_book():    
         list=1
         if(alist==[]):
             print('도서 추가 먼저 해주시길 바랍니다.')        
         else:
             for i in range(len(alist)):
                 print(("%d"+str(alist[i]))%list)   
                 list+=1

##저장
def save_book():    
         with open('c:/input.txt', 'w') as c:
             for i in range(len(a)):
                 c.write(data[i][0])
                 c.write(" ")
                 c.write(data[i][1])
                 c.write(" ")
                 c.write(data[i][2])
                 c.write(" ")
                 c.write(data[i][3])
                 c.write(" ")
                 c.write(data[i][4])
                 c.write("\n")
         print("저장되었습니다.")



##프로그램 나가기
def exit_book():    
        print("프로그램이 종료되었습니다.")
        exit()

