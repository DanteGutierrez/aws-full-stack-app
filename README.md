# aws-full-stack-app
Creating a Full stack application using full cloud based tools 

# Backend #
Using aws lambda functions to connect to the api gateway
- Language: Python
- Full CRUD

## Structure: ##
<details>
  <summary><h3>Books</h3></summary>
  
Field | Data Type
------|----------
picture | string
title | string
author | string
genre | enum
price | number
rent_price | number
past_users | dict<date, user_id>
condition | enum
is_hardback | boolean
availability | enum
owner | dict<date, user_id>
</details>

<details>
  <summary><h3>Users</h3></summary>
  
  Field | Data Type
  ------|----------
  name | string
  password | string
  email | string
  address | string
  payment | dict<user_id, card_id>
  role | enum
  rented | dict<date, book_id>
  owned | dict<date, book_id>
</details>
  
<details>
  <summary><h3>Receipts</h3></summary>
  
  Field | Data Type
  ------|----------
  user_id | string
  date | date
  total | number
  purchases | list[[Purchase OBJ]](#purchase-obj)
  payment_id | string
</details>
  

<details>
  <summary><h4>Purchase OBJ</h4>* Not a collection</summary>

  Field | Data Type
  ------|----------
  book_id | string
  price | number
  is_owned | boolean
</details>


## API Documentation ##

* User needs to be authenticated to access any endpoint

Method | Endpoint | Body | Returns | Notes
-------|----------|------|---------|------
GET | /user | null | list of users | query by name
GET | /user/{id} | null | user | 
POST | /user | [User](#users) | created user |
PUT | /user/{id} | [User](#users) | updated user | ignores address
DELETE | /user/{id} | null | null | 
GET | /book | null | list of books | query by title, author, genre, price, condition, isHardback and availability
GET | /book/{id} | null | books | 
POST | /book | [Book](#books) | created book |
PUT | /book/{id} | [Book](#books) | updated book | 
DELETE | /book/{id} | null | null | 
