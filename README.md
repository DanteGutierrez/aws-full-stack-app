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
  cost | number
  purchases | list[Purchase OBJ]
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

Endpoint | Body | Returns | Notes
---------|------|---------|------
