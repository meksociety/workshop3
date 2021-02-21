from fastapi import FastAPI, Path, Query
from pydantic import BaseModel, Field
from starlette.responses import JSONResponse
from typing import Dict, Optional, List, Tuple
import uvicorn

app = FastAPI()

# 127.0.0.1:3000/
@app.get("/")
def index():
    return JSONResponse(content={"message": "Hello,  World."}, status_code=200)


# 127.0.0.1:3000/profile/Mek
# 127.0.0.1:3000/profile/Poopae
@app.get("/profile/{name}")
def get_path_parameter(name: str):
    print(name)
    return JSONResponse(
        content={"message": f"My name is : {name}"},
        status_code=200,
    )


# 127.0.0.1:3000/profile?start=0&limit=0
# 127.0.0.1:3000/profile?limit=10
# 127.0.0.1:3000/profile?start=0
@app.get("/profile")
def get_query_parameter(start: int = 0, limit: int = 0):
    return JSONResponse(
        content={"message": f"start: {start} limit: {limit}"},
        status_code=200,
    )


@app.get("/books")
def get_books():
    # list of dict
    books = [
        {
            "book_id": 1,
            "book_name": "Harry Potter and Philosopher's Stone",
            "page": 223,
        },
        {
            "book_id": 2,
            "book_name": "Harry Potter and the Chamber of Secrets",
            "page": 251,
        },
        {
            "book_id": 3,
            "book_name": "Harry Potter and the Prisoner of Azkaban",
            "page": 251,
        },
    ]

    return JSONResponse(content={"status": "ok", "data": books}, status_code=200)


# 127.0.0.1:3000/books/1
@app.get("/books/{book_id}")
def get_books_by_id(book_id: int):
    # book_id = 1
    dict_books = [
        {
            "book_id": 1,
            "book_name": "Harry Potter and Philosopher's Stone",
            "page": 223,
        },
        {
            "book_id": 2,
            "book_name": "Harry Potter and the Chamber of Secrets",
            "page": 251,
        },
        {
            "book_id": 3,
            "book_name": "Harry Potter and the Prisoner of Azkaban",
            "page": 251,
        },
    ]

    # หา book ที่ ID นั้น ๆ
    # book_filter = list(filter(lambda book: book["book_id"] == book_id, dict_books))

    # ตรวจสอบความถูกต้องของ result
    # result = book_filter[0] if len(book_filter) > 0 else {}

    book_flitter = {}
    for book in dict_books:
        if book["book_id"] == book_id:
            book_flitter = book

    return JSONResponse(content={"status": "ok", "data": book_flitter}, status_code=200)


class Books(BaseModel):
    id: str
    name: str
    page: int


@app.post("/books")
def create_books(req_body: Books):
    req_body_dict = req_body.dict()
    # req_body_dict
    #   "id":"1",
    #  "name":"Python 101",
    #  "page":500

    id = req_body_dict["id"]
    name = req_body_dict["name"]
    page = req_body_dict["page"]

    print("[ Log ] name", id)
    print("[ Log ] name", name)
    print("[ Log ] page", page)

    # INSERT INTO book

    mock_response = {
        "id": id,
        "name": name,
        "page": page,
    }
    return JSONResponse(
        content={"status": "ok", "data": mock_response}, status_code=201
    )


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=3000, reload=True)

# reload=True
# เหมาะกับตอน dev
# reload=False
# เหมาะกับ production
