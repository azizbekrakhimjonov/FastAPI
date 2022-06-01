from models import Words, Users2
from start_base import Session
from fastapi import HTTPException, status
import requests as res

class Functions:
    def __init__(self):
        self.request = Session()
        self.temp = 0

    def insert_data(self, txt):
        self.request.begin()
        word = Words(word=txt)
        self.request.add(word)
        self.request.commit()
        return 'success'

    def send_back(self, txt: str):
        lst = []
        back = self.request.query(Words).all()
        for i in back:
            lst.append(i.word)
        for j in lst:
            if txt == j:
                self.temp += 1
                return j
        if self.temp < 1:
            try:
                rs = res.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{txt}")
                response = rs.json()[0]['meanings'][0]['definitions'][0]['definition']
                self.insert_data(f"{txt}: {response}")
                return f"{txt}: {response}"
            except:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Translation with {txt} not found")

    def signup(self, name, surname, age: int):
        self.request.begin()
        add = Users2(name=name, surname=surname, age=age)
        self.request.add(add)
        self.request.commit()
        return "Now you are signed up successfully! Reload page and use limitless-pro translator"

    def authentication(self, name: str, surname: str, age: int):
        lst = []
        query = self.request.query(Users2).all()
        for i in query:
            tup = (i.name, i.surname, i.age)
            lst.append(tup)
        check = (name, surname, age)
        if check in lst:
            raise HTTPException(status_code=status.HTTP_200_OK, detail=f"You are welcome {name}!")
        else:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="Please sign up to use pro edition: type: http://127.0.0.1:8000/signup/")


if __name__ == '__main__':
    pass
    # print(post.signup('ab', 'cd', 12))
    # print(post.authentification('ba', 'b', 1))
    # tries above ...|
